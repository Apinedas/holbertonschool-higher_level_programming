window.onload = () => {
  const helloContainer = document.querySelector('DIV#hello');

  fetch('https://fourtonfish.com/hellosalut/?lang=fr')
    .then(response => {
      response.json()
        .then(data => {
          const textToAdd = document.createTextNode(data.hello);
          helloContainer.appendChild(textToAdd);
        });
    })
    .catch(error => {
      console.log(error);
    });
};
