def anti_vowel(text):
    #consonant = list(text)
    consonant = ""
    for i in text:
        for j in ["a","e","i","o","u","A","E","I","O","U"]:
            if i == j:
                break
        else:
            consonant += i
                #consonant.remove(consonant[i])
    return consonant
    
print anti_vowel(raw_input("aaaa ... "))

## add changes for git
