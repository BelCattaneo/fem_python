function sumBorderNodes(matrix, x, y) {
  return [
    getNodeByIndexes(matrix, x    , y - 1), 
    getNodeByIndexes(matrix, x + 1, y), 
    getNodeByIndexes(matrix, x    , y + 1), 
    getNodeByIndexes(matrix, x - 1, y)
  ].reduce((acc, el) => {
    return acc + el;
  }, 0);
}

function borderInnerMatrixIndexesAndNeighbours(matrix, fn) {
  borderInnerMatrixIndexes(matrix, function(x, y) {
    const neighbours = [
      nodeInBorder(matrix, x  , y-1)? null : {x: x  , y : y-1}, 
      nodeInBorder(matrix, x+1, y  )? null : {x: x+1, y : y  }, 
      nodeInBorder(matrix, x  , y+1)? null : {x: x  , y : y+1}, 
      nodeInBorder(matrix, x-1, y  )? null : {x: x-1, y : y  } 
    ];

    fn(x, y, neighbours);
  });
}

function buildConstantMatrix(matrix) {
  const constants = [];

  borderInnerMatrixIndexes(matrix, (x, y) => {
    constants.push(sumBorderNodes(matrix, x, y));
  })
  
  return constants;
}

function createMatrixFromInputs(temperatures, size) {
  const matrix = [];
  
  for(let j = 0; j < size; j++) {
    matrix.push([]);
    for(let i = 0; i < size; i++) {
      matrix[j][i] = chooseTemperature(temperatures, size, i, j);
    }
  } 

  return matrix;
}

function buildCoeficientMatrix(constantMatrix, matrix){
  let matrixCoeficients = [];
  borderInnerMatrixIndexesAndNeighbours(matrix, function(x, y, neighbours){
    matrixCoeficients.push(coeficientsRow(constantMatrix, matrix, x, y, neighbours));
  })
  return matrixCoeficients;
}

function coeficientsRow(constantMatrix, matrix, x, y, neighbours){
  let coeficientsRow = new Array(constantMatrix.length).fill(0);
  const matrixSize = math.sqrt(constantMatrix.length);
  let currentNodeIndex = matrixIndexToArrayIndex(matrixSize, x, y);
  coeficientsRow[currentNodeIndex] = 4;

  neighbours.forEach(function(neighbour){
    if (neighbour) {
      let neighbourIndex = matrixIndexToArrayIndex(matrixSize, neighbour.x, neighbour.y);
      coeficientsRow[neighbourIndex] = -1;
    }
  })

  return coeficientsRow;
}

// Reemplaza la columna indicada por la matriz de constantes.
function replaceWithConstantMatrix(coeficientMatrix, constantMatrix, index){
  let newCoeficientMatrix = clone(coeficientMatrix);
  for (let i = 0; i < constantMatrix.length; i++) {
    newCoeficientMatrix[i][index] = constantMatrix[i];    
  }
  return newCoeficientMatrix;
}

// Obtiene las temperaturas en los puntos interiores.
function getResults(coeficientMatrix, constantMatrix){
  const determinant = math.bignumber(math.det(coeficientMatrix));

  let results = [];

  for(i = 0; i < constantMatrix.length; i++){
    let currentReplacedMatrix = replaceWithConstantMatrix(coeficientMatrix, constantMatrix, i);
    let currentReplacedMatrixDeterminant = math.bignumber(math.det(currentReplacedMatrix));
    console.log(currentReplacedMatrixDeterminant);

    /*
    if(currentReplacedMatrixDeterminant < 0) {
      console.error(currentReplacedMatrix);
      console.error(constantMatrix);
      console.error(i);
      console.error(currentReplacedMatrixDeterminant);
      throw new Error(`This should not happen!`);
    }
*/
    results.push(math.number(math.divide(currentReplacedMatrixDeterminant, determinant)));
  }

  return results;
}

// Crea la matriz con todas las temperaturas.
function buildFinalMatrix(matrix, results){
  let index = 0;
  let finalMatrix = clone(matrix);
  for (let i = 1; i < finalMatrix.length-1; i++) {
    for (let j = 1; j < finalMatrix[i].length-1; j++) {
      if (finalMatrix[i][j] === 0) {
        finalMatrix[i][j] = results[index];
        index++;
      }      
    }
  }
  return finalMatrix;
}

function diferenciasFinitas(size, temperatures){
  let matrix = createMatrixFromInputs(temperatures, size);
  let constantMatrix = buildConstantMatrix(matrix);
  let coeficientMatrix = buildCoeficientMatrix(constantMatrix, matrix);
  let results = getResults(coeficientMatrix, constantMatrix);  

  return { constantMatrix, coeficientMatrix, finalMatrix: buildFinalMatrix(matrix, results)};
}


/* ------------------------------------------------------------------------------------ */


function chooseTemperature(temperatures, size, x, y) {
  if(x === 0 && y === 0) {
    return (temperatures.top + temperatures.left) / 2;
  }

  if(x === size - 1 && y === size - 1) {
    return (temperatures.right + temperatures.bottom) / 2;
  }

  if(x === size - 1 && y === 0) {
    return (temperatures.right + temperatures.top) / 2;
  }

  if(x === 0 && y === size - 1) {
    return (temperatures.left + temperatures.bottom) / 2;
  }

  if(x === 0) {
    return temperatures.left;
  }

  if(x === size - 1) {
    return temperatures.right;
  }

  if(y === 0) {
    return temperatures.top;
  }

  if(y === size - 1) {
    return temperatures.bottom;
  }

  return 0;
}

