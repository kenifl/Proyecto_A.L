const { fraction, add, multiply, divide, equal } = require('mathjs');

var k = 3;
var f = 2;
var c = 2;

var matrix = Array(f);
matrix.fill(Array(c).fill(0));

//aquí irían asignaciones

for(var i = 0; i < f; i++)
{
    for(var j = 0; j < c; j++)
    {
        matrix[i][j] = multiply(matrix[i][j], k);
    }
}