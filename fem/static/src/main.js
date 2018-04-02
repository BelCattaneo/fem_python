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
  });

});