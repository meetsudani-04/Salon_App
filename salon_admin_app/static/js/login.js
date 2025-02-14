$(document).ready(function () {
  function validationCheck(input_id) {
    let a = $("#" + input_id).val();

    if (a === "") {
      $("#" + input_id + "_error").text("Please enter a valid value");
      $("#" + input_id).addClass("error");
      return true;
    }

    if (input_id === "password" && (a.length < 3 || a.length > 8)) {
      $("#" + input_id + "_error").text("Minimum 3 or maximum 8 characters");
      return true;
    }

    $("#" + input_id + "_error").text("");
    $("#" + input_id).removeClass("error");
    return false;
  }

  function check_all_validation() {
    var is_email_error = validationCheck("email");
    var is_password_error = validationCheck("password");
  
    if (is_email_error || is_password_error) {
      return false;
    }
    return true;
  }

  $("input, select").blur(function () {
    validationCheck($(this).attr("id"));
  });

  $("#login_form").submit(function () {
    let is_valid = check_all_validation();
    if (is_valid) {
//      alert("Your Submission has been sent.");
    } else {
//      alert("Error in form.");
    }
    return is_valid;
  });
  
// Password hide/show
  $("#togglePassword").click(function () {
    var passFieldType = $("#password").attr("type");
    if (passFieldType === "password") {
      $("#password").attr("type", "text");
    } else {
      $("#password").attr("type", "password");
    }
    $(this).toggleClass("bi-eye-slash bi-eye");
  });
  
});
