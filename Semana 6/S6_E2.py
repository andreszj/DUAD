#concepto de scope

global_variable = [2 , 3 , 4]

def first_function () :
    local_variable = 'hola'
    global_variable.pop(1)
    print (global_variable)

first_function ()
#print (local_variable)   #'local_variable' is not defined