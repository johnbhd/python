import turtle
import math
import time
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Radar Simulation")
screen.setup(width=800, height=800)  # Increase window size for a bigger radar

# Draw the radar circle (increase radius)
radar_circle = turtle.Turtle()
radar_circle.hideturtle()
radar_circle.speed(0)
radar_circle.color("green")
radar_circle.penup()
radar_circle.goto(0, -500)  # Increased radius for a larger circle
radar_circle.pendown()
radar_circle.circle(500)  # Increased circle radius

# Draw radial lines (increase spacing based on the new circle size)
radar_circle.penup()
radar_circle.goto(0, 0)
for angle in range(0, 360, 30):
    radar_circle.setheading(angle)
    radar_circle.pendown()
    radar_circle.forward(500)  # Increased length for larger radar
    radar_circle.penup()
    radar_circle.goto(0, 0)

# Radar sweep line (increase the length to match new radar size)
sweep_line = turtle.Turtle()
sweep_line.hideturtle()
sweep_line.speed(0)
sweep_line.color("lime")
sweep_line.width(3)  # Increase width for better visibility

# Radar dots for enemies
enemy_dots = [turtle.Turtle() for _ in range(8)]
for dot in enemy_dots:
    dot.hideturtle()
    dot.speed(0)
    dot.color("red")
    dot.penup()
    dot.shapesize(2)  # Increase the size of the red dots

# Enemy states: [(angle, x, y, visible_until_time, blink_timer)]
def generate_enemy_positions():
    enemies = []
    for _ in range(8):  # Always have 8 enemies
        angle = random.randint(0, 359)
        distance = random.randint(50, 500)  # Increased range for larger radar
        x = distance * math.cos(math.radians(angle))
        y = distance * math.sin(math.radians(angle))
        enemies.append((angle, x, y, 0, 0))  # Initially invisible and no blink timer
    return enemies

def radar_sweep():
    angle = 0
    active_enemies = generate_enemy_positions()
    enemy_timer = time.time()  # Timer for enemy relocation

    while True:
        # Clear previous sweep line
        sweep_line.clear()

        # Draw the sweep line
        sweep_line.penup()
        sweep_line.goto(0, 0)
        sweep_line.setheading(angle)
        sweep_line.pendown()
        sweep_line.forward(500)  # Increased length for larger radar

        # Check if the sweep line intersects with any enemy
        current_time = time.time()
        for i, (enemy_angle, x, y, visible_until, blink_timer) in enumerate(active_enemies):
            if abs(angle - enemy_angle) <= 2 and current_time > visible_until:  # Enemy detected
                active_enemies[i] = (enemy_angle, x, y, current_time + 2.5, current_time)  # Stay visible for 2.5 seconds and set blink timer

        # Update enemy visibility and blinking
        for i, (enemy_angle, x, y, visible_until, blink_timer) in enumerate(active_enemies):
            if current_time <= visible_until:  # Enemy is visible
                if current_time - blink_timer >= 0.2:  # Blink every 0.2 seconds
                    if enemy_dots[i].isvisible():
                        enemy_dots[i].hideturtle()
                    else:
                        enemy_dots[i].goto(x, y)
                        enemy_dots[i].showturtle()
                    active_enemies[i] = (enemy_angle, x, y, visible_until, current_time)
            else:
                enemy_dots[i].hideturtle()

        # Relocate enemies every 3 seconds
        if current_time - enemy_timer > 2:
            active_enemies = generate_enemy_positions()
            enemy_timer = current_time

        # Control speed of the sweep line (speed up by decreasing sleep time)
        time.sleep(0.005)  # Decrease the sleep time to make the sweep line faster

        # Update the angle
        angle = (angle + 6) % 360  # Increase the angle increment to make the line rotate faster

# Start radar sweep
radar_sweep()
