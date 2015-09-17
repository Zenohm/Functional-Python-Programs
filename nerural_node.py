def weighted_average(inputs,weights=[]):
    weighted_list = []
    if len(weights) or sum(weights) > 1:
        for each_weight in range(len(weights)):
            weights[each_weight] /= sum(weights)
    if type(inputs[0])==list:
        if len(inputs[0]) == 2:
            for each_input,the_weight in inputs:
                weighted_list.append(each_input * the_weight)
            return sum(weighted_list)/int(len(weighted_list))
        else:
            return 'Fuck you.'
    else:
        if len(inputs) == len(weights):
            for each_input,the_weight in zip(inputs,weights):
                weighted_list.append(each_input * the_weight)
            return sum(weighted_list)/int(len(weighted_list))
        else:
            return 'Fuck you. Lists are different sizes.'
        
