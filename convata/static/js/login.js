const submitBtn = document.querySelector('button');
const theForm = document.querySelector('form');
const honeyPot = document.querySelector('#honeypot');

// Add event listener
submitBtn.addEventListener('click', (e) => {
  e.preventDefault();

  if (honeyPot.value.length > 0) return;

  if (theForm.checkValidity()) {
    submitBtn.classList.toggle('loading');
    submitBtn.textContent = 'Granting you access... 😎';
  } else {
    return;
  }

  theForm.submit();
});

// Set Up show password or hide password

const show_hide_btn = document.querySelector('.password-hint');
const pwd_field = document.querySelector('#password1');

show_hide_btn.addEventListener('click', (e) => {
  if (show_hide_btn.textContent === 'Show Password') {
    show_hide_btn.textContent = 'Hide Password';

    pwd_field.setAttribute('type', 'text');
    return;
  }

  // Otherwise set the field to password again
  show_hide_btn.textContent = 'Show Password';
  pwd_field.setAttribute('type', 'password');
  return;
});
