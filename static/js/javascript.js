// Copyright solution researched and resourced on stackoverflow
// document.getElementById('copyright-year').appendChild(document.createTextNode(new Date().getFullYear()));

// // script to auto close the alert messages
// setTimeout(function () {
//     let messages = document.getElementById('alert-msg');
//     let alert = new bootstrap.Alert(messages);
//     alert.close();
// }, 2500);

// Example starter JavaScript for disabling form submissions if there are invalid fields
(function () {
    'use strict';

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll('.needs-validation');

    // Loop over them and prevent submission
    Array.prototype.slice.call(forms).forEach(function (form) {
        form.addEventListener(
            'submit',
            function (event) {
                if (!form.checkValidity()) {
                    event.preventDefault();
                    event.stopPropagation();
                }

                form.classList.add('was-validated');
            },
            false
        );
    });
})();
