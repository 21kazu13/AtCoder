import time
n = 500
nx = n
ny = n

start = time.time()
l = [[x*y for x in range(nx)] for y in range(ny)]
print ("elapsed time for init of list:{0}".format(time.time()-start) + "[sec]")

start = time.time()
d = {}
for x in range(nx):
    for y in range(ny):
        d[(x,y)] = x*y
print ("elapsed time for init of dict:{0}".format(time.time()-start) + "[sec]")

start = time.time()
for x in range(nx):
    for y in range(ny):
        l[y][x] += 1
print ("elapsed time for update of list:{0}".format(time.time()-start) + "[sec]")

start = time.time()
for x in range(nx):
    for y in range(ny):
        d[(x,y)] += 1
print ("elapsed time for update of dict:{0}".format(time.time()-start) + "[sec]")

di = {}
for i in range(n):
    di[(i,i)] = i*i

start = time.time()
for x in range(nx):
    for y in range(ny):
        di[(x,y)] = di.get((x,y),0) + 1
print ("elapsed time for init/update of dict:{0}".format(time.time()-start) + "[sec]")
