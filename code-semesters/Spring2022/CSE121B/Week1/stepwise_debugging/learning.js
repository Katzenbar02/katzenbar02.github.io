
let currentDateAndTime = Date()

console.log("It is now "+currentDateAndTime)


let theTotal = total(1,12,7,9,5,6,52)

console.log("The total is "+theTotal)


function total(...theNumbers){
	let sum = 0
	let totalsum = 0
	for(let aNumber in theNumbers){
		sum = parseFloat(aNumber)//Want to know why aNumber is multiplied by 1? Remove it and find out. :)
		totalsum += theNumbers[sum]
	}
	return totalsum
}
