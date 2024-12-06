# Hypercheckers tournament
Andrey is a referee at a hypercheckers championship. Each game of 
hypercheckers involves three players. During the game, each player scores a 
positive integer number of points. If after the end of the game the first 
player has scored a points, the second player has scored b points, and the 
third player has scored c points, then the game is said to have ended with 
a score of a:b:c.

Andrey knows that the rules of hypercheckers are designed in such a way 
that the scores of any two players differ by no more than k times.

After the match, Andrey shows its result by placing three cards with the 
players' scores on a special board. To do this, he has a set of n cards 
with the numbers x1, x2, …, xn written on them. To find out how prepared he 
is for the championship, Andrey wants to understand how many different 
score options he can show on the board using the cards he has.

He needs to write a program that, given the number k and the values ​​of 
the numbers on the cards Andrey has, determines the number of different 
score options that Andrey can show on the board.

## Input format
The first line of the input file contains two integers: n and k (3 ≤ n ≤ 
100000, 1 ≤ k ≤ 109).

The second line of the input file contains n integers x1, x2, …, xn (1 ≤ xi 
≤ 109).

## Output format
The output file must contain one integer — the required number of different 
counting options.