
const addItem = document.querySelector('DIV#add_item');
const container = document.querySelector('UL.my_list');

addItem.addEventListener('click', () => {
  const itemToAdd = document.createElement('li');
  const textToAdd = document.createTextNode('Item');
  itemToAdd.appendChild(textToAdd);
  container.appendChild(itemToAdd);
});
