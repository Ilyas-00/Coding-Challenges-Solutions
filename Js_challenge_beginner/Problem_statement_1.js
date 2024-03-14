/**
Problem statement

Write a program that asks the user for his first name and last name. It then concatenates them and displays them in a single sentence.

Input

Prompt the user for his first and last name, let’s say she entered the following:

Enter FirstName : Dustin
Enter LastName : Tyler

Expected output

Hello, Dustin Tyler

*/

const firstName = prompt('Enter FirstName : '); 
const lastName = prompt('Enter LastName : ');
console.log(`Hello, ${firstName} ${lastName}`); 