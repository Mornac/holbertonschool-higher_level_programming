document.querySelector('#toggle_header').addEventListener('DOMContentLoaded', () => {
  const header = document.querySelector('header');
  if (header.classList.contains('red')) {
    header.classList.toggle('red', 'green');
  } else {
    header.classList.toggle('green', 'red');
  }
});
