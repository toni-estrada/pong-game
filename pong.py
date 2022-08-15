from ursina import *

app = Ursina()

window.color = color.orange
camera.orthographic = True
camera.fov = 1

collision_cooldown = .15

left_paddle = Entity(model="quad", scale=(1 / 32, 6 / 32), x=-.80, origin_x=.5, collider="box")
right_paddle = duplicate(left_paddle, x=left_paddle.x * -1, )
ball = Entity(model="circle", scale=.05, collider="box", speed=10, collision_cooldown=collision_cooldown)

floor = Entity(model="quad", y=-.5, origin_y=.5, scale=(2, 10), collider="box")
ceiling = duplicate(floor, y=.5, rotation_z=180)
left_wall = duplicate(floor, x=-.5 * window.aspect_ratio, rotation_z=90)
right_wall = duplicate(floor, x=.5 * window.aspect_ratio, rotation_z=-90)


def update():
    left_paddle.y += (held_keys["w"] - held_keys["s"]) * time.dt * 1
    right_paddle.y += (held_keys["up arrow"] - held_keys["down arrow"]) * time.dt * 1

    ball.collision_cooldown -= time.dt
    ball.position += ball.right * time.dt * ball.speed

    if ball.collision_cooldown > 0:
        return

    hit_info = ball.intersects()
    if hit_info.hit:
        ball.collision_cooldown = 0.15

        if hit_info.entity in (left_paddle, right_paddle, left_wall, right_wall):
            hit_info.entity.collision = False
            invoke(setattr, hit_info.entity, "collision", False, delay=.1)
            direction_multiplier = 1
            if hit_info.entity == left_paddle:
                direction_multiplier = -1

                left_paddle.collision = False
                right_paddle.collision = True
            else:
                right_paddle.collision = False
                left_paddle.collision = True

            ball.rotation_z += 180 * direction_multiplier
            ball.rotation_z -= (hit_info.entity.world_y - ball.y) * 20 * 32 * direction_multiplier
            ball.speed *= 1.1

        else:
            ball.rotation_z *= -abs(hit_info.world_normal.normalized()[1])


app.run()
