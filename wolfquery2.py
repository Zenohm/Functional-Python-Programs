def wolfquery(input):
    from urllib.request import urlopen
    return urlopen("http://api.wolframalpha.com/v2/query?appid=R33RAT-7QTK4AL8LL&input="+str(input))

