@namespace
class SpriteKind:
    NPC = SpriteKind.create()

def on_right_released():
    if controller.left.is_pressed():
        if controller.up.is_pressed():
            if controller.up.is_pressed():
                animation.run_image_animation(nena,
                    assets.animation("""
                        nena-animation-left
                        """),
                    100,
                    True)
        elif controller.down.is_pressed():
            animation.run_image_animation(nena,
                assets.animation("""
                    nena-animation-down
                    """),
                100,
                True)
        else:
            animation.run_image_animation(nena,
                assets.animation("""
                    nena-animation-left
                    """),
                100,
                True)
    elif controller.up.is_pressed():
        if controller.down.is_pressed():
            animation.run_image_animation(nena,
                [img("""
                    . f f f . f f f f f . . . .
                    f f f f f c c c c f f . . .
                    f f f f b c c c c c c f . .
                    f f f c 3 c c c c c c f . .
                    . f 3 3 c c c c c c c c f .
                    . f f f c c c c c 4 c c f .
                    . f f f f c c c 4 4 e f f .
                    . f f 4 4 f b f 4 4 e f f .
                    . . f 4 d 4 1 f d d f f . .
                    . . f f f 4 d d d d f . . .
                    . . . f e e 4 4 4 e f . . .
                    . . . 4 d d e 3 3 3 f . . .
                    . . . e d d e 3 3 3 f . . .
                    . . . f e e f 6 6 6 f . . .
                    . . . . f f f f f f . . . .
                    . . . . . f f f . . . . . .
                    """)],
                0,
                False)
        else:
            animation.run_image_animation(nena,
                assets.animation("""
                    nena-animation-up
                    """),
                100,
                True)
    elif controller.down.is_pressed():
        animation.run_image_animation(nena,
            assets.animation("""
                nena-animation-down
                """),
            100,
            True)
    else:
        animation.run_image_animation(nena,
            [img("""
                . f f f . f f f f f . . . .
                f f f f f c c c c f f . . .
                f f f f b c c c c c c f . .
                f f f c 3 c c c c c c f . .
                . f 3 3 c c c c c c c c f .
                . f f f c c c c c 4 c c f .
                . f f f f c c c 4 4 e f f .
                . f f 4 4 f b f 4 4 e f f .
                . . f 4 d 4 1 f d d f f . .
                . . f f f 4 d d d d f . . .
                . . . f e e 4 4 4 e f . . .
                . . . 4 d d e 3 3 3 f . . .
                . . . e d d e 3 3 3 f . . .
                . . . f e e f 6 6 6 f . . .
                . . . . f f f f f f . . . .
                . . . . . f f f . . . . . .
                """)],
            0,
            False)
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)

def walkSound():
    music.play(music.melody_playable(music.footstep),
        music.PlaybackMode.IN_BACKGROUND)
    music.rest(music.beat(BeatFraction.TRIPLET))

