def bubble_sort(list):
	for i in range(len(list)):
		for j in range(len(list)):
			if list[i] < list[j]:
				(list[i], list[j]) = (list[j], list[i])
	return list

a = [9, 2, 0, 4, 3, 5, 8, 7, 9, 10, 30, 78,100, 20, 39, 3, 44, 5, 6]
print bubble_sort(a)


 

