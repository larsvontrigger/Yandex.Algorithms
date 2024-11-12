with open('/Users/piratejet/Documents/GitHub/Y.Algoritms/Yandex.4/4.TaskB/input.txt', 'r') as file:
    text = file.read()

words = text.split()
word_count = {}
result = []

for word in words:
    result.append(str(word_count.get(word, 0)))  
    word_count[word] = word_count.get(word, 0) + 1 

print(" ".join(result)) 
