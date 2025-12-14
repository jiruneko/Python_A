# l = ['Good morning', 'Good morning', 'Good night']

# for i in l:
#     print(i)

def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

for g in greeting():
    print(g)