def lychrel(num):
    import sys
    for incr in range(0,50):
        num = num + int(str(num)[::-1])
        if num == int(str(num)[::-1]):
            print("Palindrome:",num,"Iterations:",incr)
            return True
    return False

lych = []
for a in range(1,1000001):
    if lychrel(a) == False:
        lych.append(a)

len(lych)
