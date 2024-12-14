import turtle
import time
import random

delay = 0.1

# dibuat 1966
# jadi ini adalah script yang sudah dibuat oleh orang lain 
# KALO PENGEN TAHU INI BUAT APA TINGGAL ARAHKAN KURSOR KE TULISANNYA
wn = turtle.Screen()
# screen ini untuk menampilkan layar di output
wn.title("GAME SNAKE BY RAFA KHADAFI")
wn.bgcolor("pink")
wn.setup(width=600, height=600)
wn.tracer(0)


# buat kepala ularnya
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = 'stop'

# buat kaki ularnya
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("white")
food.penup()
food.goto(0,100)

segments = []

def go_up():
    head.direction = "up"
def go_down():
    head.direction = "down"
def go_left():
    head.direction = "left"
def go_right():
    head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# keyboard
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")

while True:
    wn.update()

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor()>290 or head.ycor()<-290:


    if head.distance(food) < 20:
        # membuat makanan menjadi muncul secara random
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

    # memberi segments
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("blue")
    new_segment.penup()
    segments.append(new_segment)
    new_segment.goto(0,100)

    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)


    if len(segments) > 0 :
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)


    move()
    time.sleep(delay)
    # ini supaya menjadi pengulangan tanpa henti

wn.mainloop()

