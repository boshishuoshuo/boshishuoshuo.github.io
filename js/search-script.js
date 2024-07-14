(function() {
    var searchTerm = document.getElementById('search-input').value.toLowerCase();
    var searchResults = document.getElementById('search-results');
    var posts = {{ site.posts | jsonify }};
    
    searchResults.innerHTML = '';
    posts.forEach(function(post) {
      if (post.title.toLowerCase().includes(searchTerm) || post.cipaiming.toLowerCase().includes(searchTerm) || post.zuozhe.toLowerCase().includes(searchTerm)) {
        var resultItem = document.createElement('li');
        resultItem.innerHTML = '<a href="' + post.url + '">' + post.title + '</a>';
        searchResults.appendChild(resultItem);
      }
    });
  })();
  