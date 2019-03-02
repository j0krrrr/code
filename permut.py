def permut(string):
        if (len(string)==1):
		return [string]
	perm_list=[]
	for i,a in enumerate(string):
		remaining_elements= string[:i]+string[i+1:]
                remaining_elements=[x for x in remaining_elements]
		z=permut(remaining_elements)
		for t in z:
			perm_list.append([a]+t)
	return perm_list
print(permut('abcd'))
