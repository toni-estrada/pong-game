from ursina import *

app = Ursina()

window.color = color.orange
camera.orthographic = True
camera.fov = 1

collision_cooldown = .15

left_paddle = Entity(model="quad", scale=(1/32, 6/32), x=-.80,  origin_x=.5, collider="box")
right_paddle = duplicate(left_paddle, x=left_paddle.x*-1,)
ball = Entity(model="circle", scale=.05, collider="box", speed=0, collision_cooldown=collision_cooldown)


app.run()