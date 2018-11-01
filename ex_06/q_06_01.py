words = "Connect Foundation"

if 'F' in words:
    words.lower()
    words[7] = '&' # 문자열은 상수, assignment 불가능!
else:
    print(words)

print(words)