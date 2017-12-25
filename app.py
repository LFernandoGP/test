print("Docker")

lista = list(range(100))
output = []

for x in lista:
    if x%2==0:
        output.append(x)

print("Valor {}".format(output))

output.sort()
