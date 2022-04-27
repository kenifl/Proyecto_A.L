const { fraction, add, multiply, divide, equal } = require('mathjs');

var f = 3
var c = 2
var matrix1 = Array(f);
matrix1.fill(Array(c).fill(0));
var matrix2 = Array(f);
matrix2.fill(Array(c).fill(0));
var res = Array(f);
res.fill(Array(c).fill(0));

//aquí irían asignaciones 

for(var i = 0; i < matrix1.length; i++)
{
    for(var j = 0; j < matrix2[0].length; j++)
    {
        for(var k = 0; k < matrix2.length; k++)
        {
            res[i][j] = add(res[i][j], multiply(matrix1[i][k], matrix2[k][j]));
        }
    }
}

