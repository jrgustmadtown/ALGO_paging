import sys
PAGE=100

def possers(reqs, n):
    pos = [[] for _ in range(PAGE)]
    for i in range(n - 1, -1, -1):
        pos[reqs[i]].append(i)
    return pos

def paging(ksize, n, reqs):
    faults = 0
    k = []
    pos = possers(reqs, n)

    for i in range(n):
        page = reqs[i]
        pos[page].pop()

        if page in k:
            continue

        if len(k) < ksize:
            k.append(page)
        else:
            far = -1
            remove = -1
            for h, p in enumerate(k):
                if pos[p]:
                    next = pos[p][-1]
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
    



