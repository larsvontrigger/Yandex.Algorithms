# Alien genome
The genome of the inhabitants of the Tau Ceti system contains 26 types of bases, 
for which we will use the letters of the Latin alphabet from A to Z, and the 
genome itself is written as a line of Latin letters. An important role in the 
genome is played by pairs of adjacent bases, for example, in the genome "ABBACAB" 
the following pairs of bases can be distinguished: AB, BB, BA, AC, CA, AB.

The degree of proximity of one genome to another genome is the number of pairs of 
adjacent bases of the first genome that are found in the second genome.

## Input format
You are given two genomes, determine the degree of proximity of the first genome 
to the second genome. The program receives two lines of capital Latin letters as 
input. Each line is non-empty, and its length does not exceed 105.

## Output format
The program must output one integer - the degree of proximity of the genome 
written in the first line to the genome written in the second line.