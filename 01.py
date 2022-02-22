def search(list,n): 
     
    for i in range(len(list)): 
        if list[i] == n: 
            return True 
    return False  
list = ['1', '2', 'kle', '4','MCA', '6']  
n = input("Enter the key to search")  
if search(list,n): 
    print("Found") 
else: 
    print("Not Found") 
