names = ['Jose', 'John', 'Pepe the frog']
colors = ['Teal', 'Red', 'Purple']
index = 0

favorite = colors[0]  # teal 
secondary_favorite = [-3]  # Will stil pull teal

print('Pepe' in names)  #case sensitive -> will print false

if ('Teal' in colors):
    print('Nice color bruhh')

if names.__contains__('John'):
    print('True')

for color in colors:
    print(color)

while index < len(names):
    print(f'{index}: {names[index]}')
    index+=1