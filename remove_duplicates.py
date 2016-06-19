def remove_duplicates22(lis):
    tmp_lis = lis[:]
    rst_lis = []
    i = 0
    lst_len = len(tmp_lis)
    print lst_len
    while i < lst_len:
        j=1
        while (i+j) < lst_len: 
            if tmp_lis[i] == tmp_lis[i+j]:
                del tmp_lis[i+j]
                lst_len -= 1
            else:
                j+=1
            print j
            print lst_len
            print "tmp_lis:"; print tmp_lis
        i+=1

    print "final ..."
    print lis
    return tmp_lis

def remove_duplicates(n):
    newlist = []
    for item in n:
        while newlist.count(item) == 0:
            newlist.append(item)
    return newlist
    
print remove_duplicates([88, 5, 88, 7, 88, 93, 4])
