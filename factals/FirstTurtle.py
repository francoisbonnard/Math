from turtle import  *
# shape("tree")
speed(0.5)

def tree(size, levels, angle):
    if levels == 0:
        color("green")
        dot(size)
        return
    forward(size)
    right(angle)
    tree(size*0.8, levels-1, angle)
    left(angle*2)
    tree(size*0.8, levels-1, angle)
    right(angle)
    backward(size)

def tree2(size, levels, angle):
    if levels == 0:
        color("green")
        dot(size)
        return
    forward(size)
    right(angle)
    tree(size*0.8, levels-1, angle)
    backward(size)
    left(angle*2)
    tree(size*0.8, levels-1, angle)


forward(200)
left(90)
tree(70, 5, 30)
left(90)
forward(400)
right(90)
tree2(70, 5, 30)

mainloop()
