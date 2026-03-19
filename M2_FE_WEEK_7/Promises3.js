const array = ["very", "Dogs", "cute", "are"];
const newArray = [];
let sentence ="";
const p1 = new Promise(resolve => {setTimeout(resolve,100,array[0])}).then(value => {newArray.push(value)});
const p2 = new Promise(resolve => {setTimeout(resolve,0,array[1])}).then(value => {newArray.push(value)});
const p3 = new Promise(resolve => {setTimeout(resolve,100,array[2])}).then(value => {newArray.push(value)});
const p4 = new Promise(resolve => {setTimeout(resolve,0,array[3])}).then(value => {newArray.push(value)});

Promise.all([p1,p2,p3,p4]).then(() => {newArray.forEach(element => {
    sentence = sentence+element+" ";});console.log(sentence)})