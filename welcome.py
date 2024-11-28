import turtle
import random
import time

def setup_turtle(color, speed, pensize):
    t = turtle.Turtle()
    t.speed(speed)
    t.color(color)
    t.pensize(pensize)
    t.hideturtle()
    return t

def write_caption_text():
    writer = setup_turtle("lime", 0, 5)
    writer.penup()

    # Centering the text
    writer.goto(0, 50)
    writer.pendown()
    style = ("Impact", 40, "bold")
    writer.write("WELCOME TO", font=style, align="center")
    
    # A small pause for dramatic effect
    time.sleep(0.5)

    # Centering the second line
    writer.penup()
    writer.goto(0, -10)
    writer.pendown()
    writer.write("SUSIE'S GITHUB", font=style, align="center")

def draw_starry_background():
    star = setup_turtle("white", 0, 1)
    star.speed("fastest")
    star.penup()
    
    # Quickly generate 40 stars
    for i in range(40):
        x = random.randint(-400, 400)
        y = random.randint(-300, 300)
        star.goto(x, y)
        # Stars have random sizes to add dimension
        star.dot(random.randint(2, 4))

def main():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Welcome to Susie's Github")
    screen.setup(width=800, height=600)

    draw_starry_background()
    write_caption_text()  # Text on top

    screen.mainloop()

main()
