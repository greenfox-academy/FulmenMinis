'use strict';
function prison(person) {
  var person = person;
  let fugitive = 1;
  let visits = 0;

  let prisonFunction = {
    visit: function () {
      if (fugitive === 0) {
        console.log("Nobody is here anymore");
      } else {
        visits++;
        console.log(person + " is visited " + visits + " time(s)");        
      }  
    },
    escape: function () {
      console.log("BREAKING NEWS, " + person + " escaped the prison");
      fugitive = 0;
    }
  }
  return prisonFunction;
}




// Create a prison function, that has your name as a private fugutive variable
// The function should return an object that has two methods:
//  - visit() // logs "[yourname] is visited [x] time(s)" to the console.
//    - the [x] times displayes the numbers the function is called
//    - If the fugitive variable is empty, then display "Nobody is here anymore"
//  - escape() // logs "BREAKING NEWS, [yourname] escaped the prison" to the console.
//    - it should empties the fugitive variable

const alcatraz = prison('Sad Panda');

alcatraz.visit() // Sad Panda is visited 1 time(s)
alcatraz.visit() // Sad Panda is visited 2 time(s)
alcatraz.escape() // BREAKING NEWS, Sad Panda escaped the prison
alcatraz.visit() // Nobody is here anymore