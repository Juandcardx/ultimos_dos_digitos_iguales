# Los dos ultimos digitos son iguales?

print("----------------------------------------------------")
print("---------Digite un numero de minimo 2 cifras--------")
print("----------------------------------------------------")

#input
n= int(input("Digite el valor de n: "))

#procesing

de= n//10%10
mod= n%10
x = de
y = mod

#output
if n<11:
    print(" no cumple con la condicion")
else:
 if x == y:

    print(" sus dos ultimos digitos son iguales")

 else:

    print(" sus dos ultimos digitos son diferentes")