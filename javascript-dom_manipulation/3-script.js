document.querySelector('#toggle_header').addEventListener('DOMContentLoaded', () => {
  const header = document.querySelector('header');
  if (header.classList.contains('red')) {
    header.classList.toggle('green');
  } else {
    header.classList.toggle('red');
  }
});
