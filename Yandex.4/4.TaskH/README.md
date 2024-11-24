# Deciphering Mayan 
Deciphering Mayan writing has proven more challenging than early research 
suggested. Over the course of more than two hundred years, little has been 
learned. The major advances have come in the last 30 years.

Mayan writing is based on small pictures, known as glyphs, that represent sounds. 
Mayan words are usually written using these glyphs, which are arranged next to 
each other in a certain order.

One of the problems with deciphering Mayan writing is determining that order. When 
drawing glyphs for a word, Mayan writers sometimes chose the positions of the 
glyphs based on aesthetic preferences rather than specific rules. This means that 
although the sounds for many glyphs are known, archaeologists are not always sure 
how the written word is supposed to be pronounced.

Archaeologists are looking for a certain word, W. They know the glyphs for it, but 
they don’t know all the possible ways they can be arranged. Since they know you’re 
coming to IOI ’06, they’re asking for your help. They will give you g symbols that 
make up the word W and a sequence S of all the symbols in the inscription they are 
studying, in the order they appear. Help them by counting the number of possible 
occurrences of the word W.

Task Write a program that, given the symbols of the word W and the sequence S of 
symbols in the inscription, counts the number of all possible occurrences of the 
word W in S, that is, the number of all different positions of g consecutive 
symbols in the sequence S that are some permutation of the symbols of the word W .

## Input format
1 ≤ g ≤ 3,000, g is the number of symbols in the word W

g ≤ |S| ≤ 3,000,000 where |S| is the number of symbols in the sequence S

The program receives data in the following format:

LINE 1: Contains two numbers separated by a space – g and |S|. LINE 2: Contains g 
consecutive symbols that are used to write the word W . The allowed characters are 
'a'-'z' and 'A'-'Z'; uppercase and lowercase letters are considered distinct. LINE 
3: Contains |S| consecutive characters that represent the icons in the label. The 
allowed characters are 'a'-'z' and 'A'-'Z'; uppercase and lowercase letters are 
considered distinct.

## Output Format
The program's single output line should contain the number of possible occurrences 
of the word W in S.