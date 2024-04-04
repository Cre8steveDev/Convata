const submitBtn = document.querySelector('button');
const theForm = document.querySelector('form');
const honeyPot = document.querySelector('#honeypot');
const pswd1 = document.querySelector('#password1').textContent;
const pswd2 = document.querySelector('#password2').textContent;

// Add event listener
submitBtn.addEventListener('click', (e) => {
  e.preventDefault();

  if (honeyPot.value.length > 0) return;

  if (pswd1 !== pswd2) return alert('Passwords do not match! 😎');

  if (theForm.checkValidity()) {
    submitBtn.classList.toggle('loading');
    submitBtn.textContent = 'Registering You to the Trybe... 😎';
  } else {
    return;
  }

  theForm.submit();
});
