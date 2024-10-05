x = input()
a = input()
b = input()
c = input()

#Making a new lists
new_number = list(x)
old_number1 = list(a)
old_number2 = list(b)
old_number3 = list(c)

#Making lists for sorted data
filter_new_number = fnb = []
filter_old_number1 = on1 = []
filter_old_number2 =  on2 =[]
filter_old_number3 = on3 = []

#Аilter data from unnecessary characters
for x in new_number:
    if x.isdigit():
        filter_new_number.append(x)
for a in old_number1:
    if a.isdigit():
        filter_old_number1.append(a)
for b in old_number2:
    if b.isdigit():
        filter_old_number2.append(b)
for c in old_number3:
    if c.isdigit():
        filter_old_number3.append(c)

#Create a function for quantitative sorting of an array
def sort_lenght(function):
    if len(function) == 11:
        function.pop(0)
        function.insert(0,8)
    elif len(function) == 10:
        function.insert(0,8)
    elif len(function) == 7:
        function.insert(0,8)
        function.insert(1,4)
        function.insert(2,9)
        function.insert(3,5)
    return(function)
sort_lenght(fnb)
sort_lenght(on1)
sort_lenght(on2)
sort_lenght(on3)

#Comparisons of prepared sorted arrays
if fnb == on1:
    print("YES")
else:
    print("NO")

if fnb == on2:
    print("YES")
else:
    print("NO")

if fnb == on3:
    print("YES")
else:
    print("NO")
