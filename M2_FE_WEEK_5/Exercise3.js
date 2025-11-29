const temperaturesOnCelsius = [12, 18, 22, 25, 30, 15, 9, 28, 33, 20];

const temperaturesOnFahrenheit = temperaturesOnCelsius.map((temperature) => (temperature*9/5)+32);

console.log(temperaturesOnFahrenheit)