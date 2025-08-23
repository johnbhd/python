import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create the turtle to display the title
title_pen = turtle.Turtle()
title_pen.hideturtle()
title_pen.color("white")
title_pen.penup()
title_pen.goto(0, 100)  # Position the text at the top of the screen
title_pen.write("Endless Creative Patterns", align="center", font=("Arial", 24, "bold"))

# Wait for 2 seconds before starting the random gestures
time.sleep(2)

# Clear the screen for random gestures
title_pen.clear()

# Create the turtle for random gestures
gesture_pen = turtle.Turtle()
gesture_pen.speed(0)  # Fastest speed
gesture_pen.hideturtle()

# Define colors
colors = ["red", "blue", "green", "yellow", "purple", "orange", "white", "pink", "cyan"]

# Infinite loop for random gestures
while True:
    # Move to a random position
    gesture_pen.penup()
    gesture_pen.goto(random.randint(-400, 400), random.randint(-400, 400))
    gesture_pen.pendown()

    # Set random color and pen size
    gesture_pen.color(random.choice(colors))
    gesture_pen.pensize(random.randint(1, 5))

    # Randomize the type of gesture
    gesture_type = random.choice(["circle", "line", "star"])
    if gesture_type == "circle":
        radius = random.randint(20, 150)
        gesture_pen.circle(radius)
    elif gesture_type == "line":
        for _ in range(random.randint(3, 6)):
            angle = random.randint(0, 360)
            distance = random.randint(50, 200)
            gesture_pen.forward(distance)
            gesture_pen.left(angle)
    elif gesture_type == "star":
        for _ in range(5):
            gesture_pen.forward(random.randint(50, 150))
            gesture_pen.right(144)
