fname = input("Enter a filename: ")

if len(fname) < 1:
    fname = "clown.txt"

fhand = open(fname, 'rt')

di = dict()

for lin in fhand:
    lin = lin.rstrip()
    wds = lin.split()
    for wd in wds:
        # retrieve/create/update/ counter
        di[wd] = di.get(wd, 0) + 1

tmp = list()

for k, v in di.items():
    newt = v, k
    tmp.append(newt)

tmp = sorted(tmp, reverse=True)[:5]

for v, k in tmp[:5]:
    print(v,k)