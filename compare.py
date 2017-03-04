with open("c-code.txt") as f:
    c = f.read().splitlines()

with open("e-code.txt") as f:
    e = f.read().splitlines()

c = list(set(c))
e = list(set(e))

c = [x.lower().strip(' ') for x in c]
e = [x.lower().strip(' ') for x in e]
    
print "commercial:", len(c)
print "enterprise:", len(e)

d = set(e).intersection(c)
print "duplicates:", d, len(d)

with open("results.txt", "w") as f:
    f.write("\r\n".join(d))
