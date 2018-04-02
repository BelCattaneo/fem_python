

function readValues() {
  return {
    top: parseInt($("#top").val()),
    right: parseInt($("#right").val()),
    left: parseInt($("#left").val()),
    bottom: parseInt($("#bottom").val()),
    size: parseInt($("#size").val()),
    method: $("#method").val()
  }  
}

function matrixToHeatmapNodes(tempMatrix, screenSize){
  let data = [];
  let factor = screenSize / (tempMatrix.length-1);
  for (let i = 0; i < tempMatrix.length; i++) {
    for (let j = 0; j < tempMatrix[i].length; j++) {
      data.push({x : factor * j, y : factor * i, value : tempMatrix[i][j]});
    }    
  }
  return data;
}

function createHeatmapDataObject(tempMatrix, screenSize){
  return {
    max : math.max(math.max(tempMatrix)),
    data : matrixToHeatmapNodes(tempMatrix, screenSize)
  }; 
}

function renderMatrix($elem, matrix, {withRounding} = {}) {
  $elem.empty();

  const render = (tr) => {
    return (elem) => {
      const td = document.createElement("td");
      td.setAttribute("style", "width: fit-content;");
      td.innerHTML = withRounding ? Math.round(elem) : elem;
      tr.appendChild(td);

    }
  }

  
  for(let x = 0; x < matrix.length; x++) {
    let tr = document.createElement("tr");
    tr.setAttribute("style", "width: auto;");
    if(matrix[x].length) {
      for (let y = 0; y < matrix.length; y++) {
        render(tr)(matrix[x][y])
      }
    } else {
      render(tr)(matrix[x])
    }


    $elem.append(tr);
  }
}


