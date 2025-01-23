x={'first': [1, 2, 3], 'sucond': 'me', 'third': 50.5, 'forth': 4, 'fifth': [4, 5, 6], 'sixth': 6}
values=[]
keys=[]
k=0
for i in x.values() :
    values.append(i)

for i in x :
    keys.append(i)

for j in range(5,-1,-1):
    #  print(values[j])
    #  print("")
    #  print(keys[k])
     x[keys[k]]=values[j]
     k+=1
    
print("")
print(x)
print("")