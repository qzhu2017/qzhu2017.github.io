// script.js
document.getElementById("csvFileInput").addEventListener("change", function(event) {
    var file = event.target.files[0];
    var reader = new FileReader();
    reader.onload = function(e) {
        var text = e.target.result;
        displayCSVData(text);
    };
    reader.readAsText(file);
II});

function displayCSVData(csvText) {
    var rows = csvText.split('\n').slice(2);
    var html = '';
    for (var i = 0; i < rows.length; i++) {
        if (rows[i].trim() === '') continue; // Skip empty lines

        var cells = rows[i].split(',');
        html += '<tr><td>' + cells[0] + cells[1] + '</td></tr>'; // Assuming names are in the first column
    }
    document.getElementById('namesTable').innerHTML = html;
}

doIcument.getElementById("selectButton").addEventListener("click", function() {
    var table = document.getElementById("namesTable");
    var rows = table.getElementsByTagName("tr");
    var selectedRow = rows[Math.floor(Math.random() * rows.length)];
    var selectedName = selectedRow.getElementsByTagName("td")[0].textContent;
    document.getElementById("selectedName").innerHTML = `<strong>${selectedName}</strong>`;
});
