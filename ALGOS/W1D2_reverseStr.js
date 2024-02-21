/* 
  String: Reverse
  Given a string,
  return a new string that is the given string reversed
*/
const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "racecar";
const expected2 = "racecar";

const str3 = "hello";
const expected3 = "olleh";

// i = h - e - l
// j = o - l

const str4 = "";
const expected4 = "";

// take 5-8 mins to write the pseudocode here:

// create the function and decide what params it needs and what it will return
/**
 * Reverse a given string
 * @param {string} str String to be reversed.
 * @returns {string} The given str reversed.
 */
function reversed2(str) {
  var reversed = "";
  for (var i = str.length - 1; i >= 0; i--) {
    reversed += str[i];
  }
  return reversed;
}

function reversed(str) {
  var reversed = "";
  for (var i = 0; i <= str.length - 1; i++) {
    reversed = str[i] + reversed;
  }
  return reversed;
}
// hello
// olleh
function reversedArr(str) {
  var arr = str.split("");
  // console.log(arr);
  for (var i = 0; i < arr.length / 2; i++) {
    temp = arr[i]; // temp = e
    arr[i] = arr[arr.length - 1 - i];
    arr[arr.length - 1 - i] = temp;
  }
  return arr.join("");
}
// console.log(reversedArr(str1));
// console.log(reversed(str1));
// console.log(reversed(str2));
// console.log(reversed(str3));
// console.log(reversed(str4));
var list = [1, 2, 3];
// console.log(list.reverse());

var reversedWord = str1.split("").reverse().join("");

console.log(reversedWord);
