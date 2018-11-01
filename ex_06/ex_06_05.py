str = 'X-DSPM-Confidence: 0.8475'

ipos = str.find(':')
print(ipos)

piece = str[ipos+2:]
print(piece, type(piece)) # 0.8475

value = float(piece)
print(value, type(value))