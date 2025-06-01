# Analice el algoritmo de bubble_sort usando la Big O Notation.

def bubble_sort (list_to_sort): # O(n^2)
    
    for outer_index in range (0, len(list_to_sort)-1):  # O(n)
        changes_done = False    # O(1)
        for index in range (0, len (list_to_sort)-1-outer_index):   # O(n^2)
            
            current_data = list_to_sort[index]  # O(1)
            next_data = list_to_sort[index+1]   # O(1)
            print (f'Iteration {outer_index} , {index}')    # O(1)
            if current_data > next_data:    # O(1)
                list_to_sort[index] = next_data     # O(1)
                list_to_sort[index+1] = current_data    # O(1)
                changes_done = True     # O(1)
                print (f'Replacing: {next_data} <-> {current_data}')       # O(1)
        if not changes_done:    # O(1)
            print ('Stopping iteration, no more changes to make')   # O(1)
            break   # O(1)
    new_list = list_to_sort     # O(1)
    return new_list     # O(1)


# list_to_sort = [12,-10,39,5,10,0]
list_to_sort = [1,2,0,7,9,19]   # O(1)

print (f'Sorted List: {bubble_sort(list_to_sort)}') # O(n^2)
