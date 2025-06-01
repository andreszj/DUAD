# Crea un bubble_sort por tu cuenta sin revisar el código de la lección.

def bubble_sort (list_to_sort):
    
    for outer_index in range (0, len(list_to_sort)-1):
        changes_done = False
        for index in range (0, len (list_to_sort)-1-outer_index):
            
            current_data = list_to_sort[index]
            next_data = list_to_sort[index+1]
            print (f'Iteration {outer_index} , {index}')
            if current_data > next_data:
                list_to_sort[index] = next_data
                list_to_sort[index+1] = current_data
                changes_done = True
                print (f'Replacing: {next_data} <-> {current_data}')
        if not changes_done:
            print ('Stopping iteration, no more changes to make')
            break
    new_list = list_to_sort
    return new_list


# list_to_sort = [12,-10,39,5,10,0]
list_to_sort = [1,2,0,7,9,19]

print (f'Sorted List: {bubble_sort(list_to_sort)}')
