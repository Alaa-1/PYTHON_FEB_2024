/* 
  Acronyms
  Create a function that, given a string, returns the string’s acronym 
  (first letter of each word capitalized). 
  Do it with .split first if you need to, then try to do it without
*/
//                  i === "" -> i +1
const strA = "object oriented programming";
const expectedA = "OOP";

// The 4 pillars of OOP
const strB = "abstraction polymorphism inheritance encapsulation";
const expectedB = "APIE";

const strC = "software development life cycle";
const expectedC = "SDLC";

// // Bonus: ignore extra spaces
const strD = "  global   information tracker    ";
const expectedD = "GIT";

// take 5-8 mins to write the pseudocode here:
//* declare an empty str (output)
//* concat the first letter of the first word to our output => o
//? Loop over our str
//?   check if the value at the current index is a space ?
//*     concat the value at index + 1 with the output
//! return the output to upper Case
// create the function and decide what params it needs and what it will return
function acronymize(str) {
  // your code here
  var output = ""; // declare an empty str (output)
  output += str[0]; // concat the first letter of the first word to our output => o
  // output = o
  for (var i = 0; i <= str.length; i++) {
    if (str[i] === " " && str[i + 1] != " ") {
      output += str[i + 1];
      // ouput = "oo" 1st iteration
    }
  }
  return output.toUpperCase();
}

function acronymize(str) {
  // your code here
  var output = ""; // declare an empty str (output)
  output += str[0]; // concat the first letter of the first word to our output => o
  // output = o
  for (var i = 0; i <= str.length; i++) {
    if (str[i] === " " && str[i + 1] != " ") {
      output += str[i + 1];
      // ouput = "oo" 1st iteration
    }
  }
  return output.toUpperCase();
}
//TODO
function acronymizeD(str) {
  // your code here
  var output = []; // declare an empty str (output)
  output.push(str[0]); // concat the first letter of the first word to our output => o
  // output = o
  for (var i = 0; i <= str.length; i++) {
    if (str[i] === " " && str[i + 1] != " ") {
      output.push(str[i + 1]);
      // ouput = "oo" 1st iteration
    }
  }
  return output.join("").toUpperCase();
}
console.log(acronymizeD(strD));
