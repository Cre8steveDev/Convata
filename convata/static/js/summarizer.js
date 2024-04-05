// Simple Javascript to add a little interaction for
// the button click when sending form data to the
// server for conversion

// Retrieve the button by id

const submitBtn = document.querySelector('button');
const fileInput = document.querySelector('#upload_pdf');
const theForm = document.querySelector('form');

// Add event listener
submitBtn.addEventListener('click', (e) => {
  e.preventDefault();

  submitBtn.classList.toggle('loading');
  submitBtn.textContent = 'Summarizing Document... 😎';

  theForm.submit();
});
