const { fraction, add, multiply, divide, equal, simplify } = require('mathjs');

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
        var temp = matrix[i][j] + '*' + k;
        matrix[i][j] = simplify(temp);
    }
}