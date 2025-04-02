fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    const listMovies = document.getElementById('list_movies');
    data.results.forEach(movie => {
      const item = document.createElement('li');
      item.textContent = movie.title;
      listMovies.appendChild(item);
    });
  })
  .catch(error => console.error('Error:', error));
