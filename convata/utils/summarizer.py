"""Merge pdf function handler. Receives the request object and works
With the files the user wants to merge 
"""

import json
import requests
from pypdf import PdfReader
from datetime import datetime
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
from os import environ


def handle_summarize_pdf(req):
    """This function will handle the pdf merge operation"""
    file1: FileStorage  = req.files["file"]
    
    summary_rate = req.form.get("level", "Short Summary")
    
    file_name = secure_filename(file1.filename)
    upload_path = environ["UPLOADS"]
    
    file1.save(f"{upload_path}/{file_name}")
    
    time_string = datetime.now().strftime("%H-%M-%S-%f")
    final_file_name = f"{file_name}_{time_string}.pdf"

    # # Read the pdf file into a reader object
    reader = PdfReader(f"{upload_path}/{file_name}")
    
    # Save pdf text into a string
    pdf_string = ""

    # # # Iterate through the pages and extract the text
    for page in reader.pages:
        pdf_string += page.extract_text()

    # Send string to for AI to summarize
    if len(pdf_string) > 5000:
        pdf_string = pdf_string[0:5000]
    
    url = "https://api.edenai.run/v2/text/generation"

    payload = {
        "response_as_dict": True,
        "attributes_as_list": False,
        "show_original_response": False,
        "temperature": 0,
        "max_tokens": 1000,
        "providers": "openai",
        "text": f"SUMMARIZE THE FOLLOWING TEXT. YOUR RESPONSE SHOULD BE A VERY {summary_rate}. Use the same writing tone as the writing style of the document. IGNORE IRRELEVANT PARTS OF THE DOCUMENT SUCH AS TABLE OF CONTENT, COPYRIGHT NOTICE. ENSURE THE RESPONSE IS PROPERLY FORMATTED FOR EASY OF READING. IMPORTANTLY!!! YOUR RESPONSE SHOULD START WITH THE SUMMARY OF THE TEXT THAT HAS BEEN PROVIDED ONLY. HERE IS THE TEXT TO BE SUMMARIZED: {pdf_string}"
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer " + environ["EDEN_AI"]
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        result = json.loads(response.text)
        
        pdf_summary = result["openai"]["generated_text"]

    except Exception as e:
        print(e)
        pdf_summary = "Sorry! There was an error summarizing the document."

    return {"filename": final_file_name, "summary": pdf_summary}
