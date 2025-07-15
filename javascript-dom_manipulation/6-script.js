document.addEventListener('DOMContentLoaded', () => {
  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
      const characterDiv = document.getElementById('character');
      characterDiv.textContent = data.name;
    })
    .catch(error => {
      console.error('Error fetching data:', error);
    });
});
