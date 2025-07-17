  document.addEventListener('DOMContentLoaded', () => {
    fetch('https://swapi-api.hbtn.io/api/people/5/?format=json'URL)
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        document.querySelector('#character').textContent = data.name;
      })
      .catch(error => console.error('Error:', error));
  });

