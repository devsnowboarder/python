generatorsobj = (i**i for i in range(1, 5))
print(generatorobj) # generator object
print(next(generatorobj)) # 1