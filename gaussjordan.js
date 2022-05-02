const { simplify } = require('mathjs');

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
    
    if (matrix[x][y] != '0')
    {
        var operation = matrix[x][y];
        for (var i = 0; i < unknowns+1; i++)
        {
            temp = matrix[x][i] + '/' + operation;
            matrix[x][i] = simplify(temp);
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
            var operation = matrix[i][y] + '*-1';
            for (var j = 0; j < unknowns+1; j++)
            {
                temp = matrix[i][j] + '+(' + operation + '*' + matrix[x][j] + ')';
                matrix[i][j] = simplify(temp);
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
        matrix[i][j] = '6';
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