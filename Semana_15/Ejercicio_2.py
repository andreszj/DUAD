# Modifica el bubble_sort para que funcione de derecha a izquierda, ordenando los números menores primero (como en la imagen de abajo).

def bubble_sort (list_to_sort):
    
    for outer_index in range (0, len(list_to_sort)-1):
        changes_done = False
        for index in range (len (list_to_sort)-1-outer_index,0,-1):
            
            current_data = list_to_sort[index]
            prev_data = list_to_sort[index-1]
            print (f'Iteration {outer_index} , {len (list_to_sort)-index}')
            if current_data < prev_data:
                list_to_sort[index] = prev_data
                list_to_sort[index-1] = current_data
                changes_done = True
                print (f'Replacing: {prev_data} <-> {current_data}')
        if not changes_done:
            print ('Stopping iteration, no more changes to make')
            break
    new_list = list_to_sort
    return new_list


# list_to_sort = [12,-10,39,5,10,0]
# list_to_sort = [1,2,0,7,9,19]
list_to_sort = [3,2,0,7,9,1]

print (f'Sorted List: {bubble_sort(list_to_sort)}')
