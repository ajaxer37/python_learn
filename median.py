def median(n):
    n.sort()
    if len(n) % 2 == 1:
        return n[(len(n)-1)/2]
    else:
        med = (n[len(n)/2 - 1] + n[len(n)/2])/2.0
        return med
        
print median([1,3,4,2,6])
print median([4,5,5,4])
