def Crypt(string,key):
    import random
    random.seed(key)
    alpha = 2 * " AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890.;:,'?/|{}[]-=+_!@#$%^&*()<>`~"
    crypt = []
    lenalpha = int(len(alpha)/2)
    for p in range(len(string)):
        letterposition = alpha.index(string[p]) + lenalpha - int(lenalpha * random.random())
        crypt.append(alpha[letterposition])
    return ''.join(crypt)
