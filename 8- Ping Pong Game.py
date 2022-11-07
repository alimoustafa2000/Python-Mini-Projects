# ---------------------
# import turtle module
# ---------------------

import turtle

# -------------------
# create game's window
# -------------------

window = turtle.Screen()
window.title("Ping Pong By A L I")                      # create window title
window.bgcolor("black")                                 # set the color of the BG
window.setup(width=800, height=600)                     # set window width and hight
window.tracer(0)                                        # prevent auto update of the window

# ----------------
# create player 1
# ----------------

player1 = turtle.Turtle()
player1.speed(0)                                        # set the speed of player1 (the speed of drawing the pixels on the screen) => to be fast
player1.shape("square")                                 # set the shape of player1
player1.shapesize(stretch_wid=5, stretch_len=1)         # set the shape size of player1
player1.color("yellow")                                 # set the color of player1
player1.penup()                                         # to prevent drawing when moving
player1.goto(-370, 0)                                   # set the site of player1

# ----------------
# create player 2
# ----------------

player2 = turtle.Turtle()
player2.speed(0)                                        # set the speed of player2 (the speed of drawing the pixels on the screen) => to be fast
player2.shape("square")                                 # set the shape of player2
player2.shapesize(stretch_wid=5, stretch_len=1)         # set the shape size of player2
player2.color("red")                                    # set the color of player2
player2.penup()                                         # to prevent drawing when moving
player2.goto(370, 0)                                    # set the site of player2

# ----------------
# create the ball
# ----------------

ball = turtle.Turtle()
ball.speed(0)                                           # set the speed of the ball (the speed of drawing the pixels on the screen) => to be fast
ball.shape("circle")                                    # set the shape of the ball
ball.color("white")                                     # set the color of the ball
ball.penup()                                            # to prevent drawing when moving
ball.goto(0, 0)                                         # set the site of the ball
ball.dx = 0.5
ball.dy = 0.5


# ----------------
# create the score
# ----------------

score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)                                          # set the speed of the score (the speed of drawing the pixels on the screen) => to be fast
score.color("white")                                    # set the color of the score
score.penup()                                           # to prevent drawing when moving
score.hideturtle()
score.goto(0, 260)                                      # set the site of the score
score.write("player 1: 0 || player 2: 0", align = "center", font = ("Courier", 15, "normal"))

# ---------------
# game functions
# ---------------

# moving player 1 up
def player1_up():
    y = player1.ycor()                                  # current site of player1
    y += 30                                             # add 30 to the current y axis
    player1.sety(y)                                     # set the new site of player1

# moving player 1 down
def player1_down():
    y = player1.ycor()                                  # current site of player1
    y -= 30                                             # minus 30 from the current y axis
    player1.sety(y)                                     # set the new site of player1

# moving player 2 up
def player2_up():
    y = player2.ycor()                                  # current site of player2
    y += 30                                             # add 30 to the current y axis
    player2.sety(y)                                     # set the new site of player2

# moving player 2 down
def player2_down():
    y = player2.ycor()                                  # current site of player2
    y -= 30                                             # minus 30 from the current y axis
    player2.sety(y)                                     # set the new site of player2


# -----------------
# keyboard binding
# -----------------

window.listen()
window.onkeypress(player1_up, "w")                      # apply player1_up function when I press on "w"
window.onkeypress(player1_down, "s")                    # apply player1_down function when I press on "s"
window.onkeypress(player2_up, "Up")                     # apply player2_up function when I press on "up arrow"
window.onkeypress(player2_down, "Down")                 # apply player2_down function when I press on "down arrow"


# ---------------
# main game loop
# ---------------

while True:

    window.update()                                     # update the screen every time the loop runs

    ball.setx(ball.xcor() + ball.dx)                    # movement of the ball along x axis
    ball.sety(ball.ycor() + ball.dy)                    # movement of the ball along y axis

    if ball.ycor() > 290:                               # if the ball touched the upper boarder of the window (upper boarder of the window at 300 px and the ball is 20 px)

        ball.sety(290)                                  # return the ball again at 290
        ball.dy *= -1                                   # and multiply ball.dy by -1 to become -0.3, so the movement will be in the opposite side


    if ball.ycor() < -290:                              # if the ball touched the lower boarder of the window (lower boarder of the window at -300 px and the ball is 20 px)

        ball.sety(-290)                                 # return the ball again at -290
        ball.dy *= -1                                   # and multiply ball.dy by -1 to become -0.3, so the movement will be in the opposite side


    if ball.xcor() > 390:                               # if the ball touched the right boarder of the window (right boarder of the window at 400 px and the ball is 20 px)

        ball.goto(0, 0)                                 # return the ball again to the center
        ball.dx *= -1                                   # and multiply ball.dx by -1 to become -0.3, so the movement will be in the opposite side

        score1 += 1
        score.clear()                                   # to clear the old score to update it
        score.write(f"player 1: {score1} || player 2: {score2}", align = "center", font = ("Courier", 15, "normal"))


    if ball.xcor() < -390:                              # if the ball touched the left boarder of the window (left boarder of the window at -400 px and the ball is 20 px)

        ball.goto(0, 0)                                 # return the ball again to the center
        ball.dx *= -1                                   # and multiply ball.dx by -1 to become -0.3, so the movement will be in the opposite side

        score2 += 1
        score.clear()                                   # to clear the old score to update it
        score.write(f"player 1: {score1} || player 2: {score2}", align = "center", font = ("Courier", 15, "normal"))


    # collision of player 1 with the ball
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < player1.ycor() + 40 and ball.ycor() > player1.ycor() - 40):

        ball.setx(-340)
        ball.dx *=-1


    # collision of player 2 with the ball
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < player2.ycor() + 40 and ball.ycor() > player2.ycor() - 40):

        ball.setx(340)
        ball.dx *=-1
