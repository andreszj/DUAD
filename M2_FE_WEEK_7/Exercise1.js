function pairFunction(number, functionA = ()=>{console.log('The number is even!')}, functionB=()=>{console.log('The number is odd!')}){

    if (number%2===0){
        functionA();
    }
    else {
        functionB();
    }
}

pairFunction(4);