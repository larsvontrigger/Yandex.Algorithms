# Air conditioners
When implementing the Smart School project, it was decided to install a new 
generation air conditioner for automatic cooling and ventilation in each 
classroom of the selected school. According to the project, only one air 
conditioner should be installed in each classroom, and the capacity of the 
air conditioner should be sufficient for the size of the class. The larger 
the class, the more powerful the air conditioner should be.

All classes in the school are numbered sequentially from 1 to n. It is 
known that for each class with number i, exactly one air conditioner is 
required, the capacity of which is greater than or equal to ai watts.

The school administration was provided with a list of m different models of 
air conditioners that can be purchased. For each air conditioner model, its 
capacity and cost are known. It is required to write a program that will 
determine the minimum total cost of air conditioners that can be used to 
equip all the classes in the school.

## Input format
The first line of the input file contains one integer n (1 ≤ n ≤ 50,000) 
the number of classes in the school.

The second line contains n integers ai (1 ≤ ai ≤ 1000) — the minimum power 
of the air conditioner in watts that can be installed in the class with the 
number i.

The third line contains one integer m (1 ≤ m ≤ 50,000) — the number of 
proposed air conditioner models.

Next, each of the m lines contains a pair of integers bj and cj (1 ≤ bj ≤ 
1000, 1 ≤ cj ≤ 1000) — the power in watts of the j-th air conditioner model 
and its price in rubles, respectively.

## Output format
The output file must contain one number — the minimum total cost of air 
conditioners in rubles. It is guaranteed that at least one correct choice 
of air conditioners exists, and a suitable air conditioner can be installed 
in all classes