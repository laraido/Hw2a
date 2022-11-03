def sort_dictionary(userdict):

	out_list = []
	age_list = []
	for k,v in userdict.items():
		out_list.append((k,v[0]))
		age_list.append(v[1])
		
	output = [x for _, x in sorted(zip(age_list, out_list))]
	print(output)
	
	return;
	
#userdict = {'Jose': (4094456123, 27), 'Johnny': (5102341234, 24), 'Ava': (1231231234, 23)}
#print('Original List: ')
#print(userdict)
#print('New Sorted List: ') 
#sort_dictionary(userdict)
