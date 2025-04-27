'use strict';
{
  window.addEventListener('load', () => {
    const menuOpen = document.querySelector('.menu-open');
    const menuClose = document.querySelector('.menu-close');
    const nav = document.querySelector('nav');

    menuOpen.addEventListener('click', function () {
      nav.classList.add('open');
    });
    menuClose.addEventListener('click', function () {
      nav.classList.remove('open');
    });
  });
}
