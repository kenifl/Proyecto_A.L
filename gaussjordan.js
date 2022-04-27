const { fraction } = require('mathjs');

var imprimirEcuacion = (unknowns, matrix,  x = -1, y = -1) => {
    var placeholder = '[]';
    for (var i = 0; i < unknowns; i++)
    {
        var letter = 120
        for (var j = 0; j < unknowns; j++)
        {
            console.log(`${(i == x && j == y) ? placeholder : matrix[i][j]}${String.fromCharCode(letter)} `);
            letter = letter < 122 ? letter + 1 : 97;
            if (j == unknowns - 1)
                console.log('| ');
        }
        console.log(`= ${(i == x && unknowns == y) ? placeholder : matrix[i][unknowns]}`);
    }
    console.log('\n');
}

