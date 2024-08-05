def is_palindrome(s):
    return s == s[::-1]

def partition(s):
    result = []
    
    def backtrack(start, path):
        if start == len(s):
            result.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            if is_palindrome(s[start:end]):
                path.append(s[start:end])
                backtrack(start + end - start, path)
                path.pop()
    
    backtrack(0, [])
    return result
s = "aab"
print(partition(s))   
