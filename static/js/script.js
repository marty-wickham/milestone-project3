$(document).ready(function () {
    $('#password, #r_password').on('keyup', function () {
        if ($('#password').val() == $('#r_password').val()) {
            $('#message').html('Matching').css('color', 'green');
        } else
            $('#message').html('Not Matching').css('color', 'red');
    });
})