# Turtles
The following problem for younger students is widely known. Three turtles are 
crawling along the road. One turtle says: “There are two turtles ahead of me.” 
Another turtle says: “There are two turtles behind me.” The third turtle says: 
“There are two turtles ahead of me and two turtles behind me.” How can this be? 
Answer: the third turtle is lying! N turtles are moving along the road one after 
another. Each turtle says a phrase like: “There are ai turtles ahead of me and bi 
turtles behind me.” Your task is to determine the greatest number of turtles that 
can tell the truth.

## Input format
The first line contains an integer N (1 ≤ N ≤ 10000) lines containing integers ai 
and bi, the absolute value of which does not exceed 10000, describing the 
statement of the i-th turtle.

## Output format
Print an integer M – the maximum number of turtles that can tell the truth.