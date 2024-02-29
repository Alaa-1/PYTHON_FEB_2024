/* 
  Given a string,
  return a new string with the duplicates excluded
  
*/
//? Return the last occurence of the character

const str1 = "abcABC";
const expected1 = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

const str3 = "";
const expected3 = "";

const str4 = "aa";
const expected4 = "a";

// BONUS
// const str5 = "solo";
// const expected5 = "slo";

// pseudocode here
// * created an empty object ( freqTable = {})
// * created an empty string ( result = "")
//* Iterate over the given string
//? if the freqTable has the current char
//? add the current char to the freqTable
//! else if the char already exists increment its value
//* We Iterate over the freqTable
//? concatenate every key in the result string

//* RETRUN RESULT

// create the function and decide what params it needs and what it will return
/**
 * return a new string with the duplicates excluded
 * @param {string} str
 * @returns {string}
 */
function strDedupe(str) {
  var freqTable = {};
  var result = "";

  for (var i = str.length - 1; i >= 0; i--) {
    var currChar = str[i];
    if (!freqTable.hasOwnProperty(currChar)) {
      result = currChar + result;
      freqTable[currChar] = true;
    }
  }
  return result;
}
console.log(strDedupe("solo"));
