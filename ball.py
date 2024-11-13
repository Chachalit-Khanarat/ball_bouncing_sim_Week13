from math import sqrt
import turtle

class ball():
    def __init__(self, color, size, x, y , vx, vy, mass):
        self.color = color
        self.size = size
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.mass = mass

    def draw_ball(self):
        # draw a circle of radius equals to size at x, y coordinates and paint it with color
        turtle.penup()
        turtle.color(self.color)
        turtle.fillcolor(self.color)
        turtle.goto(self.x,self.y-self.size)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()

    def move_ball(self,dt):
        # update the x, y coordinates of ball i with velocity in the x (vx) and y (vy) components
        self.x += self.vx*dt
        self.y += self.vy*dt


    def update_ball_velocity(self, canvas_width, canvas_height):
        # if the ball hits the side walls, reverse the vx velocity
        if abs(self.x) > (canvas_width - self.size):
            self.vx = -self.vx

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(self.y) > (canvas_height - self.size):
            self.vy = -self.vy

    def check_collision(self, other):
        if sqrt((self.x - other.x)**2 + (self.y - other.y)**2) < self.size + other.size :
            return True
        return False

    def resolve_collision(self, other):
        if self.check_collision(other):
            # Calculate normal and tangent unit vectors
            normal = [(self.x - other.x) / sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2), 
                      (self.y - other.y) / sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)]
            tangent = [-normal[1], normal[0]]

            # Project velocities onto the normal and tangent vectors
            v1n = normal[0] * self.vx + normal[1] * self.vy
            v1t = tangent[0] * self.vx + tangent[1] * self.vy
            v2n = normal[0] * other.vx + normal[1] * other.vy
            v2t = tangent[0] * other.vx + tangent[1] * other.vy

            # Calculate new normal velocities using conservation of momentum
            v1n_final = (v1n * (self.mass - other.mass) + 2 * other.mass * v2n) / (self.mass + other.mass)
            v2n_final = (v2n * (other.mass - self.mass) + 2 * self.mass * v1n) / (self.mass + other.mass)

            # Convert scalar normal and tangent velocities into vectors
            self.vx = v1n_final * normal[0] + v1t * tangent[0]
            self.vy = v1n_final * normal[1] + v1t * tangent[1]
            other.vx = v2n_final * normal[0] + v2t * tangent[0]
            other.vy = v2n_final * normal[1] + v2t * tangent[1]

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.color == other.color and self.mass == other.mass




