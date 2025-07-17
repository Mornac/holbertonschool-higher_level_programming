document.addEventListener('DOMContentLoaded', () => {
  const toggleButton = document.querySelector('#toggle_header');
  const header = document.querySelector('header');

  toggleButton.addEventListener('click', () => {
    header.classList.toggle('green');
    header.classList.toggle('red');
  });
});
