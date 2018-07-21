/*

In JavaScript, define a function `makeCounter` which takes one optional argument defining the intial value, `start`, 
with a default value of 0. The function should return an object containing keys that define 3 methods:
  - `value` returns the current value of the counter
  - `increment` increments the value of the counter by 1 and returns the new value
  - `decrement` decrements the value of the counter by 1 and returns the new value

The returned object should not allow direct modification or retrieval of the value.

Example usage:

var counter = makeCounter();
console.log(counter.value());
// 0

var counter2 = makeCounter(4);

console.log(counter2.value());
// 4

console.log(counter2.increment());
// 5
console.log(counter2.value());
// 5

counter2.decrement();
counter2.decrement();
console.log(counter2.decrement());
// 2

*/





function makeCounter(start){
	//console.log("params - >" + start)
	
	//console.log(start)
	if(start === undefined){
		start = 0
	}
	let object = {

		value :function(params){
			if(params === undefined){
				
				return start	
			}
			
		},

		increment :function(params){
			
			if(params === undefined){
				start = start+1
				return start
			}
			
		},

		decrement :function(params){
			if(params === undefined){
				start = start-1
				return start
			}
		}	
	};
	return object
}

var counter = makeCounter();
console.log("val 0->"+counter.value());
// 0

var counter2 = makeCounter(4);

console.log("val 4->"+counter2.value());
// 4

console.log("increment 5->"+counter2.increment());
// 5
console.log("val 5->"+counter2.value());
// 5

counter2.decrement();
counter2.decrement();
console.log("decrement 2->"+counter2.decrement());
// 2

function minArgs(...params){
	console.log(params.length)
	let min = 0
	params.forEach(function(ele) {
  		if(ele < min){
  			min = ele
  		}
	});
	return min
}



console.log(minArgs(1, -6, 78, 12, 45.5, -6.9, 98, 4.7, 2.3))



function group(collection, grouper){
	obj ={}
	collection.forEach((ele)=>{
		let fele = grouper(ele)
		if(obj[fele] === undefined){
			obj[fele]=[]
			obj[fele].push(ele)
		}else{
			obj[fele].push(ele)
		}
	})
	return obj
}

console.log(group([6.5, 4.2, 6.3, 9 , 5.5, 6.3, 4.1, 9.6, 7.5, 2.2, 2.4, 5.4], Math.floor))