
function formValidation() {
// Make quick references to our fields.
var firstname = document.getElementById('firstname');
var addr = document.getElementById('addr');
var zip = document.getElementById('zip');
var state = document.getElementById('state');
var username = document.getElementById('username');
var email = document.getElementById('email');
// To check empty form fields.
if (firstname.value.length == 0) {
document.getElementById('head').innerText = "* All fields are mandatory *"; // This segment displays the validation rule for all fields
firstname.focus();
return false;
}
// Check each input in the order that it appears in the form.
if (inputAlphabet(firstname, "* For your name please use alphabets only *")) {
if (lengthDefine(username, 6, 8)) {
if (emailValidation(email, "* Please enter a valid email address *")) {
if (trueSelection(state, "* Please Choose any one option")) {
if (textAlphanumeric(addr, "* For Address please use numbers and letters *")) {
if (textNumeric(zip, "* Please enter a valid zip code *")) {
return true;
}
}
}
}
}
}
return false;
}
// Function that checks whether input text is numeric or not.
function textNumeric(inputtext, alertMsg) {
var numericExpression = /^[0-9]+$/;
if (inputtext.value.match(numericExpression)) {
return true;
} else {
document.getElementById('p6').innerText = alertMsg; // This segment displays the validation rule for zip.
inputtext.focus();
return false;
}
}
// Function that checks whether input text is an alphabetic character or not.
function inputAlphabet(inputtext, alertMsg) {
var alphaExp = /^[a-zA-Z]+$/;
if (inputtext.value.match(alphaExp)) {
return true;
} else {
document.getElementById('p1').innerText = alertMsg; // This segment displays the validation rule for name.
//alert(alertMsg);
inputtext.focus();
return false;
}
}
// Function that checks whether input text includes alphabetic and numeric characters.
function textAlphanumeric(inputtext, alertMsg) {
var alphaExp = /^[0-9a-zA-Z]+$/;
if (inputtext.value.match(alphaExp)) {
return true;
} else {
document.getElementById('p5').innerText = alertMsg; // This segment displays the validation rule for address.
inputtext.focus();
return false;
}
}
// Function that checks whether the input characters are restricted according to defined by user.
function lengthDefine(inputtext, min, max) {
var uInput = inputtext.value;
if (uInput.length >= min && uInput.length <= max) {
return true;
} else {
document.getElementById('p2').innerText = "* Please enter between " + min + " and " + max + " characters *"; // This segment displays the validation rule for username
inputtext.focus();
return false;
}
}
// Function that checks whether a option is selected from the selector and if it's not it displays an alert message.
function trueSelection(inputtext, alertMsg) {
if (inputtext.value == "Please Choose") {
document.getElementById('p4').innerText = alertMsg; //this segment displays the validation rule for selection.
inputtext.focus();
return false;
} else {
return true;
}
}
// Function that checks whether an user entered valid email address or not and displays alert message on wrong email address format.
function emailValidation(inputtext, alertMsg) {
var emailExp = /^[w-.+]+@[a-zA-Z0-9.-]+.[a-zA-z0-9]{2,4}$/;
if (inputtext.value.match(emailExp)) {
return true;
} else {
document.getElementById('p3').innerText = alertMsg; // This segment displays the validation rule for email.
inputtext.focus();
return false;
}
}
