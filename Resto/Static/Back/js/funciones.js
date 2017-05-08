$(function(){
  $("#login_usuario").click(function(){
    var formData = new FormData($('#form_login')[0]);
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
  });
});