def on_left_released():
    if controller.right.is_pressed():
        if controller.down.is_pressed():
            if controller.up.is_pressed():
                animation.run_image_animation(nena,
                    assets.animation("""
                        nena-animation-right
                        """),
                    100,
                    True)
        elif controller.up.is_pressed():
            animation.run_image_animation(nena,
                assets.animation("""
                    nena-animation-up
                    """),
                100,
                True)
        else:
            animation.run_image_animation(nena,
                assets.animation("""
                    nena-animation-right
                    """),
                100,
                True)
    elif controller.up.is_pressed():
        if controller.down.is_pressed():
            animation.run_image_animation(nena,
                [img("""
                    . . . . f f f f f . f f f .
                    . . . f f c c c c f f f f f
                    . . f c c c c c c b f f f f
                    . . f c c c c c c 3 c f f f
                    . f c c c c c c c c 3 3 f .
                    . f c c 4 c c c c c f f f .
                    . f f e 4 4 c c c f f f f .
                    . f f e 4 4 f b f 4 4 f f .
                    . . f f d d f 1 4 d 4 f . .
                    . . . f d d d d 4 f f f . .
                    . . . f e 4 4 4 e e f . . .
                    . . . f 3 3 3 e d d 4 . . .
                    . . . f 3 3 3 e d d e . . .
                    . . . f 6 6 6 f e e f . . .
                    . . . . f f f f f f . . . .
                    . . . . . . f f f . . . . .
                    """)],
                0,
                False)
        else:
            animation.run_image_animation(nena,
                assets.animation("""
                    nena-animation-up
                    """),
                100,
                True)
    elif controller.down.is_pressed():
        animation.run_image_animation(nena,
            assets.animation("""
                nena-animation-down
                """),
            100,
            True)
    else:
        animation.run_image_animation(nena,
            [img("""
                . . . . f f f f f . f f f .
                . . . f f c c c c f f f f f
                . . f c c c c c c b f f f f
                . . f c c c c c c 3 c f f f
                . f c c c c c c c c 3 3 f .
                . f c c 4 c c c c c f f f .
                . f f e 4 4 c c c f f f f .
                . f f e 4 4 f b f 4 4 f f .
                . . f f d d f 1 4 d 4 f . .
                . . . f d d d d 4 f f f . .
                . . . f e 4 4 4 e e f . . .
                . . . f 3 3 3 e d d 4 . . .
                . . . f 3 3 3 e d d e . . .
                . . . f 6 6 6 f e e f . . .
                . . . . f f f f f f . . . .
                . . . . . . f f f . . . . .
                """)],
            0,
            False)
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

def on_hit_wall(sprite, location):
    pass
scene.on_hit_wall(SpriteKind.player, on_hit_wall)

def on_on_overlap(sprite2, otherSprite):
    if controller.A.is_pressed():
        music.play(music.melody_playable(music.ba_ding),
            music.PlaybackMode.IN_BACKGROUND)
        game.show_long_text("Hola! Quiero 2 GALLINAS", DialogLayout.BOTTOM)
        music.play(music.melody_playable(music.power_down),
            music.PlaybackMode.IN_BACKGROUND)
        pause(100)
sprites.on_overlap(SpriteKind.player, SpriteKind.NPC, on_on_overlap)

