/* 
  Given in an alumni interview
  String Encode
  You are given a string that may contain sequences of consecutive characters.
  Create a function to shorten a string by including the character,
  then the number of times it appears. 

  If final result is not shorter (such as "bb" => "b2" ),
  return the original string.
  */

//
const str1 = "aaaabbcddd";
const expected1 = "a4b2cd3";

const str2 = "";
const expected2 = "";

const str3 = "a";
const expected3 = "a";

const str4 = "bbcc";
const expected4 = "bbcc";

// freqTable = {
//   a: 4,
//   b: 2,
//   c: 1,
//   d: 3,
// };

// // take 5-7 mins to write the pseudocode here:

// // create the function and decide what params it needs and what it will return
// /**
//  *
//  * @param {string} str  The string to encode
//  * @returns {string} The given string encoded
//  */
// function encodeStr(str) {
//   var encoded = "";
//   for (var i = 0; i < str.length; i++) {
//     // i
//     // "aaaa bb c ddd"
//     var currChar = str[i];
//     var dupCount = 1;

//     while (str[i + 1] === currChar) {
//       dupCount++;
//       i++;
//     }
//     // console.log(dupCount);
//     if (dupCount === 1) {
//       encoded += currChar;
//     } else {
//       encoded += currChar + dupCount;
//     }
//   }
//   return encoded.length < str.length ? encoded : str;
// }

// console.log(encodeStr(str1) === expected1);
// console.log(encodeStr(str2) === expected2);
// console.log(encodeStr(str3) === expected3);
// console.log(encodeStr(str4) === expected4);

function freqTable(str) {
  var charFreq = {};
  var encoded = "";

  for (const char of str) {
    if (charFreq[char]) {
      charFreq[char]++;
    } else {
      charFreq[char] = 1;
    }
  }
  // console.log(charFreq);
  for (var char of str) {
    if (charFreq[char] > 0) {
      if (charFreq[char] === 1) {
        encoded += char;
      } else {
        encoded += char + charFreq[char];
        charFreq[char] = 0;
      }
    }
  }

  return encoded.length < str.length ? encoded : str;
}

console.log(freqTable(str1) === expected1);
console.log(freqTable(str2) === expected2);
console.log(freqTable(str3) === expected3);
console.log(freqTable(str4) === expected4);
