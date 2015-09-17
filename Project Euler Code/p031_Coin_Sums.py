def list_multiply(a,b):
    return [a[x]*b[x] for x in range(len(a))]


def redistribute(list_of_keys,list_of_values,inputted_number):
    for each_key in range(len(list_of_keys)):
        cut = inputted_number//list_of_keys[each_key]
        list_of_values[each_key] += cut
        inputted_number -= cut * list_of_keys[each_key]
    return dict(zip(list_of_keys,list_of_values))
    

    

values = [100,50,20,5,2,1]
number_of_coins = [1,1,2,1,2,1]
max_number_of_coins = [2,4,20,40,100,200]

