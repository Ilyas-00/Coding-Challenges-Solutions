/**
Problem statement

Write a program that asks for a temperature in degrees celsius, then displays it on the Fahrenheit scale.
The conversion between scales is given by the formula: [°F] = ([°C] x 9/5) + 32.

Input

Prompt user to enter temperature in Celcius, let’s say user entered 40.

Enter Temp in Celsius : 40

Expected output

Calculate temperature in Fahrenheit and display the result:

Temp in Farhenheit: 104

*/
const input = Number(prompt('Enter Temp in Celsius : ')); 
const res = ([input] * 9/5) + 32
console.log('Temp in Farhenheit : '+ res ); 
