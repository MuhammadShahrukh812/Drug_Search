function searchDrugs() {
    var searchInput = document.getElementById('searchInput').value;

    // Make a GET request to the Flask API
    fetch(`/search?q=${searchInput}`)
        .then(response => response.json())
        .then(data => displayResults(data))
        .catch(error => console.error('Error:', error));
}

function displayResults(results) {
    var resultsContainer = document.getElementById('results');
    resultsContainer.innerHTML = ''; 

    if (results.length === 0) {
        resultsContainer.innerHTML = '<p>No results found.</p>';
        return;
    }

    var ul = document.createElement('ul');

    results.forEach(function(result) {
        var li = document.createElement('li');
        li.innerHTML = `<strong>Name:</strong> ${result.name}<br>
                        <strong>Description:</strong> ${result.description}<br>
                        <strong>Released:</strong> ${result.released}`;
        ul.appendChild(li);
    });

    resultsContainer.appendChild(ul);
}