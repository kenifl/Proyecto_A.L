const { fraction, add, multiply, divide, equal, simplify } = require('mathjs');

var rows = 3;
var columns = 2;
var matrix1 = Array(rows);
matrix1.fill(Array(columns).fill(0));
var matrix2 = Array(rows);
matrix2.fill(Array(columns).fill(0));
var res = Array(rows);
res.fill(Array(columns).fill(0));

//Aquí irían asignaciones

for(var i = 0; i < rows; i++)
{
    for(var j = 0; j < columns; j++)
    {
        // res[i][j] = add(matrix1[i][j], matrix2[i][j]);
        res[i][j] = simplify(matrix1[i][j], matrix2[i][j]);
    }
}