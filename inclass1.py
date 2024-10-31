phs1 = str(input('What phrase would you like to reverse? '))
rng = len(phs1)
phs2 = ''
for x in range (0,rng):
        phs2 = phs2 + phs1[-(x+1)]
print(phs2)
