$(document).ready(function () {

    function validationCheck(input_id) {
      let a = $("#" + input_id).val();

      if (a === "") {
        $("#" + input_id + "_error").text("Please enter a valid value");
        $("#" + input_id).addClass("error");
        return true;
      }

      $("#" + input_id + "_error").text("");
      $("#" + input_id).removeClass("error");
      return false;
    }

    $("input, select").blur(function () {
      validationCheck($(this).attr("id"));
    });

    $("#forget_pass").submit(function (event) {
      let is_email_error = validationCheck("email");
      if ( ! is_email_error) {
//        alert("Your Submission has been sent.");
        return true;
      } else {
//        alert("Error in form.");
        return false;
      }
    });

  });
