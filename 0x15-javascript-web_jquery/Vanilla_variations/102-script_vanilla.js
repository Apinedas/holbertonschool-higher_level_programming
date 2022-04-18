window.onload = () => {
  const helloContainer = document.querySelector('DIV#hello');
  const translateButton = document.querySelector('INPUT#btn_translate');
  const mainUrl = 'https://fourtonfish.com/hellosalut/?lang=';

  translateButton.addEventListener('click', () => {
    const langContainer = document.querySelector('INPUT#language_code');
    const url = mainUrl + langContainer.value;
    console.log(url);

    fetch(url)
    .then(response => {
      response.json()
        .then(data => {
          helloContainer.textContent = data.hello;
        });
    })
    .catch(error => {
      console.log(error);
    });
  });
};
