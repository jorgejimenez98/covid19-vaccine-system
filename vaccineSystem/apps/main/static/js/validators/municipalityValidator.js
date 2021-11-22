var FormsValidation = (function () {
    $.validator.addMethod(
      "noEmptySpaces",
      function (value) {
        if (value.trim() === "") {
          return false;
        }
        return true;
      },
      "* No debe contener espacios en blanco"
    );
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
            val_province_id: {
              required: true,
            },
          },
          messages: {
            val_name: {
              required: "El nombre completo es obligatorio",
            },
            val_province_id: {
              required: "Debes seleccionar una provincia",
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
  