# Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.


def count_cases (string) : 
    upper_case = 0
    lower_case = 0
    for index in range (0, len(string)) :
        if ('A' <= string [index] <= 'Z'):
            upper_case = upper_case + 1
        elif ('a' <= string [index] <= 'z'):
            lower_case = lower_case +1
    print (f'There’s {upper_case} upper cases and {lower_case} lower cases')
    return upper_case


def main () :
    string = 'I love Nation Sushi'
    count_cases (string)


main ()