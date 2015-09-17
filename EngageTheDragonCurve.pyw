from turtle import *

def dragon(iterations):
    directions = [False]
    app = directions.append
    for counter in range(iterations):
        gen = [not(directions[digit]) for digit in reversed(range((2**(counter+1))-1))]
        app(False)
        for elements in gen:
            app(elements)
    return directions

def engage_the_dragon(depth,speed,size,distance,colora,colorb,anglea=90,angleb=90):
    draggy = Turtle()
    draggy.hideturtle()
    draggy.getscreen().delay(0)
    draggy.speed(speed)
    draggy.width(size)
    draggy.color(colora,colorb)
    turns = dragon(depth)
    for each_turn in turns:
        draggy.forward(distance)
        if each_turn:
            draggy.left(anglea)
        else:
            draggy.right(angleb)

def main(depth=20,speed=0,distance=1,size=0,colora='black',colorb='blue'):
    Screen()
    engage_the_dragon(depth,speed,size,distance,colora,colorb)

if __name__ == '__main__':
    main(15)
    input('Done!')

