def remove_duplicates(lis):
    tmp_lis = lis[:]
    rst_lis = []
    k = 0
    m = 0
    for i in tmp_lis:
        if lis.count(i) >= 1:
            rst_lis.append(i)
            n = tmp_lis.count(i)
            print "n: %d" % n
            for j in range(n):
                tmp_lis.remove(i)
            print "tmp_lis: "
            print tmp_lis
            print rst_lis
    print "final ..."
    print lis
    print tmp_lis
    print rst_lis
    return rst_lis
    
print remove_duplicates([88, 5, 7, 88, 93, 4])
         
