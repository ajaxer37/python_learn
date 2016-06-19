def censor(text, word):
    tmp = text.split()
    strr = []
    for i in tmp:
        if word == i:
            jj = ""
            for j in i:
                jj += "*"
            i = jj
        strr.append(i)
    return ' '.join(strr)
    
input_strs = raw_input("Multi args by commar : ")
input_strs = input_strs.split(',')
print censor(input_strs[0],input_strs[1] )
