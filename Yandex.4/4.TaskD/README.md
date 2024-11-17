# Keyboard
At the regional stage of the All-Russian School Olympiad in Computer Science in 
2009, the following problem was proposed.

Everyone knows that over time, a keyboard wears out and the keys on it begin to 
stick. Of course, such a keyboard can still be used for some time, but you have 
to use a lot of force to press the keys.

When a keyboard is manufactured, the number of presses that each key must 
withstand is initially specified. If you know these values ​​for the keyboard you 
are using, then for a certain sequence of pressed keys you can determine which 
keys will break during their use and which will not.

You need to write a program that determines which keys will break during a given 
version of keyboard use.

## Input format
The first line of input data contains an integer n (1 ≤ n ≤ 1000) — the number of 
keys on the keyboard. The second line contains n integers — с1, с2, …, сn, where 
сi (1 ≤ ci ≤ 100000) is the number of keystrokes sustained by the i-th key. The 
third line contains an integer k (1 ≤ k ≤ 100000) — the total number of 
keystrokes, and the last line contains k integers pj (1 ≤ pj ≤ n) — the sequence 
of keys pressed.

## Output format
The program must output n lines containing information about the health of the 
keys. If the i-th key is broken, the i-th line must contain the word YES, if the 
key is working — the word NO.