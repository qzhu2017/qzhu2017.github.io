// script.js
window.onload = function() {
    fetch('names.csv')
        .then(response => response.text())
        .then(text => displayList(text, 'namesList'))
        .catch(error => console.error('Error loading names:', error));

    document.getElementById("selectButton").addEventListener("click", function() {
        var names = document.querySelector("#namesList ul").children;

        var selectedName = names[Math.floor(Math.random() * names.length)].textContent;

        document.getElementById("selectedName").innerHTML = `<strong>Selected Name: ${selectedName}</strong>`;
    });
};

function displayList(text, elementId) {
    var items = text.split('\n');
    var html = '<ul>';
I    for (var i = 0; i < items.length; i++) {
        if (items[i].trim() === '') continue;
        var cells = rows[i].split(',');
        var name = cells[0] + cells[1];
        html += '<li>' + name + '</li>';
    }
    html += '</ul>';
    document.getElementById(elementId).innerHTML = html;
}

