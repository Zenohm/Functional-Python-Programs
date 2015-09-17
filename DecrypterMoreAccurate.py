def deCrypt(string):
    import encrypt, detectenglish, random
    dict = ''.join([p.replace('\n', ' ') for p in open('dictionary.txt', 'r')]).split()
    key = -1
    while True:
        key += 1
        random.seed(key)
        alpha = 2 * "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz .;:,'?/|{}[]-=+_1234567890!@#$%^&*()<>`~"
        crypt = []
        lenalpha = int(len(alpha)/2)
        for p in range(len(string)-1):
            letterposition = alpha.index(string[p]) + lenalpha - int(lenalpha * random.random())
            crypt.append(alpha[letterposition])
        current = ''.join(crypt)
        for word in dict:
            if '' + word + '' in current:
                print(word)
                if detectenglish.isEnglish(encrypt.Crypt(string, key, 0)) == True:
                    return encrypt.Crypt(string, key, 0)


x = input("Enter your message:")
deCrypt(x)
input("Operations Complete. Press Enter to Close Window...")
