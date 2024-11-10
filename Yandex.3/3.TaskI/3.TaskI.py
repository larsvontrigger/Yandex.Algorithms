numofstudents= int(input())

#Making a tuple for every student
students_languages = []

#For every student input languages
for i in range(numofstudents):
    Mi = int(input())  
    languages = list()  
    for i in range(Mi):
        language = input().strip()  
        languages.append(language)
    students_languages.append(languages)

def langknowledge():
    alllangs = set(students_languages[0])  
    anylangs = set(students_languages[0])  
    
    for langs in students_languages[1:]:  
        alllangs &= set(langs)  
        anylangs |= set(langs)  
    
    print(len(alllangs))  
    for lang in alllangs:
        print(lang)
    
    print(len(anylangs))  
    for lang in anylangs:
        print(lang)

langknowledge()  


