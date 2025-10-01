import sys

def paging(ksize, n, reqs):
    faults = 0
    k = []

    for i in range(n):
        page = reqs[i]

        if page in k:
            continue

        if len(k) < ksize:
            k.append(page)
        else:
            far = -1
            remove = -1
            follow = reqs[i+1:]
            for h, p in enumerate(k):
                if p in follow:
                    next = follow.index(p)
                else:
                    next = float('inf')
                if next > far:
                    far = next
                    remove = h
            k[remove] = page
            
        faults+=1

    return faults

inputy = sys.stdin.read().splitlines()
t = int(inputy[0])
index = 1
outputy = []

for _ in range(t):
    ksize = int(inputy[index])
    index+=1
    n = int(inputy[index])
    index+=1
    reqs = list(map(int, inputy[index].split()))
    index+=1
    outputy.append(paging(ksize, n, list(reqs)))

for _ in outputy:
    print(_)
    



