def trip(up):
    try:
        import sys
        for a in range(1,up):
            for b in range(1,up):
                    c = (a**2+b**2)**.5
                    if a+b+c == 1000:
                        1/0
    except:
        print("Special Pythagorean Triplet Found!",int(a),int(b),int(c))
        print("Product:",int(a*b*c))

