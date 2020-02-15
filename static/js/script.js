$(document).ready(function () {
    $(document).ready(function(){
            
            // A function that will check the length of the user input and return an alert if the passowrd is not long enough
            $("#password").on("focus", function(){

                $("#password").on("keyup", function(){
                    $("#passwordMessage").html("Password must contain at least 8 characters");
                    if($("#password").val().length >= 8 || $("#password").val().length == 0){
                        $("#passwordMessage").html("")
                    }
                });
            });

            $("#password").on("blur", function(){
                if($("#password").val().length >= 8 || $("#password").val().length == 0){
                    $("#passwordMessage").html("");
                }  
            });
            

            // A function to validate that the repeat password matches the password field
            $("#r-password").on("focus", function(){

            });

            $('#r-password').on('keyup', function(){
                if ($("#r-password").val() != 0) {
                    if ($('#r-password').val() != $('#password').val()) {
                        $('#r-password-message').html("Passwords do not match!");
                        $('#register-btn').attr("disabled", "disabled");
                    }
                    else {
                        $('#r-password-message').html("Passwords Match!")
                        $('#register-btn').removeAttr("disabled")
                    }
                }
                else {
                    $('#r-password-message').html("")
                    $('#register-btn').removeAttr("disabled")
                }
            })
        });
})