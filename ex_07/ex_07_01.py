fh = open('mbox-short.txt', 'rt')
print(fh)

for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())
