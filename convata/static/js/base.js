const menuBtn = document.querySelector('#hamburger');
const img = document.querySelector('#hamburger img');
const menuContainer = document.querySelector('.mobile-navigation-container');

menuBtn.addEventListener('click', (e) => {
  e.stopPropagation();

  if (!menuContainer.classList.contains('open')) {
    img.setAttribute('src', '/static/images/menu-close.png');
  } else {
    img.setAttribute('src', '/static/images/menu-open.png');
  }
  menuContainer.classList.toggle('open');
});

// Apply listener on document to close menu on any click
document.querySelector('body').addEventListener('click', (e) => {
  if (menuContainer.classList.contains('open')) {
    menuContainer.classList.remove('open');
    img.setAttribute('src', '/static/images/menu-open.png');
  }
});
