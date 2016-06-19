def count(sequence,item):
    cnt = 0
    for i in sequence:
        if i == item:
            cnt += 1
    return cnt
    
input_strings = raw_input("Lists and pattern : ").split(' ')
for ii in input_strings:
    print ii
    
print count(input_strings[0],input_strings[1])

