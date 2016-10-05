def selection_sort(list):
	for i in range(len(list)-1):
		min = i
		for j in range(i+ 1, len(list)):
			if list[j] < list[min]:
				min = j
		(list[min], list[i]) = (list[i], list[min])
	return list

a = [9, 2, 0, 4, 3, 5, 8, 7, 9, 10, 30, 78,100, 20, 39, 3, 44, 5, 6]
print selection_sort(a)