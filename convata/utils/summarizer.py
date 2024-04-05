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
    save_path = environ["DOWNLOADS"]
    
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
    
    url = "https://api.edenai.run/v2/text/generation"

    payload = {
        "response_as_dict": True,
        "attributes_as_list": False,
        "show_original_response": False,
        "temperature": 0,
        "max_tokens": 1000,
        "providers": "openai",
        "text": f"SUMMARIZE THE FOLLOWING TEXT. Your response should be a {summary_rate}. Use the same writing tone as the writing style of the document. ENSURE THE RESPONSE IS PROPERLY FORMATTED FOR EASY OF READING \n HERE IS THE DOCUMENT TO BE SUMMARIZED: {pdf_string}"
    }
    
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer " + environ["EDEN_AI"]
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        result = json.loads(response.text)

        # pdf_summary = result['microsoft']['result']
        print(result)

    except Exception as e:
        print(e)
        pdf_summary = "Sorry! There was an error summarizing the document."

    return {"filename": final_file_name, "summary": pdf_summary}
