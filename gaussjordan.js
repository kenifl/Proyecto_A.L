const { fraction, add, multiply, divide, equal } = require('mathjs');

var imprimirEcuacion = (unknowns, matrix,  x = -1, y = -1) => {
    var placeholder = '[]';
    for (var i = 0; i < unknowns; i++)
    {
        var letter = 120
        for (var j = 0; j < unknowns; j++)
        {
            process.stdout.write(`${(i == x && j == y) ? placeholder : matrix[i][j]}${String.fromCharCode(letter)} `, );
            letter = letter < 122 ? letter + 1 : 97;
            if (j == unknowns - 1)
                process.stdout.write(' ');
        }
        process.stdout.write(`| ${(i == x && unknowns == y) ? placeholder : matrix[i][unknowns]}`);
        process.stdout.write('\n');
    }
    process.stdout.write('\n');
}

var one = (unknowns, matrix, x, y) => {
    console.log('one');
    
    if (!equal(matrix[x][y], fraction(0, 1)))
    {
        var operation = matrix[x][y];
        for (var i = 0; i < unknowns+1; i++)
        {
            matrix[x][i] = divide(matrix[x][i], operation);
        }
    }
    imprimirEcuacion(unknowns, matrix);
}

var zeros = (unknowns, matrix, x, y) => {
    console.log('zero');
    for (var i = 0; i < unknowns; i++)
    {
        if(i != x)
        {
            var operation = multiply(matrix[i][y], fraction(-1, 1));
            for (var j = 0; j < unknowns+1; j++)
            {
                matrix[i][j] = add(matrix[i][j], multiply(operation, matrix[x][j]));
            }
        }
    }
    imprimirEcuacion(unknowns, matrix);
}

var unknowns = parseInt(process.argv[2]);
console.log(unknowns)
var matrix = Array(unknowns);
matrix.fill(Array(unknowns+1).fill(0));

for (var i = 0; i < unknowns; i++)
{
    for (var j = 0; j < unknowns+1; j++)
    {
        imprimirEcuacion(unknowns, matrix, i, j);
        matrix[i][j] = fraction(2, 1);
    }
}
console.log('\n');
imprimirEcuacion(unknowns, matrix);
for(var i = 0; i < unknowns; i++)
{
    one(unknowns, matrix, i, i);
    zeros(unknowns, matrix, i, i);
}
console.log('Resultado: ');
imprimirEcuacion(unknowns, matrix);