$(document).ready(function(){
var list = []

$.ajaxSetup({
     beforeSend: function(xhr, settings) {
         function getCookie(name) {
             var cookieValue = null;
             if (document.cookie && document.cookie != '') {
                 var cookies = document.cookie.split(';');
                 for (var i = 0; i < cookies.length; i++) {
                     var cookie = jQuery.trim(cookies[i]);
                     // Does this cookie string begin with the name we want?
                     if (cookie.substring(0, name.length + 1) == (name + '=')) {
                         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                         break;
                     }
                 }
             }
             return cookieValue;
         }
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     }
});

$(".materia").click(function(){
  if(this.checked==false){
    list.splice(list.indexOf(this.value),1)
  }else{
    list.push(this.value)
  }
  console.log(list)

});

$("label").click(function(){
  

})

$('#insert').click(function(){
  var info = '';
  for(var i = 0; i<list.length; i++){
    info+= list[i]+',';
  }
  info = info.slice(',', -1);
  $.post('/go/post/',{materias: info}, function(data,status){
    if(data==201){
      $("#label").empty()
      $("#label").append('Ya has seleccionado tus materias');
      location.reload();
    }else if(data==200){
      $("#label").empty()
      $("#label").append('Materias seleccionadas exitosamente');
      location.reload();
    }
  });
});


//HOVER
$(".semestre").attr('title', 'Semestre');
$(".creditos").attr('title', 'Cantidad de creditos pertenecientes a la materia');
$(".teoria").attr('title', 'Horas de teoria');
$(".practica").attr('title', 'Horas de practica');




});
