'use strict';
// Saturn is missing from the planetList
// Insert it into the correct position
// bonus for using some built in methods


// Solution 1
var planetList = ["Mercury","Venus","Earth","Mars","Jupiter","Uranus","Neptune"];
planetList.splice(5, 0, "Saturn");
console.log(planetList);

