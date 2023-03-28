import collections
f = open("real_output.txt","r")
print(dict(collections.Counter([ x for x in f.read().splitlines() ])))


f.close()
