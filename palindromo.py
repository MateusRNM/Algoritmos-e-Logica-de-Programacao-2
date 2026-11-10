def palindromo(txt):
    l = 0
    r = len(txt)-1
    while l < r:
        if txt[l] != txt[r]:
            return False
        l += 1
        r -= 1
    return True

print(palindromo("arara"))
print(palindromo("aabc"))