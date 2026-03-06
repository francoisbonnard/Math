from turtle import  *
# shape("tree")
speed(0.5)

def snowflake(size, levels):
    if levels == 0:
        forward(size)
        return
    snowflake(size/3, levels-1)
    left(60)
    snowflake(size/3, levels-1)
    right(120)
    snowflake(size/3, levels-1)
    left(60)
    snowflake(size/3, levels-1)     
    

snowflake(200, 4)
mainloop()
