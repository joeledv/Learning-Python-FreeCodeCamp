def adjacency_list_to_matrix(dict_adj):
    array2d = []
    empty_array = [0]*len(dict_adj)

    for element in dict_adj:
      array = empty_array.copy()
      for i in dict_adj[element]:
          array[i] = 1
      array2d.append(array)
      print(array)
    
    return array2d