$( document ).ready(function() {
  $("#run").click(function () {
      var size = $("#size").val();
      var top = $("#top").val();
      var right = $("#right").val();
      var bottom = $("#bottom").val();
      var left = $("#left").val();
      var source = $("#source").val();
      
      
      var method;
      if ($("#diferencias-finitas").parent().hasClass("active")) {
        method =  "diferencias_finitas";
      } else if( $("#galerkin").parent().hasClass("active")){
        method = "galerkin";
      }
      
      if (size > 2) {
        $.ajax({
          url: '/ajax/calculate_temperatures/',
          data: {
            'size': size,
            'top': top,
            'right': right,
            'bottom': bottom,
            'left': left,
            'source': source,
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
      }else{
        alert("El numero de nodos laterales debe ser mayor a 2")
      }

    });
});