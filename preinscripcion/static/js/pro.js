$(document).ready(function(){
  // $.ajax({
  //   url:'/pro/',
  //   type:'GET',
  //   dataType : 'json',
  //   sucess : function(json){
  //     alert(json);
  //     $('.imageDiv').append("<div class='card2 image'><img src='../../media/"+json.image+"' style='width:100%;'><h1>"+json.profesional+"</h1><p class='title1'>"+json.especializacion+"</p><p>Experience: "+json.experiencia+" Years</p><p><button class='btn-r1'>"+json.email+"</button></p></div>")
  //   }
  // })
if($('.dato').val()==0){
  $.get('/areas/',function(res){
    console.log(res);
    $('.before').append("<h2>Areas segun su popularidad</h2>")
    for(var i = 0; i<res.length;i++){
      $('.imageDiv').append("<div class='card2 image' style='max-width: 400px; width: 400px;height: 400px;'><img src='"+res[i].image+"' style='width:100%; height:300px;max-height:300px;'><p><button onclick='window.location.href=`../profesional/"+res[i].name+"/`' class='btn-r1' style='background-color:rgba(78, 78, 78, 0.4);height:100px;'>"+res[i].name+"</button></p></div>")
    }
  });
}
if($('.dato').val()==1){
  $.get('/pro/',function(res){
    console.log(res);
    for(var i = 0; i<res.length;i++){
      $('.imageDiv').append("<div class='card2 image'><img src='"+res[i].image+"' style='width:100%;'><h1>"+res[i].profesional+"</h1><p class='title1'>"+res[i].especializacion+"</p><p>Experience: "+res[i].experiencia+" Years</p><p><button class='btn-r1'>"+res[i].email+"</button></p></div>")
    }
  });
}
if($('.dato').val()==2){
  $.get('/pro2/',function(res){
    console.log(res);
    for(var i = 0; i<res.length;i++){
      $('.imageDiv').append("<div class='card2 image'><img src='"+res[i].image+"' style='width:100%;'><h1>"+res[i].profesional+"</h1><p class='title1'>"+res[i].especializacion+"</p><p>Experience: "+res[i].experiencia+" Years</p><p><button class='btn-r1'>"+res[i].email+"</button></p></div>")
    }
  });
}
if($('.dato').val()==3){
  $.get('/pro3/',function(res){
    console.log(res);
    for(var i = 0; i<res.length;i++){
      $('.imageDiv').append("<div class='card2 image'><img src='"+res[i].image+"' style='width:100%;'><h1>"+res[i].profesional+"</h1><p class='title1'>"+res[i].especializacion+"</p><p>Experience: "+res[i].experiencia+" Years</p><p><button class='btn-r1'>"+res[i].email+"</button></p></div>")
    }
  });
}
if($('.dato').val()==4){
  $.get('/pro4/',function(res){
    console.log(res);
    for(var i = 0; i<res.length;i++){
      $('.imageDiv').append("<div class='card2 image'><img src='"+res[i].image+"' style='width:100%;'><h1>"+res[i].profesional+"</h1><p class='title1'>"+res[i].especializacion+"</p><p>Experience: "+res[i].experiencia+" Years</p><p><button class='btn-r1'>"+res[i].email+"</button></p></div>")
    }
  });
}
if($('.dato').val()==5){
  $.get('/pro5/',function(res){
    console.log(res);
    for(var i = 0; i<res.length;i++){
      $('.imageDiv').append("<div class='card2 image'><img src='"+res[i].image+"' style='width:100%;'><h1>"+res[i].profesional+"</h1><p class='title1'>"+res[i].especializacion+"</p><p>Experience: "+res[i].experiencia+" Years</p><p><button class='btn-r1'>"+res[i].email+"</button></p></div>")
    }
  });
}
if($('.dato').val()==6){
  $.get('/pro6/',function(res){
    console.log(res);
    for(var i = 0; i<res.length;i++){
      $('.imageDiv').append("<div class='card2 image'><img src='"+res[i].image+"' style='width:100%;'><h1>"+res[i].profesional+"</h1><p class='title1'>"+res[i].especializacion+"</p><p>Experience: "+res[i].experiencia+" Years</p><p><button class='btn-r1'>"+res[i].email+"</button></p></div>")
    }
  });
}
if($('.dato').val()==7){
  $.get('/pro7/',function(res){
    console.log(res);
    for(var i = 0; i<res.length;i++){
      $('.imageDiv').append("<div class='card2 image'><img src='"+res[i].image+"' style='width:100%;'><h1>"+res[i].profesional+"</h1><p class='title1'>"+res[i].especializacion+"</p><p>Experience: "+res[i].experiencia+" Years</p><p><button class='btn-r1'>"+res[i].email+"</button></p></div>")
    }
  });
}

if($('.dato').val()==8){
  $('.dropdown').remove()
  $('.before').append("<div class='found'><h2>Busqueda de Profesional</h2> <br><input id='input' type='text' placeholder='Nombre Apellido' value=''></input><a id='a' href='#'><div id='div'>Buscar</div></a></div>")
}

$('#div').click(function(){
  $.get('/exists?profesional='+$('#input').val(), function(res){
    console.log(res);
    for(var i = 0; i<res.length;i++){
      $('.imageDiv').empty()
      $('.imageDiv').append("<div class='card2 image' style='margin-left:65px;'><img src='"+res[i].image+"' style='width:100%;'><h1>"+res[i].profesional+"</h1><p class='title1'>"+res[i].especializacion+"</p><p>Experience: "+res[i].experiencia+" Years</p><p><button class='btn-r1'>"+res[i].email+"</button></p></div>")
    }
    if(res.length==0){
      $('.imageDiv').empty()
      $('.imageDiv').append("<h2 style='margin-left:15px;'> El profesional no esta registrado </h2>")
    }
  });
})

if($('.dato').val()==9){
  $.get('/prof/',function(res){
    console.log(res);
      $('.before').append("<h2>Areas en Ciudad Parra</h2>")
    for(var i = 0; i<res.length;i++){
      $('.imageDiv').append("<div class='card2 image' style='max-width: 400px; width: 400px;height: 400px;'><img src='"+res[i].image+"' style='width:100%; height:300px;max-height:300px;'><p><button onclick='window.location.href=`../profesional/"+res[i].name+"/`' class='btn-r1' style='background-color:rgba(78, 78, 78, 0.4);height:100px;'>"+res[i].name+"</button></p></div>")
    }
  });
}




});