def on_down_pressed():
    if controller.up.is_pressed():
        if controller.left.is_pressed():
            if controller.right.is_pressed():
                animation.run_image_animation(nena,
                    [img("""
                        . f f f . f f f f . f f f .
                        f f f f f c c c c f f f f f
                        f f f f b c c c c b f f f f
                        f f f c 3 c c c c 3 c f f f
                        . f 3 3 c c c c c c 3 3 f .
                        . f c c c c 4 4 c c c c f .
                        . f f c c 4 4 4 4 c c f f .
                        . f f f b f 4 4 f b f f f .
                        . f f 4 1 f d d f 1 4 f f .
                        . . f f d d d d d d f f . .
                        . . e f e 4 4 4 4 e f e . .
                        . e 4 f b 3 3 3 3 b f 4 e .
                        . 4 d f 3 3 3 3 3 3 c d 4 .
                        . 4 4 f 6 6 6 6 6 6 f 4 4 .
                        . . . . f f f f f f . . . .
                        . . . . f f . . f f . . . .
                        """)],
                    0,
                    False)
            else:
                animation.run_image_animation(nena,
                    assets.animation("""
                        nena-animation-left
                        """),
                    100,
                    True)
        elif controller.right.is_pressed():
            animation.run_image_animation(nena,
                assets.animation("""
                    nena-animation-right
                    """),
                100,
                True)
        else:
            animation.run_image_animation(nena,
                [img("""
                    . f f f . f f f f . f f f .
                    f f f f f c c c c f f f f f
                    f f f f b c c c c b f f f f
                    f f f c 3 c c c c 3 c f f f
                    . f 3 3 c c c c c c 3 3 f .
                    . f c c c c c c c c c c f .
                    . f f c c c c c c c c f f .
                    . f f f c c c c c c f f f .
                    . f f f f f f f f f f f f .
                    . . f f f f f f f f f f . .
                    . . e f f f f f f f f e . .
                    . e 4 f f f f f f f f 4 e .
                    . 4 d f 3 3 3 3 3 3 c d 4 .
                    . 4 4 f 6 6 6 6 6 6 f 4 4 .
                    . . . . f f f f f f . . . .
                    . . . . f f . . f f . . . .
                    """)],
                0,
                False)
    else:
        animation.run_image_animation(nena,
            assets.animation("""
                nena-animation-down
                """),
            100,
            True)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_right_pressed():
    if controller.left.is_pressed():
        if controller.down.is_pressed():
            if controller.up.is_pressed():
                animation.run_image_animation(nena,
                    [img("""
                        . f f f . f f f f f . . . .
                        f f f f f c c c c f f . . .
                        f f f f b c c c c c c f . .
                        f f f c 3 c c c c c c f . .
                        . f 3 3 c c c c c c c c f .
                        . f f f c c c c c 4 c c f .
                        . f f f f c c c 4 4 e f f .
                        . f f 4 4 f b f 4 4 e f f .
                        . . f 4 d 4 1 f d d f f . .
                        . . f f f 4 d d d d f . . .
                        . . . f e e 4 4 4 e f . . .
                        . . . 4 d d e 3 3 3 f . . .
                        . . . e d d e 3 3 3 f . . .
                        . . . f e e f 6 6 6 f . . .
                        . . . . f f f f f f . . . .
                        . . . . . f f f . . . . . .
                        """)],
                    0,
                    False)
            else:
                animation.run_image_animation(nena,
                    assets.animation("""
                        nena-animation-up
                        """),
                    100,
                    True)
        elif controller.down.is_pressed():
            animation.run_image_animation(nena,
                assets.animation("""
                    nena-animation-down
                    """),
                100,
                True)
        else:
            animation.run_image_animation(nena,
                [img("""
                    . . . . f f f f f . f f f .
                    . . . f f c c c c f f f f f
                    . . f c c c c c c b f f f f
                    . . f c c c c c c 3 c f f f
                    . f c c c c c c c c 3 3 f .
                    . f c c 4 c c c c c f f f .
                    . f f e 4 4 c c c f f f f .
                    . f f e 4 4 f b f 4 4 f f .
                    . . f f d d f 1 4 d 4 f . .
                    . . . f d d d d 4 f f f . .
                    . . . f e 4 4 4 e e f . . .
                    . . . f 3 3 3 e d d 4 . . .
                    . . . f 3 3 3 e d d e . . .
                    . . . f 6 6 6 f e e f . . .
                    . . . . f f f f f f . . . .
                    . . . . . . f f f . . . . .
                    """)],
                0,
                False)
    else:
        animation.run_image_animation(nena,
            assets.animation("""
                nena-animation-right
                """),
            100,
            True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_left_pressed():
    if controller.right.is_pressed():
        if controller.up.is_pressed():
            if controller.down.is_pressed():
                animation.run_image_animation(nena,
                    [img("""
                        . . . . f f f f f . f f f .
                        . . . f f c c c c f f f f f
                        . . f c c c c c c b f f f f
                        . . f c c c c c c 3 c f f f
                        . f c c c c c c c c 3 3 f .
                        . f c c 4 c c c c c f f f .
                        . f f e 4 4 c c c f f f f .
                        . f f e 4 4 f b f 4 4 f f .
                        . . f f d d f 1 4 d 4 f . .
                        . . . f d d d d 4 f f f . .
                        . . . f e 4 4 4 e e f . . .
                        . . . f 3 3 3 e d d 4 . . .
                        . . . f 3 3 3 e d d e . . .
                        . . . f 6 6 6 f e e f . . .
                        . . . . f f f f f f . . . .
                        . . . . . . f f f . . . . .
                        """)],
                    0,
                    False)
            else:
                animation.run_image_animation(nena,
                    assets.animation("""
                        nena-animation-up
                        """),
                    100,
                    True)
        elif controller.down.is_pressed():
            animation.run_image_animation(nena,
                assets.animation("""
                    nena-animation-down
                    """),
                100,
                True)
        else:
            animation.run_image_animation(nena,
                [img("""
                    . f f f . f f f f f . . . .
                    f f f f f c c c c f f . . .
                    f f f f b c c c c c c f . .
                    f f f c 3 c c c c c c f . .
                    . f 3 3 c c c c c c c c f .
                    . f f f c c c c c 4 c c f .
                    . f f f f c c c 4 4 e f f .
                    . f f 4 4 f b f 4 4 e f f .
                    . . f 4 d 4 1 f d d f f . .
                    . . f f f 4 d d d d f . . .
                    . . . f e e 4 4 4 e f . . .
                    . . . 4 d d e 3 3 3 f . . .
                    . . . e d d e 3 3 3 f . . .
                    . . . f e e f 6 6 6 f . . .
                    . . . . f f f f f f . . . .
                    . . . . . f f f . . . . . .
                    """)],
                0,
                False)
    else:
        animation.run_image_animation(nena,
            assets.animation("""
                nena-animation-left
                """),
            100,
            True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_up_pressed():
    if controller.down.is_pressed():
        if controller.left.is_pressed():
            if controller.right.is_pressed():
                animation.run_image_animation(nena,
                    [img("""
                        . f f f . f f f f . f f f .
                        f f f f f c c c c f f f f f
                        f f f f b c c c c b f f f f
                        f f f c 3 c c c c 3 c f f f
                        . f 3 3 c c c c c c 3 3 f .
                        . f c c c c c c c c c c f .
                        . f f c c c c c c c c f f .
                        . f f f c c c c c c f f f .
                        . f f f f f f f f f f f f .
                        . . f f f f f f f f f f . .
                        . . e f f f f f f f f e . .
                        . e 4 f f f f f f f f 4 e .
                        . 4 d f 3 3 3 3 3 3 c d 4 .
                        . 4 4 f 6 6 6 6 6 6 f 4 4 .
                        . . . . f f f f f f . . . .
                        . . . . f f . . f f . . . .
                        """)],
                    0,
                    False)
            else:
                animation.run_image_animation(nena,
                    assets.animation("""
                        nena-animation-left
                        """),
                    100,
                    True)
        elif controller.right.is_pressed():
            animation.run_image_animation(nena,
                assets.animation("""
                    nena-animation-right
                    """),
                100,
                True)
        else:
            animation.run_image_animation(nena,
                [img("""
                    . f f f . f f f f . f f f .
                    f f f f f c c c c f f f f f
                    f f f f b c c c c b f f f f
                    f f f c 3 c c c c 3 c f f f
                    . f 3 3 c c c c c c 3 3 f .
                    . f c c c c 4 4 c c c c f .
                    . f f c c 4 4 4 4 c c f f .
                    . f f f b f 4 4 f b f f f .
                    . f f 4 1 f d d f 1 4 f f .
                    . . f f d d d d d d f f . .
                    . . e f e 4 4 4 4 e f e . .
                    . e 4 f b 3 3 3 3 b f 4 e .
                    . 4 d f 3 3 3 3 3 3 c d 4 .
                    . 4 4 f 6 6 6 6 6 6 f 4 4 .
                    . . . . f f f f f f . . . .
                    . . . . f f . . f f . . . .
                    """)],
                0,
                True)
    else:
        animation.run_image_animation(nena,
            assets.animation("""
                nena-animation-up
                """),
            100,
            True)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_down_released():
    if controller.up.is_pressed():
        if controller.left.is_pressed():
            if controller.right.is_pressed():
                animation.run_image_animation(nena,
                    assets.animation("""
                        nena-animation-up
                        """),
                    100,
                    True)
        elif controller.right.is_pressed():
            animation.run_image_animation(nena,
                assets.animation("""
                    nena-animation-right
                    """),
                100,
                True)
        else:
            animation.run_image_animation(nena,
                assets.animation("""
                    nena-animation-up
                    """),
                100,
                True)
    elif controller.left.is_pressed():
        if controller.right.is_pressed():
            animation.run_image_animation(nena,
                [img("""
                    . f f f . f f f f . f f f .
                    f f f f f c c c c f f f f f
                    f f f f b c c c c b f f f f
                    f f f c 3 c c c c 3 c f f f
                    . f 3 3 c c c c c c 3 3 f .
                    . f c c c c 4 4 c c c c f .
                    . f f c c 4 4 4 4 c c f f .
                    . f f f b f 4 4 f b f f f .
                    . f f 4 1 f d d f 1 4 f f .
                    . . f f d d d d d d f f . .
                    . . e f e 4 4 4 4 e f e . .
                    . e 4 f b 3 3 3 3 b f 4 e .
                    . 4 d f 3 3 3 3 3 3 c d 4 .
                    . 4 4 f 6 6 6 6 6 6 f 4 4 .
                    . . . . f f f f f f . . . .
                    . . . . f f . . f f . . . .
                    """)],
                0,
                False)
        else:
            animation.run_image_animation(nena,
                assets.animation("""
                    nena-animation-left
                    """),
                100,
                True)
    elif controller.right.is_pressed():
        animation.run_image_animation(nena,
            assets.animation("""
                nena-animation-right
                """),
            100,
            True)
    else:
        animation.run_image_animation(nena,
            [img("""
                . f f f . f f f f . f f f .
                f f f f f c c c c f f f f f
                f f f f b c c c c b f f f f
                f f f c 3 c c c c 3 c f f f
                . f 3 3 c c c c c c 3 3 f .
                . f c c c c 4 4 c c c c f .
                . f f c c 4 4 4 4 c c f f .
                . f f f b f 4 4 f b f f f .
                . f f 4 1 f d d f 1 4 f f .
                . . f f d d d d d d f f . .
                . . e f e 4 4 4 4 e f e . .
                . e 4 f b 3 3 3 3 b f 4 e .
                . 4 d f 3 3 3 3 3 3 c d 4 .
                . 4 4 f 6 6 6 6 6 6 f 4 4 .
                . . . . f f f f f f . . . .
                . . . . f f . . f f . . . .
                """)],
            0,
            False)
controller.down.on_event(ControllerButtonEvent.RELEASED, on_down_released)

def on_up_released():
    if controller.down.is_pressed():
        if controller.left.is_pressed():
            if controller.right.is_pressed():
                animation.run_image_animation(nena,
                    [img("""
                        . f f f . f f f f . f f f .
                        f f f f f c c c c f f f f f
                        f f f f b c c c c b f f f f
                        f f f c 3 c c c c 3 c f f f
                        . f 3 3 c c c c c c 3 3 f .
                        . f c c c c 4 4 c c c c f .
                        . f f c c 4 4 4 4 c c f f .
                        . f f f b f 4 4 f b f f f .
                        . f f 4 1 f d d f 1 4 f f .
                        . . f f d d d d d d f f . .
                        . . e f e 4 4 4 4 e f e . .
                        . e 4 f b 3 3 3 3 b f 4 e .
                        . 4 d f 3 3 3 3 3 3 c d 4 .
                        . 4 4 f 6 6 6 6 6 6 f 4 4 .
                        . . . . f f f f f f . . . .
                        . . . . f f . . f f . . . .
                        """)],
                    0,
                    True)
        elif controller.right.is_pressed():
            animation.run_image_animation(nena,
                assets.animation("""
                    nena-animation-right
                    """),
                100,
                True)
        else:
            animation.run_image_animation(nena,
                [img("""
                    . f f f . f f f f . f f f .
                    f f f f f c c c c f f f f f
                    f f f f b c c c c b f f f f
                    f f f c 3 c c c c 3 c f f f
                    . f 3 3 c c c c c c 3 3 f .
                    . f c c c c 4 4 c c c c f .
                    . f f c c 4 4 4 4 c c f f .
                    . f f f b f 4 4 f b f f f .
                    . f f 4 1 f d d f 1 4 f f .
                    . . f f d d d d d d f f . .
                    . . e f e 4 4 4 4 e f e . .
                    . e 4 f b 3 3 3 3 b f 4 e .
                    . 4 d f 3 3 3 3 3 3 c d 4 .
                    . 4 4 f 6 6 6 6 6 6 f 4 4 .
                    . . . . f f f f f f . . . .
                    . . . . f f . . f f . . . .
                    """)],
                0,
                True)
    elif controller.left.is_pressed():
        if controller.right.is_pressed():
            animation.run_image_animation(nena,
                [img("""
                    . f f f . f f f f . f f f .
                    f f f f f c c c c f f f f f
                    f f f f b c c c c b f f f f
                    f f f c 3 c c c c 3 c f f f
                    . f 3 3 c c c c c c 3 3 f .
                    . f c c c c c c c c c c f .
                    . f f c c c c c c c c f f .
                    . f f f c c c c c c f f f .
                    . f f f f f f f f f f f f .
                    . . f f f f f f f f f f . .
                    . . e f f f f f f f f e . .
                    . e 4 f f f f f f f f 4 e .
                    . 4 d f 3 3 3 3 3 3 c d 4 .
                    . 4 4 f 6 6 6 6 6 6 f 4 4 .
                    . . . . f f f f f f . . . .
                    . . . . f f . . f f . . . .
                    """)],
                0,
                False)
        else:
            animation.run_image_animation(nena,
                assets.animation("""
                    nena-animation-left
                    """),
                100,
                True)
    elif controller.right.is_pressed():
        animation.run_image_animation(nena,
            assets.animation("""
                nena-animation-right
                """),
            100,
            True)
    else:
        animation.run_image_animation(nena,
            [img("""
                . f f f . f f f f . f f f .
                f f f f f c c c c f f f f f
                f f f f b c c c c b f f f f
                f f f c 3 c c c c 3 c f f f
                . f 3 3 c c c c c c 3 3 f .
                . f c c c c c c c c c c f .
                . f f c c c c c c c c f f .
                . f f f c c c c c c f f f .
                . f f f f f f f f f f f f .
                . . f f f f f f f f f f . .
                . . e f f f f f f f f e . .
                . e 4 f f f f f f f f 4 e .
                . 4 d f 3 3 3 3 3 3 c d 4 .
                . 4 4 f 6 6 6 6 6 6 f 4 4 .
                . . . . f f f f f f . . . .
                . . . . f f . . f f . . . .
                """)],
            0,
            False)
controller.up.on_event(ControllerButtonEvent.RELEASED, on_up_released)

nena: Sprite = None
npc1 = sprites.create(img("""
        . . . . . . f f f f . . . . . .
        . . . . f f f 2 2 f f f . . . .
        . . . f f f 2 2 2 2 f f f . . .
        . . f f f e e e e e e f f f . .
        . . f f e 2 2 2 2 2 2 e e f . .
        . . f e 2 f f f f f f 2 e f . .
        . . f f f f e e e e f f f f . .
        . f f e f b f 4 4 f b f e f f .
        . f e e 4 1 f d d f 1 4 e e f .
        . . f e e d d d d d d e e f . .
        . . . f e e 4 4 4 4 e e f . . .
        . . e 4 f 2 2 2 2 2 2 f 4 e . .
        . . 4 d f 2 2 2 2 2 2 f d 4 . .
        . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
        . . . . . f f f f f f . . . . .
        . . . . . f f . . f f . . . . .
        """),
    SpriteKind.NPC)
nena = sprites.create(assets.image("""
    nena-front
    """), SpriteKind.player)
controller.move_sprite(nena)
scene.set_background_image(img("""
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    """))
tiles.set_tilemap(tilemap("""
    airport
    """))
scene.camera_follow_sprite(nena)
nena.set_stay_in_screen(False)
tiles.place_on_tile(npc1, tiles.get_tile_location(2, 1))
tiles.place_on_tile(nena, tiles.get_tile_location(7, 2))
preu = [6, 2, 5, 3, 12]
cantitat = [1, 1.5, 12, 1]
producte = ["gallina", "patata", "cabra", "ou", "cavall"]