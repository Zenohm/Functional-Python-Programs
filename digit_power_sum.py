def digit_power_sum(number):
    import math
    if number in range(9):
        return True
    if not math.log10(number)%1:
        return False
    storage, sum = str(number), 0
    for char in storage:
        sum += int(char)
    storage = (math.log(number)/math.log(sum))%1
    if storage:
        return False
    return True

