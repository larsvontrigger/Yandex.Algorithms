# Alley
In a park in the city of Pittsburgh there is a wonderful alley consisting of N trees planted in 
a row, each of K varieties. Due to the fact that Pittsburgh is hosting the Byteland Open 
Programming Championship, it was decided to build a huge arena for the competition. So, 
according to this plan, the entire alley was to be cut down. However, the Ministry of Trees and 
Shrubs opposed this decision and demanded that some of the trees be left alone. According to 
the new construction plan, all trees that will not be cut down must form one continuous 
segment, which is a subsegment of the original one. At least one of each of the K tree species 
must be preserved. Your task is to find a segment of the shortest length that satisfies the 
specified restrictions.

## Input format
The first line of the input file contains two numbers N and K (1 ≤ N, K ≤ 250000). The second 
line of the input file contains N numbers (separated by spaces), the i-th number of the second 
line specifies the color of the i-th tree from the left in the alley. It is guaranteed that 
there is at least one tree of each color

## Output format
In the output file, output two numbers, the coordinates of the left and right ends of the 
segment of minimum length that satisfies the condition. If there are several optimal answers, 
output any one.