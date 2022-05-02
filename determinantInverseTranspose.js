const { simplify } = require('mathjs');

var transpose = function(matrix) {
    var rows = matrix.length;
    var columns = matrix[0].length;
    var res = Array(columns);
    res.fill(Array(rows).fill(0));
    for(var i = 0; i < rows; i++)
    {
        for(var j = 0; j < columns; j++)
        {
            res[j][i] = matrix[i][j];
        }
    }
    return res;
}

var determinant = function(matrix) {
    if (matrix.length == 1)
    {
        return matrix[0][0];
    }
    else
    {
        var determinantNumber = 0;
        for(var i = 0; i < matrix.length; i++)
        {
            var temp = multiply(matrix[0][i], pow(-1, i + 1));
            determinantNumber = add(determinantNumber, multiply(temp, determinant(sliceMatrix(matrix, i))));
        }
    }
    return determinantNumber;
}

var sliceMatrix = function(matrix, index) {
    var newMatrix = [];
    var tempMatrix = [];
    for(var i = 0; i < matrix.length; i++)
    {
        if(i != index)
        {
            newMatrix.push(matrix[i].slice(0, index).concat(matrix[i].slice(index + 1)));
        }
    }
    return newMatrix;
}

var adjugate = function(matrix) {
    for(var i = 0; i < matrix.lenght; i++)
    {
        for(var j = 0; j < matrix.length; j++)
        {
            matrix[i][j] = multiply(determinant(sliceMatrix2D(matrix, i, j)), pow(-1, i + j + 3));
        }
    }
    matrix = transpose(matrix);
    return matrix;
}

var sliceMatrix2D = function(matrix, i, j) {
    var pos_r = 0;
    var pos_c = 0;
    var newMatrix = Array(matrix.length - 1);
    newMatrix.fill(Array(matrix[0].length - 1));
    for(var r = 0; r < matrix.length; r++)
    {
        for(var s = 0; s < matrix[0].length; s++)
        {
            if(r != i && s != j)
            {
                newMatrix[pos_r][pos_c] = matrix[r][s];
                if (pos_c < newMatrix[0].lenght - 1)
                {
                    pos_c++;
                }
                else
                {
                    pos_c = 0;
                    pos_r++;
                }
            }
        }
    }
}

var inverse = function(matrix) {
    inverseMatrix = divide(adjugate(matrix), determinant(matrix));
    return inverseMatrix;
}