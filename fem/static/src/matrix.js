function matrixIndexes(matrix, fn) {
  matrix.forEach((row, y) => {
    row.forEach((node, x) => {
      fn(x, y);
    })
  });
}

function borderInnerMatrixIndexes(matrix, fn) {
  for (let y = 0; y < matrix.length; y++) {
    for (let x = 0; x < matrix[y].length; x++) {
      if(!nodeInBorder(matrix, x, y)) {
        fn(x, y);
      }
    }    
  }
}

function getNodeByIndexes(matrix, x, y) {
  return matrix[y][x];
}

function matrixIndexToArrayIndex(matrixSize, x, y){
  return (x-1) + (y-1) * matrixSize;
}

function clone(obj){
  return JSON.parse(JSON.stringify(obj));
}

function nodeInBorder(matrix, x, y) {
  return (x === 0 || y === 0 || y === matrix.length -1 || x === matrix.length - 1)
}