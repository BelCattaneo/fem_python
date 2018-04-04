const screenSize = 600;

function renderHeatmap(heatmap, tempMatrix, screenSize){
  const n = tempMatrix.length;
  const zeroMatrix = math.zeros(n, n);
  if(!math.deepEqual(zeroMatrix, math.matrix(tempMatrix))){
    heatmap().setData(createHeatmapDataObject(tempMatrix, screenSize));
  }
}

function createHeatmap(){
  return h337.create({
    container: $("#heatmap")[0]
  }); 
}




$(document).ready(function() {
  $('[data-toggle="tooltip"]').tooltip()
  createHeatmap();
  $("#results-container").hide()
  
  /* 
  $("#run").click(function() {
    $("#heatmap").empty();

    const {method, size, top, right, bottom, left}  = readValues();
    const {constantMatrix, coeficientMatrix, finalMatrix} = diferenciasFinitas(size, {top, right, bottom, left});
    if(method == "finite-difference"){
    }
    $("#results-container").show()
    renderMatrix($("#coeficientMatrix"), coeficientMatrix);
    renderMatrix($("#constantMatrix"), constantMatrix);
    renderMatrix($("#finalMatrix"), finalMatrix, {withRounding: true});

    matrixIndexes(finalMatrix, function(x, y) {
      console.log(getNodeByIndexes(finalMatrix, x, y));
    });
    renderHeatmap(createHeatmap, finalMatrix, screenSize);
  }); */

});

//------------------------------------------
//New Main----------------------------------
//------------------------------------------

$( document ).ready(function() {
  $("#run").click(function () {
      var size = $("#size").val();
      var top = $("#top").val();
      var right = $("#right").val();
      var bottom = $("#bottom").val();
      var left = $("#left").val();
      
      $.ajax({
        url: '/ajax/calculate_temperatures/',
        data: {
          'size': size,
          'top': top,
          'right': right,
          'bottom': bottom,
          'left': left
        },
        dataType: 'json',
        success: function (data) {
          if (data) {
            console.log(data.fileUrl);
            $("#plot").attr("src", data.fileUrl)
          }
        }
      });

    });
});