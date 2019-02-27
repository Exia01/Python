#write a function called "combine_words" which accepts a single string and a prefix
#should return the word with the prefix together

def combine_words(word, **kwargs):
    if 'prefix' in kwargs:
        prefix = kwargs['prefix']
        return f'{prefix}{word}'
    elif 'suffix' in kwargs:
        suffix = kwargs['suffix']
        return f'{word}{suffix}'
    return word


#Test Cases
print(combine_words("child", prefix="man"))
print(combine_words("child", suffix="ish"))
print(combine_words("work", prefix="home"))