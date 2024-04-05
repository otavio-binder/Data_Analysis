lista  = {"12": "BAH", "SEX" : "13","viado" : "14"}
print(lista["12"])


va = str(input("Digita o codigo do municipio: "))
ans = list(va)
va2 = []
#print(lista["12"])
for i in range(6):
    va2.append(va[i])
cd = "".join(va2)      
print(cd)