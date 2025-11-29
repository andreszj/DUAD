const example = "This is a string!     ";
const result = [];
let i = 0;
let newLetter = '';

for (let letter of example){
    console.log(letter)
    
    if (letter !== ' '){
        newLetter = newLetter + letter;
    }
    else {
        if (newLetter !== ''){
        result[i]=newLetter;
        newLetter = '';
        i+=1;
        }
    }
}

if (newLetter !== '') {
    result[i] = newLetter;
}


console.log(result)