/* 
  Given an arr and a separator string, output a string of every item in the array separated by the separator.
  
  No trailing separator at the end
  Default the separator to a comma with a space after it if no separator is provided
*/
//                   v
const arr1 = [1, 2, 3];
const separator1 = ", ";
const expected1 = "1, 2, 3";

const arr2 = [1, 2, 3];
const separator2 = "-";
const expected2 = "1-2-3";

const arr3 = [1, 2, 3];
const separator3 = " - ";
const expected3 = "1 - 2 - 3";

const arr4 = [1];
const separator4 = ", ";
const expected4 = "1";

const arr5 = [];
const separator5 = ", ";
const expected5 = "";

// pseucode
/**
 * @param {Array<string|number|boolean>} arr
 * @param {String} separator
 * @returns {String}
 */

// Student Solution
function join(arr, separtor) {
  var joined = ""; //                               i
  for (var i = 0; i < arr.length; i++) {
    // console.log("=>", arr[i]);
    if (i === arr.length - 1) {
      joined += arr[i];
    } else {
      // console.log("=>", arr[i]);
      joined += arr[i] + separtor;
    }
  }
  return joined;
}

// console.log(join(arr1, separator1));
// console.log(join(arr2, separator2));
// console.log(join(arr3, separator3));
// console.log(join(arr4, separator4));
// console.log(join(arr5, separator5));

function join2(arr, separtor) {
  var joined = "";
  // if arr is empty return an empty string
  if (!arr.length) {
    return joined;
  }
  for (var i = 0; i < arr.length - 1; i++) {
    joined += arr[i] + separtor;
  }
  return joined + arr[arr.length - 1];
}

console.log(join2(arr5, separator5) === expected5);
