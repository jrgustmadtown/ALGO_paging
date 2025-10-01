import sys

def cache(reqs, page, off):
    i=0
    for i in range(len(reqs)):
        if reqs[i] == page:
            return (page, i+off)
        else:
            i+=1


def paging(ksize, n, reqs):
    faults = 0
    i=0 #index of page
    k = []

    if len(k) < k:
        k.append(cache(reqs[i+1:], reqs[i], i))
        faults+=1
    else:
        if reqs[i] not in k:
            indices = list(map(lambda x: x[1], k))
            far = indices.index(max(indices))
            k[far] = cache(reqs[i+1:], reqs[i], i)
                        
            faults+=1
        else:
            i+=1
        

    return faults

inputy = sys.stdin.read().splitlines()
t = int(inputy[0])
index = 0
outputy = []

for _ in range(t):
    index+=1
    ksize = int(inputy[index])
    k = [0 for _ in range(ksize)]
    index+=1
    n = int(inputy[index])
    index+=1
    reqs = inputy[index]
    outputy.append(paging(ksize, n, reqs))

for _ in outputy:
    print(_)
    



