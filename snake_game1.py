import turtle
import time
import random

delay = 0.1

#SCore
score = 0
high_score = 0

# Setup the screen
window = turtle.Screen()
window.title("snake Game by Jan")
window.bgcolor("black")
window.setup(width=800, height=800)
window.tracer(0) # Turns off animation on the screen / screen updates

# Snake head
head = turtle.Turtle()
head.speed(0) # animation speed of the turtle module, not the snake (fastest speed is 0)
head.shape("square")
head.color("green")
head.penup() # Turtles draw lines, put penup so it does not draw anything
head.goto(0,0)
head.direction = "stop" # snake head starts still at 0,0

# Snake food
food = turtle.Turtle()
food.speed(0) # animation speed of the turtle module, not the food (fastest speed is 0)
food.shape("circle")
food.color("white")
food.penup() # Turtles draw lines, put penup so it does not draw anything
food.goto(0,100)


segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0, 360)
pen.write("Score: 0 Highscore: 0", align="center", font=("Courier", 24, "normal"))

# Functions

def go_up(): # when "wasd" keys are pressed it changes direction here
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move(): # function for moving the turtle 20 px each direction
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

# Keyboard bindings for when playing the game, here I will be using the "wasd" to move the snake
window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")

# Main game loop
while True:
    window.update() # updates the screen

    # Check for a collision with the screen border
    if head.xcor()>390 or head.xcor()<-390 or head.ycor()>390 or head.ycor()<-390:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000) # hides the segments off screen

        # Clear the segments list
        segments.clear()

        # Reset score
        score = 0

        # Reset delay
        delay = 0.1

        # Update score display
        pen.clear()
        pen.write("Score: {} Highscore: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Check for a collision with the food

    if head.distance(food) < 20: #measure distance between head and food (the 2 turtles), < 20 because each basic turtle shape is 20px wide by 20 px tall. So if distance is <20 they have collided
        # Move the food to a random spot
        x = random.randint(-390, 390) # 390 since my screen width is 800, half from center is 400 but -10 so that it does not go beyond the screen
        y = random.randint(-390, 390)
        food.goto(x,y)

        # Add a segment for snake when the snake touches the food
        new_segment = turtle.Turtle()
        new_segment.speed(0) # Animation speed not snake movement
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {} Highscore: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1): # length of segments is 10, lists start from 0 to 9, here in reverse so 9 to 0
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y) # This will move segments 987654321, it will go through all segments

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20: # if segment overlaps with head, hence within 20
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)  # hides the segments off screen

            # Clear the segments list
            segments.clear()

            # Reset score
            score = 0

            # Reset delay
            delay = 0.1

            # Update score display
            pen.clear()
            pen.write("Score: {} Highscore: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay) # delay such that the snake does not move too fast for the eye to see


window.mainloop() #keep the window open for us, all code goes between window.tracer and this mainloop
