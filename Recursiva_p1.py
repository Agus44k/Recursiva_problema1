import random

def min_max(arr, i, mi, ma):
    if i == len(arr):
        return mi, ma
    
    num = arr[i]
    if num % 3 == 0:
        if num < mi:
            mi = num
        if num > ma:
            ma = num
            
    return min_max(arr, i + 1, mi, ma)

n = int(input("Tamaño del arreglo: "))
arr = []

for _ in range(n):
    arr.append(random.randint(10, 9999))

print("Arreglo:", arr)


mi, ma = min_max(arr, 0, 9999, 0)

if ma == 0:
    print("No hay multiplos de 3")
else:
    promedio = (mi + ma) / 2
    print("Mínimo:", mi)
    print("Máximo:", ma)
    print("Promedio:", promedio)