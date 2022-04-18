
const titleContainer = document.querySelector('UL#list_movies');

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => {
    response.json()
      .then(data => {
        for (const film of data.results) {
          const itemToAdd = document.createElement('li');
          const textToAdd = document.createTextNode(film.title);
          itemToAdd.appendChild(textToAdd);
          titleContainer.appendChild(itemToAdd);
        }
      });
  })
  .catch(error => {
    console.log(error);
  });
