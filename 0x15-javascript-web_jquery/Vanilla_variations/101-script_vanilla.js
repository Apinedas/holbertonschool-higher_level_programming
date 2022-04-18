
window.onload = () => {
  const addItem = document.querySelector('DIV#add_item');
  const removeItem = document.querySelector('DIV#remove_item');
  const clearList = document.querySelector('DIV#clear_list');
  const container = document.querySelector('UL.my_list');

  addItem.addEventListener('click', () => {
    const itemToAdd = document.createElement('li');
    const textToAdd = document.createTextNode('Item');
    itemToAdd.appendChild(textToAdd);
    container.appendChild(itemToAdd);
  });

  removeItem.addEventListener('click', () => {
    const lastItem = [...container.children].pop();
    if (lastItem) {
      container.removeChild(lastItem);
    }
  });

  clearList.addEventListener('click', () => {
    for (const lastItem of [...container.children]) {
      container.removeChild(lastItem);
    }
  });
};
