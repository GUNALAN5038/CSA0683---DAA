def restore_ip_addresses(s):
    def backtrack(start, path):
        if start == len(s) and len(path) == 4:
            result.append(".".join(path))
            return
        if len(path) > 4:
            return
        for end in range(start + 1, min(start + 4, len(s) + 1)):
            part = s[start:end]
            if int(part) > 255 or (len(part) > 1 and part[0] == '0'):
                continue
            path.append(part)
            backtrack(end, path)
            path.pop()
    
    result = []
    backtrack(0, [])
    return result
s = "25525511135"
print(restore_ip_addresses(s)) 
