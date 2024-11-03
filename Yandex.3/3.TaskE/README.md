# Calculator
The new OpenCalculator program has a new feature - you can configure which 
buttons are displayed and which are not. If a button is not displayed on the 
screen, then you cannot enter the corresponding number from the keyboard or copy 
it from another program. Petya has configured the calculator so that it displays 
only buttons with the numbers x, y, z. Write a program that determines whether 
Petya can enter the number N, and if not, what is the minimum number of buttons 
that must be additionally displayed on the screen for its entry.

## Input format
First, three different numbers from 0 to 9 are entered: x, y and z (the numbers 
are separated by spaces). Next, an integer non-negative number N is entered that 
Petya wants to enter into the calculator. The number N does not exceed 10000.

## Output format
Display the minimum number of buttons that must be added to be able to enter the 
number N (if the number can be entered using the existing buttons, display 0)