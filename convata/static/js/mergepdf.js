// Simple Javascript to add a little interaction for
// the button click when sending form data to the
// server for conversion

// Retrieve the button by id

const submitBtn = document.querySelector('button');
const file1 = document.querySelector('#first');
const file2 = document.querySelector('#second');
const file3 = document.querySelector('#third');
const theForm = document.querySelector('form');
const honeyPot = document.querySelector('#honeypot');

// Add event listener
submitBtn.addEventListener('click', (e) => {
  e.preventDefault();
  if (!file1.files.length && !file2.files.length)
    return alert(
      `Hey, the idea of merging means "Two or more files coming together" to become one.`
    );

  if (honeyPot.value.length > 0) return;

  submitBtn.classList.toggle('loading');
  submitBtn.textContent = 'File Merging in Progress... 😎';

  theForm.submit();
});
