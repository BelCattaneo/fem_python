$( document ).ready(function() {

  $("#run").click(function () {
    var size = $("#size").val();
    var top = $("#top").val();
    var right = $("#right").val();
    var bottom = $("#bottom").val();
    var left = $("#left").val();
    var source = $("#source").val();
    
    var compare = false;
    
    var method;
    if ($("#diferencias-finitas").parent().hasClass("active")) {
      method =  "diferencias_finitas";
    } else if( $("#galerkin").parent().hasClass("active")){
      method = "galerkin";
    }else if( $("#analitica").parent().hasClass("active")){
      method = "analitica";
    }

    if( $("#compare").parent().parent().attr("aria-expanded") == "true"){
      compare = true;
      var method2;

      if ($("#diferencias-finitas-to-compare").parent().hasClass("active")) {
        method2 =  "diferencias_finitas";
      } else if( $("#galerkin-to-compare").parent().hasClass("active")){
        method2 = "galerkin";
      }else if( $("#analitica-to-compare").parent().hasClass("active")){
        method2 = "analitica";
      }

    }
      
      if (size > 2) {
        if (compare){
          if(method != method2){
            $.ajax({
              url: '/ajax/calculate_temperatures/',
              data: {
                'size': size,
                'top': top,
                'right': right,
                'bottom': bottom,
                'left': left,
                'source': source,
                'compare': compare,
                'method': method,
                'method2': method2
              },
              dataType: 'json',
              success: function (data) {
                if (data) {
                  console.log(data.fileUrl);
                  $("#plot").attr("src", data.fileUrl)
                }
              }
            });
          } else {
            alert("Los metodos deben ser diferentes")
          }

        } else {
          $.ajax({
            url: '/ajax/calculate_temperatures/',
            data: {
              'size': size,
              'top': top,
              'right': right,
              'bottom': bottom,
              'left': left,
              'source': source,
              'compare': compare,
              'method': method
            },
            dataType: 'json',
            success: function (data) {
              if (data) {
                console.log(data.fileUrl);
                $("#plot").attr("src", data.fileUrl)
              }
            }
          });
        }
      
      }else{
        alert("El numero de nodos laterales debe ser mayor a 2");
      }

    });
});