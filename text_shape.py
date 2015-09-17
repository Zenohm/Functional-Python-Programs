def text_shape(text='test',shape=2,maxim=7):
    text = str(text)
    a = list(range(1,maxim)) + [maxim] + list(range(1,maxim))[::-1]
    b = [' ' * shape * (maxim - i) + text * i for i in a]
    for line in b:
        print(line)
