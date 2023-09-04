# yield from

def gen1():
    yield 1
    yield 2
    yield 3
    
def gen2(gen01, gen02):
    yield from gen01()
    yield 4
    yield 5
    yield 6
    yield from gen02()
    
def gen3():
    yield 7
    yield 8
    yield 9
    
generator = gen2(gen1, gen3)
for i in generator:
    print(i) 
    