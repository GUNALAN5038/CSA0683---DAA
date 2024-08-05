def minimum_distance(text, word1, word2):
    words = text.split()
    min_distance = float('inf')
    last_pos_word1 = last_pos_word2 = -1
    
    for i, word in enumerate(words):
        if word == word1:
            last_pos_word1 = i
            if last_pos_word2 != -1:
                min_distance = min(min_distance, last_pos_word1 - last_pos_word2)
        elif word == word2:
            last_pos_word2 = i
            if last_pos_word1 != -1:
                min_distance = min(min_distance, last_pos_word2 - last_pos_word1)
    
    return min_distance if min_distance != float('inf') else -1
text = "the quick brown fox jumps over the lazy dog"
word1 = "quick"
word2 = "dog"
print(minimum_distance(text, word1, word2))  

text = "the quick brown fox quick"
word1 = "quick"
word2 = "fox"
print(minimum_distance(text, word1, word2))  
