numofwords = int(input())
dictwords = {}
sentence = {}
counter = 0

#functiont that checking for accent position and making dictionary
def uppercounter(w, a, dictt, neg):
    for item in range(len(w)):
        if w[item].isupper():
            a.append(item)
    if len(a) == 1:
        word_lower = w.lower()
        if word_lower in dictt:
            dictt[word_lower].append(a)  
        else:
            dictt[word_lower] = [a]  
    else:
        neg += 1
    return neg

#input words
for _ in range(numofwords):
    word = str(input())
    ans = []
    uppercounter(word, ans, dictwords, counter)

#input sentence
sentenceinput = list(input().split())
for item in sentenceinput:
    sen = []
    counter = uppercounter(item, sen, sentence, counter)

print(dictwords)
print(sentence)
#looking for right accents in our dictionaries
for key, value in dictwords.items():
    for key1, value1 in sentence.items():
        for item in value1:
            if key.lower() == key1.lower():
                if item not in value: 
                    counter += 1

print(counter)




