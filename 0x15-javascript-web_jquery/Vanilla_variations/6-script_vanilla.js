
const changeHeader = document.querySelector('DIV#update_header');
const header = document.querySelector('header');

changeHeader.addEventListener('click', () => {
  header.textContent = 'New Header!!!';
});
