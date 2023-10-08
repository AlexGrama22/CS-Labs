import random
def apply_permutation(original, permutation):
    return ''.join(original[i-1] for i in permutation)

def left_shift(data, shifts):
    return data[shifts:] + data[:shifts]

PC1 = [
    57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4
]

PC2 = [
    14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4,
    26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32
]

initial_key = bin(random.getrandbits(64))[2:].zfill(64)
print("Cheia inițială de 64 de biți: ", initial_key)

key_after_pc1 = apply_permutation(initial_key, PC1)
print("Cheia după aplicarea permutării PC-1 (56 de biți): ", key_after_pc1,"\n")

print("Împărțim cheia de 56 de biți în două jumătăți de câte 28 de biți fiecare:")
C0 = key_after_pc1[:28]
D0 = key_after_pc1[28:]
print("C0: ", C0)
print("D0: ", D0)

i = 1
rotations = 1
print(f"\nRunda {i} cu {rotations} rotații la stânga:")

Ci = left_shift(C0, rotations)
Di = left_shift(D0, rotations)
print("Ci: ", Ci)
print("Di: ", Di)

combined_key = Ci + Di
print("\nCheia combinată de 56 de biți după rotație: ", combined_key)

key_after_pc2 = apply_permutation(combined_key, PC2)
print("Cheia de rundă Ki pentru runda", i, "este:", key_after_pc2)
