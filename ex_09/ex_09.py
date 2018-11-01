"""
텍스트 파일에 가장 많이 쓰여진 단어와 단어의 개수 찾기
"""

fname = input("Enter a filename: ")

if len(fname) < 1:
    fname = "clown.txt"

fhand = open(fname, 'rt')

di = dict()

for lin in fhand:
    lin = lin.rstrip()
    #print(lin)
    wds = lin.split()
    #print(wds)
    for wd in wds:
        # retrieve/create/update/ counter
        di[wd] = di.get(wd, 0) + 1
        #print(wd, di[wd])

#print(di)

# how to find most common word
largest = -1
theword = None
for key, value in di.items():
    #print(key, value)
    if value > largest:
        largest = value
        theword = key
print(theword, largest)