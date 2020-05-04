#dictionary comprehension

names = ['Bruce', 'jack','roy']
superHero = ['Batman', 'Superman', 'SpiderMan']

#TODO:  we want {names: heroes}

myDict1 = {}
for name, hero in zip(names, superHero):
	myDict1[name] = hero

print(myDict1)

#comprehension
myDict2 = {n:h for n,h in zip(names, superHero)}
print(myDict2)

