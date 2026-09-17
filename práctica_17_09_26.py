

def insertion_sort(array):

    for j in range(1,len(array)):
      for i in range(1,len(array)):
          elemento = array[0] 
          if array[i] > elemento:
              array.insert(i,elemento)
              array.pop(0)

    return array


a =[4,5,6,8]

b= insertion_sort(a)
print(b)
