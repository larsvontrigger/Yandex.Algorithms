import os
with open('/Users/piratejet/Documents/GitHub/Y.Algoritms/Yandex.4/4.TaskJ/input.txt', 'r') as file:
    text = file.read()

#Main input
maininput = input()
numkeywords,registeridentifier,numidentifier = map(str,maininput.split())
numkeywords = int(numkeywords)

if registeridentifier == 'yes':
    registeridentifier = bool(True)
elif registeridentifier == 'no':
    registeridentifier = bool(False)

if numidentifier == 'yes':
    numidentifier = bool(True)
elif numidentifier == 'no':
    numidentifier = bool(False)

keywords = []
while len(keywords) < numkeywords:
    ip = str(input())
    keywords.append(ip)

#Work with keywords and input.txt
def signcleaner(text):
    
    #delete every sign exept number and letter
    if numidentifier:
        signs = '"{.,)(^%$£@!;*№/\|&?>:<}{_+=-}'
        for sign in signs:
            text = text.replace(sign," ")
    
    #delete every sign exept letter
    else:
        signs = '"{.,)(^%$£@!;*№/\|&?>:<}{_+=-}1234567890'
        for sign in signs:
            text = text.replace(sign," ")
    
    text = text.split()
    
    #delete keywords from text
    text = [word for word in text if word not in keywords]  
    
    return text

#Making dictionary for every word in txt file and count it with needed parametres
def signcounter(text):
    newtext = signcleaner(text)
    textdict = dict()
    
    #count every elem in dict like unique
    if registeridentifier:
        for sign in newtext:
            textdict[sign] = textdict.get(sign,0) + 1
        maxvalue = max(textdict.values())
    
    #count every elem in dict like .lower()
    else:
        for sign in newtext:
            textdict[sign.lower()] = textdict.get(sign.lower(),0) + 1
        maxvalue = max(textdict.values()) 
    
    #finding a key with the biggest value and break after first win
    for key,values in textdict.items():
        if values == maxvalue:
            print(key)
            break

signcounter(text)