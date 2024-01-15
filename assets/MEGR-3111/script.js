// script.js
window.onload = function() {
    fetch('names.csv')
        .then(response => response.text())
        .then(text => displayList(text, 'namesList'))
        .catch(error => console.error('Error loading names:', error));

    fetch('questions.txt')
        .then(response => response.text())
        .then(text => displayList(text, 'questionsList', true))
        .catch(error => console.error('Error loading questions:', error));

    document.getElementById("selectButton").addEventListener("click", function() {
        var names = document.querySelector("#namesList ul").children;
        var questions = document.querySelector("#questionsList ul").children;

        var selectedName = names[Math.floor(Math.random() * names.length)].textContent;
        var selectedQuestion = questions[Math.floor(Math.random() * questions.length)].textContent;

        document.getElementById("selectedName").innerHTML = `<strong>Selected Name: ${selectedName}</strong>`;
        document.getElementById("selectedQuestion").innerHTML = `<strong>Selected Question: ${selectedQuestion}</strong>`;
    });
};

function displayList(text, elementId, isQuestion = false) {
    //var items = isQuestion ? text.split('\n') : text.split('\n').slice(1);
    var items = text.split('\n');
    var html = '<ul>';
    for (var i = 0; i < items.length; i++) {
        if (items[i].trim() === '') continue;
        html += '<li>' + items[i].trim() + '</li>';
    }
    html += '</ul>';
    document.getElementById(elementId).innerHTML = html;
}

