def misterio(cadena):
 v = {'a', 'e', 'i', 'o', 'u'}
 r = 0
 for c in cadena:
 if c not in v:
 r += 1
 return r
print(misterio('misterio'))

