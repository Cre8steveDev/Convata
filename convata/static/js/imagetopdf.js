// Simple Javascript to add a little interaction for
// the button click when sending form data to the
// server for conversion

// Retrieve the button by id

const submitBtn = document.querySelector('button');
const theForm = document.querySelector('form');
const honeyPot = document.querySelector('#honeypot');

// Add event listener
submitBtn.addEventListener('click', (e) => {
  e.preventDefault();

  if (honeyPot.value.length > 0) return;

  submitBtn.classList.toggle('loading');
  submitBtn.textContent = 'Converting your Image to PDF... 😎';

  theForm.submit();
});
