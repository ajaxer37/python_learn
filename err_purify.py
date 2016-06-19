def purify(num):
    for i in num:
        print i
        if i % 2 == 1:
            print i
            num.remove(i)
            print num
    return num
 
aa = [4,5,5,4,7,9]
purify(aa)

print aa

