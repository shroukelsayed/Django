/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
$(function ()
{
    $("#passwordword").on('blur', function () {
        // console.log('zfzdfh');
        var pattern = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,15}$/;
        if ($(this).val().match(pattern))
        {
            $("#repassword").focus();
            $("#span3").html("");
            // console.log('zbzfbzfb');
        } else
        {
            // console.log('SDzdfhzn');
            // alert('8 to 15 characters which contain at least one lowercase letter, one uppercase letter, one numeric digit, and one special character')
            $("#span3").html(" 8 to 15 characters which contain at least one lowercase letter, one uppercase letter, one numeric digit, and one special character");
            $(this).focus();
            // this.select();
        }

    });
    $("#repassword").on('blur', function () {
        if ($("#repassword").val().match($("#password").val()))
        {
            $("#span4").html("");
        } else
        {
            // alert("it's must match password")
            $("#span4").html("it's must match password");
            $("#repassword").focus();
            // upassword.select();
        }

    });
    $("#email").on('blur', function (event) {
        event.preventDefault();
        var pattern = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
        if ($(this).val().match(pattern))
        {
            $.ajax({
                url: 'valid.py',
                type: 'GET',
                // async: false,
                data: {email: $(this).val()},
            })
                    .done(function (event) {
                        console.log(event);
                        if (event == "invalid") {
                            $("#span2").html("enter another email");
                            // $("#email").focus();
                        } else if (event == "valid")
                        {
                            $("#span2").html("This is valid");
                            // console.log('asdfghbjnkm');
                        }
                    })
                    .fail(function () {
                        // console.log("error");
                    })
            // $("#span1").html("");
            // console.log('zbzfbzfb');
        } else
        {
            // console.log('SDzdfhzn');
            // alert('8 to 15 characters which contain at least one lowercase letter, one uppercase letter, one numeric digit, and one special character')
            $("#span2").html("enter a valid email");
            $(this).focus();
            // this.select();
        }
    });
});

