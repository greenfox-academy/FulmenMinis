'use strict';
// 1) Subscibe to keyup events on the global window object
// 2) Console log the event object and peek inside
// 3) Display the last pressed key's code as "Last pressed key code is: __"

document.onkeyup = function(event) {
  var h1 = document.querySelector('h1');
  var code = event.which || event.keyCode;
  h1.textContent = "Last pressed key code is: " + code;
}