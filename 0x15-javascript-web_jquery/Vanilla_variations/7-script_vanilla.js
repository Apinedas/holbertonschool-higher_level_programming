
const nameContainer = document.querySelector('DIV#character');

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => {
    response.json()
      .then(data => {
        nameContainer.textContent = data.name;
      });
  })
  .catch(error => {
    console.log(error);
  });
