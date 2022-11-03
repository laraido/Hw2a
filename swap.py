def swap_list(userlist):
	if len(userlist)%2 == 0:
		get = userlist[int(len(userlist)/2)-1], userlist[-1]
		userlist[-1], userlist[int(len(userlist)/2)-1] = get
		return userlist
	else:
		get = userlist[int(len(userlist)/2)], userlist[-1]
		userlist[-1], userlist[int(len(userlist)/2)] = get
		return userlist
		
#userlist = [3]
#print(swap_list(userlist))
