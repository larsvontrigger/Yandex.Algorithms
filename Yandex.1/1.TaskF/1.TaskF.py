x_1,y_1 = int(input()),int(input())
x_2,y_2 = int(input()),int(input())

#1 case
x_3 = x_1 + x_2
y_3 = max(y_1,y_2)
s_3 = x_3 * y_3


#3 case
x_5 = x_1 + y_2
y_5 = max(x_2,y_1)
s_5 = x_5 * y_5


#5 case
x_7 = x_2 + y_1
y_7 = max(x_1,y_2)
s_7 = x_7 * y_7

#6 case
x_8 = y_1 + y_2
y_8 = max(x_1,x_2)
s_8 = x_8 * y_8

min = min(s_3,s_5,s_7,s_8)

if min == s_3:
    print(x_3,y_3,' ',y_3,x_3)

if min == s_5:
    print(x_5,y_5,' ',y_5,x_5)

if min == s_7:
    print(x_7,y_7,' ',y_7,x_7)

if min == s_8:
    print(x_8,y_8,' ',y_8,x_8)
