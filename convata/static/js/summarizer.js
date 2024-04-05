// Simple Javascript to add a little interaction for
// the button click when sending form data to the
// server for conversion

// Retrieve the button by id

const submitBtn = document.querySelector('button');
const fileInput = document.querySelector('#upload_pdf');

// Add event listener
submitBtn.addEventListener('click', (e) => {
  if (fileInput.files.length === 0) return;

  console.log(fileInput.files);

  submitBtn.classList.toggle('loading');
  submitBtn.textContent = 'File Conversion in Progress... 😎';
});
