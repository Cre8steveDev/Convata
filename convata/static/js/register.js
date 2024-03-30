const submitBtn = document.querySelector('button');
const theForm = document.querySelector('form');
const honeyPot = document.querySelector('#honeypot');

// Add event listener
submitBtn.addEventListener('click', (e) => {
  e.preventDefault();

  if (honeyPot.value.length > 0) return;

  submitBtn.classList.toggle('loading');
  submitBtn.textContent = 'Registering You to the Trybe... 😎';

  theForm.submit();
});
