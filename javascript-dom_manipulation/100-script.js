document.addEventListener('DOMContentLoaded', function() {
  // Add item functionality
  document.getElementById('add_item').addEventListener('click', function() {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    document.querySelector('.my_list').appendChild(newItem);
  });

  // Remove last item functionality
  document.getElementById('remove_item').addEventListener('click', function() {
    const list = document.querySelector('.my_list');
    if (list.children.length > 0) {
      list.removeChild(list.lastElementChild);
    }
  });

  // Clear all items functionality
  document.getElementById('clear_list').addEventListener('click', function() {
    const list = document.querySelector('.my_list');
    while (list.firstChild) {
      list.removeChild(list.firstChild);
    }
  });
});
