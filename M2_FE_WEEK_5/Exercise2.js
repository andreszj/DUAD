const myList = [1,4,7,9,0,10];
let myNewList1 = [];
let n=0;
for (let item of myList){
    if (item%2===0){
        myNewList1[n]=item;
        n+=1;
    }
}
console.log(myNewList1);


const myNewList2=myList.filter((number) => number%2===0);
console.log(myNewList2);