list = ['Jose', 'John', 'Pepe the frog']
colors = ['Teal', 'Red', 'Purple']

favorite = colors[0]  # teal 
secondary_favorite = [-3]  # Will stil pull teal

print('Pepe' in list)  #case sensitive -> will print false

if ('Teal' in colors):
    print('Nice color bruhh')

if list.__contains__('John'):
    print('True')