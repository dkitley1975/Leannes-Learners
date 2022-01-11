// Copyright solution researched and resourced on stackoverflow
// document.getElementById('copyright-year').appendChild(document.createTextNode(new Date().getFullYear()));

// script to auto close the alert messages
setTimeout(function () {
    let messages = document.getElementById('alert-msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2500);
