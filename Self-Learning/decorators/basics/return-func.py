from random import choice
# We can return funcs from other funcs
def make_laugh_func():
    def get_laugh():
        l = choice(('HAHAHAH', 'lol', 'tehehe'))
        return l

    return get_laugh # returns the entire function

laugh = make_laugh_func()
print(laugh())



def make_laugh_func_2(person): #Example of closure
    def get_laugh():
        l = choice(('HAHAHAH', 'lol', 'tehehe'))
        return f'{l} {person}'

    return get_laugh # returns the entire function

laugh = make_laugh_func_2("Jose")
print(laugh())
