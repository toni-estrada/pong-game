from ursina import *

app = Ursina()

window.color = color.orange
camera.orthographic = True
camera.fov = 1

collision_cooldown = .15

left_paddle = Entity(model="quad", scale=(1/32, 6/32), x=-.80,  origin_x=.5, collider="box")
right_paddle = duplicate(left_paddle, x=left_paddle.x*-1,)
ball = Entity(model="circle", scale=.05, collider="box", speed=0, collision_cooldown=collision_cooldown)

floor = Entity(model="quad", y=-.5, origin_y=.49, scale=(2, 1), collider="box",)
ceiling = duplicate(floor, y=floor.y*-1, rotation_z=180)
left_wall = duplicate(floor, x=-.5*window.aspect_ratio, rotation_z=90)
right_wall = duplicate(floor, x=.5*window.aspect_ratio, rotation_z=-90)

app.run()
