def reverse(text):
    print text
    rvsed_txt = list(text)
    print rvsed_txt
    if len(text) %2 == 0:
        for i in range(len(text)/2):
            rvsed_txt[i] = text[(len(text)-1-i)] 
            rvsed_txt[(len(text)-1-i)] = text[i] 
    elif len(text) %2 == 1:
        for i in range((len(text)+1)/2):
            rvsed_txt[i] = text[(len(text)-1-i)]
            rvsed_txt[(len(text)-1-i)] = text[i] 
    return ''.join(rvsed_txt)
        
print reverse(raw_input("Inputs: "))
