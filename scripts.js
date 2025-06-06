$(document).ready(function() {
    function updateAlerts() {
        $.getJSON('http://localhost:5001/alerts', function(data) {
            $('#alertsContainer').empty();
            data.forEach(function(alert) {
                var alertElement = $('<div></div>');
                alertElement.append($('<p></p>').text(alert.description));
                alertElement.append($('<p></p>').text(`Source IP: ${alert["source IP"]}`));
                alertElement.appendTo('#alertsContainer');
            });
        });
    }

    $('#filterForm').submit(function(e) {
        e.preventDefault();
        updateAlerts();
    });

    setInterval(updateAlerts, 10000); // Update every 10 seconds
});
