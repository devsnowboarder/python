scores =[]

entry=("100","Mike")
scores.append(entry)
entry=("200","John")
scores.append(entry)
scores.sort()
scores.reverse()

for entry in scores:
    score, name = entry
    print( name, "\t", score)