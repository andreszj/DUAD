const pokemon1 = new Promise(resolve => {
    fetch('https://pokeapi.co/api/v2/pokemon/1')
      .then(res => res.json())
      .then(name => {
        resolve(name["name"])})});
const pokemon2 = new Promise(resolve => {
    fetch('https://pokeapi.co/api/v2/pokemon/2')
      .then(res => res.json())
      .then(name => {
        resolve(name["name"])})});
const pokemon3 = new Promise(resolve => {
    fetch('https://pokeapi.co/api/v2/pokemon/3')
      .then(res => res.json())
      .then(name => {
        resolve(name["name"])})});
        
        
Promise.all([pokemon1,pokemon2,pokemon3]).then((values) => {console.log(values);});