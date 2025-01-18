x= [2,4,'a',6,'b',5.5,'c']
z=0.0
for i in range (len(x)):
    if isinstance(x[i], int):
        z=z+x[i]
    elif isinstance(x[i], float):
        z=z+x[i]
    else:

       print(f"this is not a number : {x[i]}") 
    
    
print(f"The sun is : {z}")
