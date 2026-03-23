const fs = require('fs');

console.log("Reading...");

fs.readFile('document1.csv', 'utf8', (err, document1) => {
    if (err) {
        console.error(err);
        return;
    }

    fs.readFile('document2.csv', 'utf8', (err, document2) => {
        if (err) {
            console.error(err);
            return;
        }

        const arrayWords1 = document1.split(/\r?\n/);
        const arrayWords2 = document2.split(/\r?\n/);

        let phrase = '';

        for (const word1 of arrayWords1) {
            for (const word2 of arrayWords2) {
                if (word1 === word2) {
                    phrase = phrase + word1 + ' ';
                }
            }
        }

        console.log(phrase);
    });
});