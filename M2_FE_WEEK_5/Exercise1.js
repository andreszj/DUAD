const myList = [1,4,7,9,0,10];

for (const item of myList){
    console.log(item)
}

// 2-ways

function printItems(item){
    console.log(item)
}
myList.forEach(printItems)

