var FormsValidation = (function () {
  $.validator.addMethod("ciValidation", function (value) {
    const regex = /^.{11,11}$/;
    if (!regex.test(value)) {
      return false;
    }
    return true;
  });
  $.validator.addMethod("no_letters", function (value) {
    const regex = /[^A-Za-z]+/;
    if (!regex.test(value)) {
      return false;
    }
    return true;
  });

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
          val_name: {
            required: true,
          },
          val_last_names: {
            required: true,
          },
          val_sex: {
            required: true,
          },
          val_adress: {
            required: true,
          },
          val_consult: {
            required: true,
          },
          val_age: {
            required: true,
            range: [1, 130],
          },
          val_ci: {
            required: true,
            no_letters: true,
            ciValidation: true,
          },
        },
        messages: {
          val_name: {
            required: "El nombre es obligatorio",
          },
          val_last_names: {
            required: "Los apellidos son obligatorios",
          },
          val_sex: {
            required: "El sexo es obligatorio",
          },
          val_adress: {
            required: "La dirección es obligatoria",
          },
          val_consult: {
            required: "Debes seleccionar un consultorio",
          },
          val_age: {
            required: "La edad es obligatoria",
            range: "Debe estar entre 1 y 130 años",
          },
          val_ci: {
            required: "El CI es obligatorio",
            no_letters: "El Ci no debe contener letras",
            ciValidation: "El Ci solo debe contener 11 caracteres",
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
