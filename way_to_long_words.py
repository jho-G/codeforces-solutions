def way_to_long_words(word):    
    
    if len(word)>10:
        return word[0] + str(len(word)-2) + word[-1]
    else:
        return word