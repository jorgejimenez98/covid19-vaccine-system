var FormsValidation = (function () {
  /* Trim Values */

  $.each($.validator.methods, function (key, value) {
    $.validator.methods[key] = function () {
      if (arguments.length > 0) {
        arguments[0] = $.trim(arguments[0]);
      }

      return value.apply(this, arguments);
    };
  });
  return {
    init: function () {
      /* Initialize Form Validation */
      $("#form-validation").validate({
        errorClass: "help-block animation-slideDown",
        errorElement: "div",
        errorPlacement: function (error, e) {
          e.parents(".form-group > div").append(error);
        },
        highlight: function (e) {
          $(e)
            .closest(".form-group")
            .removeClass("has-success has-error")
            .addClass("has-error");
          $(e).closest(".help-block").remove();
        },
        success: function (e) {
          e.closest(".form-group").removeClass("has-success has-error");
          e.closest(".help-block").remove();
        },
        rules: {
          val_username: {
            required: true,
            minlength: 3,
          },
          val_password: {
            required: true,
          },
        },
        messages: {
          val_username: {
            required: "El nombre de usuario es obligatorio",
          },
          val_password: {
            required: "La contraseña es obligatoria",
          },
        },
      });
      $("#masked_date").mask("99/99/9999");
      $("#masked_date2").mask("99-99-9999");
      $("#masked_phone").mask("(999) 999-9999");
      $("#masked_phone_ext").mask("(999) 999-9999? x99999");
      $("#masked_taxid").mask("99-9999999");
      $("#masked_ssn").mask("999-99-9999");
      $("#masked_pkey").mask("a*-999-a999");
    },
  };
})();
