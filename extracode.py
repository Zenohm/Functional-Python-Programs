def delta_list(list):
    return [list[item+1]-list[item] for item in range(len(list)-1)]


def checkchange(list):
    while len(list)!=1:
        list = delta_list(list)
    return list


def tupper(N):
    import sys
    H = 17
    W = 106
    for y in range(N+H-1, N-1, -1):
        for x in range(W):
            if 0.5 < ((y//H) // (2**(H*x + y%H))) % 2: sys.stdout.write('*')
            else: sys.stdout.write(' ')
        sys.stdout.write('\n')


prob = {"Albert":{'May':[15,16,19],'June':[17,18],'July':[14,16],'Aug':[14,15,17]},"Bernard":{14:['July','Aug'],15:['May','Aug'],16:['May','July'],17:['June','Aug'],18:['June'],19:['May']}}
def dprint(inp,delay=0):
    from sys import stdout
    from time import sleep
    stdout.write("\r{}".format(inp))
    stdout.flush()
    sleep(delay)
    stdout.write("\r\r\n") # clean up
    stdout.flush()


def graph(formula, x_range=range(-10,11)):
    import numpy as np
    import matplotlib.pyplot as plt
    x = np.arange(min(x_range),max(x_range),.001)
    y = formula(x)  # <- note now we're calling the function 'formula' with x
    plt.plot(x, y)  
    plt.show()  

def my_formula(x):
    return x**3+2*x-4

graph(my_formula, range(-10, 11))


def plotdata(datay,x=np.arange(1,10,.001),style='bo'):
    import matplotlib.pyplot as plt
    plt.plot(x, datay, style)
    plt.show()





4858450636189713423582095962494202044581400587983244549483093085061934704708809928450644769865524364849997247024915119110411605739177407856919754326571855442057210445735883681829823754139634338225199452191651284348332905131193199953502413758765239264874613394906870130562295813219481113685339535565290850023875092856892694555974281546386510730049106723058933586052544096664351265349363643957125565695936815184334857605266940161251266951421550539554519153785457525756590740540157929001765967965480064427829131488548259914721248506352686630476300
