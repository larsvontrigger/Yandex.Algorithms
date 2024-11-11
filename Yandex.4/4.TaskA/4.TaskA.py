n = int(input())
synonyms = {}

# Loop through each pair of synonyms
for _ in range(n):
    word1, word2 = input().split()
    synonyms[word1] = word2  
    synonyms[word2] = word1  
    
query_word = input()

print(synonyms[query_word])
