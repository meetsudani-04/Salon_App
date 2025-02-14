$(document).ready(function () {
  function validationCheck(input_id) {
    let value = $("#" + input_id).val();

    if (value === "") {
      $("#" + input_id + "_error").text("Please enter a valid value");
      $("#" + input_id).addClass("error");
      return true;
    }

    if (input_id === "new_password" || input_id === "confirm_password") {
      if (value.length < 3 || value.length > 8) {
        $("#" + input_id + "_error").text("Minimum 3 or maximum 8 characters");
        return true;
      }

      // password match
      let new_password = $("#new_password").val();
      let confirm_password = $("#confirm_password").val();

      if (new_password !== confirm_password) {
        $("#confirm_password_error").text("Passwords do not match");
        return true;
      } else {
        $("#confirm_password_error").text("");
      }
    }

    $("#" + input_id + "_error").text("");
    $("#" + input_id).removeClass("error");
    return false;
  }

  function check_all_validation() {
    var is_new_password_error = validationCheck("new_password");
    var is_confirm_password_error = validationCheck("confirm_password");

    if (is_new_password_error || is_confirm_password_error) {
      return false;
    }
    return true;
  }

  $("input, select").blur(function () {
    validationCheck($(this).attr("id"));
  });

  $("#resetpass_form").submit(function () {
    let is_valid = check_all_validation();
    if (is_valid) {
      alert("Your Submission has been sent.");
    } else {
      alert("Error in form.");
    }
    return is_valid;
  });

  // Password hide/show
  $("#togglePassword").click(function () {
    var passFieldType = $("#new_password").attr("type");
    if (passFieldType === "password") {
      $("#new_password").attr("type", "text");
//       $("#confirm_password").attr("type", "text");
    } else {
      $("#new_password").attr("type", "password");
//       $("#confirm_password").attr("type", "password");
    }
    $(this).toggleClass("bi-eye-slash bi-eye");
  });
});
