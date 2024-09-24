from pico2d import *
import math



open_canvas()

#fill here

grass = load_image('grass.png')
boy = load_image('character.png')

def draw_boy(x,y):
    clear_canvas_now()
    boy.draw_now(x,y)
    delay(0.01)

def run_top():
    print('TOP')
    for y in range(0,600 -1,10):
        draw_boy(0 +10,y)
    pass
def run_right():
    print('RIGHT')
    for x in range(0,800 -1,10):
        draw_boy(x,600-10)
    pass

def run_bottom():
    print('BOTTOM')
    for y in range(600,0 +1,-10):
        draw_boy(800 -10,y)
    pass
def run_left():
    print('LEFT')
    for x in range(800,0 +1,-10):
        draw_boy(x, 0 +10)
    pass

def run_rectangle():
    print('RECTANGLE')
    run_top()
    run_right()
    run_bottom()
    run_left()
    pass

def run_circle():
    print('CIRCLE')
    r, cx, cy = 300, 800//2, 600//2
    
    for d in range(0,360):
        x = r*math.cos(math.radians(d)) + cx
        y = r*math.sin(math.radians(d)) + cy
        draw_boy(x,y)

while True:
    run_rectangle()
    #run_circle()
    break

clear_canvas_now()

