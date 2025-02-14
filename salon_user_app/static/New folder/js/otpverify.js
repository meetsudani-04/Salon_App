$(document).ready(function () {

    function validationCheck(input_id) {
      let a = $("#" + input_id).val();

      if (a === "") {
        $("#" + input_id + "_error").text("Please enter a valid value");
        $("#" + input_id).addClass("error");
        return true;
      }

      if (input_id == "otp_v") {
        if (a.length < 6 || a.length > 6) {
          $("#" + input_id + "_error").text("Invalid OTP Code");
          return true;
        }
      }

      $("#" + input_id + "_error").text("");
      $("#" + input_id).removeClass("error");
      return false;
    }

    $("input, select").blur(function () {
      validationCheck($(this).attr("id"));
    });

    $("#resend_otp").click(function(){
      $("#resend_otp_message").addClass("alert alert-success");
      $("#resend_otp_message").text("OTP Send Successfully");

    })

    $("#otpverify_form").submit(function (event) {
      let is_otp_v_error = validationCheck("otp_v");
      if (!is_otp_v_error) {
//        alert("Your Submission has been sent.");
        return true;
      } else {
//        alert("Error in form.");
        return false;
      }
    });

  });
