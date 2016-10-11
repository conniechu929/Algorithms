def insertion_sort(list):
	for i in range(1, len(list)):
		current = list[i]
		j = i
		while ((j > 0) and (list[j - 1] > current)):
			list[j] = list[j - 1]
			j = j - 1
		if current != i:
			list[j] = current
	return list

a = [5, 2, 6, 1, 3, 9]
print insertion_sort(a)