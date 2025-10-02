import sys
import heapq

def paging(ksize, n, reqs):
    faults=0
    k = set()
    heap = [] #max heap

    # find the earliest of each page
    nexts = []      #requests and their index
    for i, page in enumerate(reqs):
        nexts.append((page, i))
    nexts.sort() 
    pagesorts = []
    starts = []
    curr = None

    for i, (page, ind) in enumerate(nexts):
        if page != curr:
            pagesorts.append(page)
            starts.append(i)
            curr = page
    pointers = [0] * len(pagesorts) # ptr to prevent going through full request sequence
    
    #next use index (NUI) for any page - binary search
    def NUI(page, index):
        l = 0
        h = len(pagesorts)-1
        page_i = -1

        while l<=h:
            m = (l+h)//2
            if pagesorts[m] == page:
                page_i = m
                break
            elif pagesorts[m] < page:
                l=m+1
            else:
                h=m-1
        if page_i == -1:
            return float('inf')
        
        start = starts[page_i]
        ptr = pointers[page_i]

        while start + ptr < len(nexts) and nexts[start+ptr][0] == page:
            idx = nexts[start+ptr][1]
            if idx > index:
                pointers[page_i] = ptr
                return index
            ptr+=1
        return float('inf')
    
    #page requests
    for i in range(n):
        page = reqs[i]
        if page in k:
            heapq.heappush(heap, (-NUI(page, i), page))
            continue
        faults+=1

        if len(k) >= ksize:
            while heap:
                _, p = heapq.heappop(heap)
                if p in k:
                    k.remove(p)
                    break

        k.add(page)
        heapq.heappush(heap, (-NUI(page, i), page))

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
    



