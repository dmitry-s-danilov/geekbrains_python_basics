from problem_7_lib import Complex

# set list of complex numbers
z0 = [(1, 0), (0, 1), (1, 1)]

# set operations
f = lambda z: (z,
               z + z, z + z + z, z + z + z + z,
               z * z, z * z * z, z * z * z * z)

# apply operations to self-made class
z1 = [Complex(*_) for _ in z0]
z1 = [f(_) for _ in z1]

# apply operations to built-in class
z2 = [complex(*_) for _ in z0]
z2 = [f(_) for _ in z2]

# compare results
c = all([z1[i][j].real == z2[i][j].real and z1[i][j].imag == z2[i][j].imag
         for i in range(len(z1)) for j in range(len(z1[i]))])

# print
print(*['; '.join(map(str, _)) for _ in z1], sep='\n')
print()
print(*['; '.join(map(str, _)) for _ in z2], sep='\n')
print()
print(f'check: {c}')
