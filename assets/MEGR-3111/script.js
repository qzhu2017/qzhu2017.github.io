// script.js
window.onload = function() {
    fetch('names.csv')
        .then(response => response.text())
        .then(text => displayList(text, 'namesList'))
        .catch(error => console.error('Error loading names:', error));

    document.getElementById("selectButton").addEventListener("click", function() {
        var names = document.querySelector("#namesList ul").children;
        var selectedName = names[Math.floor(Math.random() * names.length)].textContent;
        document.getElementById("selectedName").innerHTML = `Selected Name: </br></br><strong>${selectedName}</strong>`;
    });
};

function displayList(text, elementId) {
    //var items = isQuestion ? text.split('\n') : text.split('\n').slice(1);
    var items = text.split('\n');
    var html = '<ul>';
    for (var i = 0; i < items.length; i++) {
        if (items[i].trim() === '') continue;
        var cells = items[i].split(',');
        html += '<li>' + cells[0] + cells[1] + '</li>';
    }
    html += '</ul>';
    document.getElementById(elementId).innerHTML = html;
}

