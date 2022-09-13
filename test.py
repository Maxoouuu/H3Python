tab = []
a = int(input("Combien de valeurs ? "))
for i in range(a):
  num = int(input("Entrez votre nombre : "))
  tab.append(num)
listSum = sum(tab)
print("la somme des valeurs de la liste est : " , listSum)