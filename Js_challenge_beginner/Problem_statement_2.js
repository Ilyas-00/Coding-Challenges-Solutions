/**
Problem statement

Write a program that asks the user for a raw price. After that, it calculates the corresponding final price using a VAT rate of 20.6.

Input

Enter Raw Price: 1200

Expected output

Calculate VAT for value given by the user and display the final price, which for the above case is
Final Price: 1447.2 

*/
const input = Number(prompt('Enter Raw Price : ')); 
res = `${input}` *1.206
console.log('Final Price : ' + res);