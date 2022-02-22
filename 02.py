def insert(list,n):  
    index = len(list) 
    for i in range(len(list)): 
        if list[i] > n: 
            index = i 
            break  
    if index == len(list): 
        list = list[:index] + [n] 
    else: 
        list = list[:index] + [n] + list[index:] 
    return list  
list = [3 , 12 , 18 , 24 , 70 , 100] 
n = int(input("Enter a number to insert"))  
print(insert(list,n)) 
