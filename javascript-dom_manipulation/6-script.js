  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      document.querySelector('#character').textContent = data.name;
    })
    .catch(error => console.error('Error:', error));
