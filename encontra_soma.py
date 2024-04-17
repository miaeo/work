def encontra_soma(numeros, n):
    for i in range(len(numeros)):
        for j in range(i + 1, len(numeros)):
            if (numeros[i] + numeros[j] >= n and numeros[i] + numeros[j] < n + 0.01):
                print(f"Soma encontrada: {numeros[i]} + {numeros[j]} = {numeros[i] + numeros[j]:.2f}")

n = 90.49;
numeros = [
104.1, 43.3, 19.95, 90, 0.48, 42.23, 89, 1.48, 40.72, 72.4, 44.9, 88.23, 47.25, 45.9, 40.72, 49.74, 89.9, 44.9, 19.95, 89.9, 69.21, 69.81, 44.58, 53.54, 42, 41.61, 43.24, 36.6, 49, 30.85, 176.72, 93.9, 72.33, 44.88, 39.9, 44.14, 64.64, 53.69
]

encontra_soma(numeros, n)
