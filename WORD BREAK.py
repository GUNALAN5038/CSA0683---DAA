def word_break(s, word_dict):
    def backtrack(start, path):
        if start == len(s):
            result.append(" ".join(path))
            return
        for end in range(start + 1, len(s) + 1):
            if s[start:end] in word_dict:
                path.append(s[start:end])
                backtrack(end, path)
                path.pop()
    
    result = []
    backtrack(0, [])
    return result
s = "catsanddog"
word_dict = {"cat", "cats", "and", "sand", "dog"}
print(word_break(s, word_dict))  
