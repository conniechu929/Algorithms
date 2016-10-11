function insertion_sort(array) {
	for(var i = 0; i < array.length; i++){
		var current = array[i];
		for(var j = i; j > 0 && (array[j - 1] > current); j--){
			array[j] = array[j - 1];
			current = array[j];
		}
		array[j+1] = current;
	}
  return array;
}
