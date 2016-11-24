function calcProd() {
	var product = 1;
	for(var i = 1; i < 1000000; i++)
	{
		product = product * i;
	}
	return product;
}

var startTime = new Date().getTime();
prod = calcProd();
var endTime = new Date().getTime();
console.log("The result is " + prod.toString().length + " digits long.");
console.log("It took " + (endTime - startTime) + " seconds to calculate.")
