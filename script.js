// script.js
function updateClock() {
  var now = new Date();
  var hours = now.getHours() % 12;
  var minutes = now.getMinutes();
  var seconds = now.getSeconds();
  var amPm = hours >= 12 ? 'م' : 'ص';
  hours = hours ? hours : 12; // الساعة '0' تصبح '12'
  document.getElementById('clock').textContent =
    (hours < 10 ? '0' : '') + hours + ':' +
    (minutes < 10 ? '0' : '') + minutes + ':' +
    (seconds < 10 ? '0' : '') + seconds + ' ' + amPm;
}
setInterval(updateClock, 1000);
updateClock(); // initial call to display the clock immediately
