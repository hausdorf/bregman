
#!/usr/bin/env python
import random
import sys

max = int(sys.argv[1])
d = int(sys.argv[2])
size = int(sys.argv[3])
filename = sys.argv[4]
f = open(filename,"w")

f.write(str(d) + ','+str(size) + '\n')


for j in range(0,size):
   for i in range(0,d):
      value = random.randint(1,max)
      coord = float(value)/float(max)
      f.write(str(coord))
      if i < d -1:
         f.write(',')
   if j < size - 1:
      f.write('\n')

f.close()