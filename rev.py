def reverse_list(userlist):
    if len(userlist)==0:
        return none
    else:
        a = []
        list_size = len(userlist)-1
        for i in range(list_size, -1, -1):
            a.append(userlist[i])
            
        return a
"""
userlist = [1, 2, 3, 4, 5]
    
reverse_list(userlist)
print(reverse_list(userlist))
"""
