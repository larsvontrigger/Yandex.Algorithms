# Additional check for cheating
The teacher of the OiMP course ordered a well-known 
psychologist to conduct a full psychological 
examination of all students admitted to the Faculty of 
National Economy and Public Administration in order to 
determine their tendency to cheat before classes began 
and to expel them for cheating before they began 
classes and could disgrace the Faculty of National 
Economy and Public Administration with their crimes. 
The psychologist hired to conduct the examination is 
known for his innovative method, which allows one to 
understand a student's tendency to cheat based on the 
identifier he most frequently uses in programs. Help 
the well-known psychologist determine which students 
are potential criminals. Write a program that will use 
the given program to determine the identifier most 
frequently used in it.

Since different students write programs in different 
programming languages ​​during testing, your program 
must be able to work with any language. Since different 
languages ​​use different keywords, a list of keywords 
in the analyzed language is provided to the program as 
input. All sequences of Latin letters, numbers, and 
underscores that are not keywords and contain at least 
one character that is not a number can be identifiers. 
In some languages, identifiers may begin with a digit, 
while in others they may not. If an identifier cannot 
begin with a digit, then a sequence beginning with a 
digit is not an identifier. In addition, it is 
specified whether the language is case-sensitive to the 
characters used in identifiers and keywords.

## Input format
The first line contains a number n - the number of 
keywords in the language (0 <= n <= 50) and two words C 
and D, each of which is either "yes" or "no". Word C is 
equal to "yes" if identifiers and keywords in the 
language are case-sensitive, and "no" if not. Word D is 
equal to "yes" if identifiers in the language can begin 
with a digit, and "no" if not.

The next n lines contain one word each, consisting of 
Latin letters and underscores - keywords. All keywords 
are non-empty, distinct, and if the language is not 
case-sensitive, they are distinct and case-insensitive. 
The length of each keyword does not exceed 50 
characters.

The program text follows until the end of the input 
data. It contains only characters with ASCII codes from 
32 to 126 and line feeds.

The input data size does not exceed 10 kilobytes. The 
program contains at least one identifier.

## Output format
Output the identifier that appears in the program the 
maximum number of times. If there are several such 
identifiers, you should output the one that appears 
first. If the language in the input data is not 
case-sensitive, you can output the identifier in any 
case