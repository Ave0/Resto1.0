$(function(){
  $("#login_usuario").click(function(){
    var formData = new FormData($('#form_login')[0]);
    if(formData.get('email') != "" && formData.get('password') != ""){
      $.ajax({
        url: 'login/autentificar',
        type: 'POST',
        processData : false,
        contentType: false,
        data:formData,
        success: function(data){
          if(data == "Si_Existe"){
            alert("Correcto");
          }else{
            alert("Usuario o password Incorrectos");
          }
        }
      });
    }else{
      alert("Completar Campos");
    }
  });
});

$(function(){
  $("#registrar_usuario").click(function(){
    var formData = new FormData($('#form_registro')[0]);
    if(formData.get('email') != "" && formData.get('password') != "" && formData.get('nombre') != "" &&
      formData.get('direccion') != "" && formData.get('altitud') != "" && formData.get('longitud') != "" &&
      formData.get('rango_precios') != "" && formData.get('tipo_comida') != "" && formData.get('numero_mesas') != "" &&
      formData.get('tiempo_mesa') != "" && formData.get('password') != "" && formData.get('re_password') != ""){

        if(formData.get('password') == formData.get('re_password')){
          $.ajax({
            url: 'login/registrar',
            type: 'POST',
            processData : false,
            contentType: false,
            data:formData,
            success: function(data){
              console.log(data);
            }
          });
        }else{
          alert("password No Coincide");
        }

    }else{
      alert("Completar Campos");
    }
  });
});
