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

def run_right():
    print('RIGHT')
    for x in range(0,800 -1,10):
        draw_boy(x,600-10)

def run_bottom():
    print('BOTTOM')
    for y in range(600,0 +1,-10):
        draw_boy(800 -10,y)
        
def run_left():
    print('LEFT')
    for x in range(800,0 +1,-10):
        draw_boy(x, 0 +10)

def run_rectangle():
    print('RECTANGLE')
    run_top()
    run_right()
    run_bottom()
    run_left()

def run_circle():
    print('CIRCLE')
    r, cx, cy = 300, 800//2, 600//2
    
    for d in range(0,360):
        x = r*math.cos(math.radians(d)) + cx
        y = r*math.sin(math.radians(d)) + cy
        draw_boy(x,y)
        
def run_right_triangle():
    print('run_right_triangle')
    for x in range(0,800 -1,10):
        draw_boy(x, 90)
    pass

def run_high_triangle():
    print('run_high_triangle')
    for d in range(0,100):
        x = 800 - (800//2)//100*d
        y = 0 + 600//100*d
        draw_boy(x,y -10)
    pass

def run_left_triangle():
    print('run_left_triangle')
    for d in range(0,100):
        x = 800//2 - (800//2)//100*d
        y = 600 - 600//100*d
        draw_boy(x,y +10)
    pass


def run_triangle():
    print('TRICANGLE')
    run_right_triangle()
    run_high_triangle()
    run_left_triangle()
    pass

while True:
    run_rectangle()
    run_circle()
    run_triangle()
    break

clear_canvas_now()

