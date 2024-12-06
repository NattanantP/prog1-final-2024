import turtle
import ball
import random

num_balls = 5
turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()
canvas_width = turtle.screensize()[0]
canvas_height = turtle.screensize()[1]
print(canvas_width, canvas_height)
ball_radius = 0.05 * canvas_width
turtle.colormode(255)
xpos = []
ypos = []
vx = []
vy = []
ball_color = []

class RunBall:
    def __init__(self, num_balls):
        self.num_balls = num_balls
        self.ball_list = []
        self.t = 0.0
        self.pq = []
        self.HZ = 4
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        print(self.canvas_width, self.canvas_height)

        ball_radius = 0.05 * self.canvas_width
        # create random number of balls, num_balls, located at random positions within the canvas; each ball has a random velocity value in the x and y direction and is painted with a random color
        for i in range(num_balls):
            xpos.append(random.uniform(-1*canvas_width + ball_radius, canvas_width - ball_radius))
            ypos.append(random.uniform(-1*canvas_height + ball_radius, canvas_height - ball_radius))
            vx.append(10*random.uniform(-1.0, 1.0))
            vy.append(10*random.uniform(-1.0, 1.0))
            ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))


    def draw_border(self):
        turtle.penup()
        turtle.goto(-canvas_width, -canvas_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))
        for i in range(2):
            turtle.forward(2*canvas_width)
            turtle.left(90)
            turtle.forward(2*canvas_height)
            turtle.left(90)

    def run(self):
        while (True):
                e = heapq.heappop(self.pq)
                if not e.is_valid():
                    continue

                ball_a = e.a
                ball_b = e.b

                for i in range(len(self.ball_list)):
                    self.ball_list[i].move(e.time - self.t)
                self.t = e.time

                if (ball_a is not None) and (ball_b is not None) and (paddle_a is None):
                    ball_a.bounce_off(ball_b)
                elif (ball_a is not None) and (ball_b is None) and (paddle_a is None):
                    ball_a.bounce_off_vertical_wall()
                elif (ball_a is None) and (ball_b is not None) and (paddle_a is None):
                    ball_b.bounce_off_horizontal_wall()
                elif (ball_a is None) and (ball_b is None) and (paddle_a is None):
                    self.__redraw()
                elif (ball_a is not None) and (ball_b is None) and (paddle_a is not None):
                    ball_a.bounce_off_paddle()

                self.__predict(ball_a)
                self.__predict(ball_b)

# hold the window; close it by clicking the window close 'x' mark
turtle.done()
