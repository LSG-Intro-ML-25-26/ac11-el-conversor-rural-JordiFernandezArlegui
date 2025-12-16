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
    music.rest(music.beat(BeatFraction.TRIPLET))
    music.play(music.melody_playable(music.footstep),
        music.PlaybackMode.IN_BACKGROUND)
    music.set_volume(255)

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

def setNPCLocation():
    tiles.place_on_tile(NPCs[0], tiles.get_tile_location(2, 1))
    tiles.place_on_tile(NPCs[1], tiles.get_tile_location(11, 1))
    tiles.place_on_tile(NPCs[2], tiles.get_tile_location(7, 6))

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

def on_b_pressed():
    global i
    game.show_long_text("" + str(Math.round(PlayerInventoryLlenya * 100) / 100) + " llenya",
        DialogLayout.BOTTOM)
    i = 0
    while i < len(PlayerInventory):
        game.show_long_text("" + PlayerInventory[i + 1] + " " + PlayerInventory[i],
            DialogLayout.BOTTOM)
        i += 2
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_on_overlap(sprite2, otherSprite):
    global multiplicador_array, i1, i2, input2, indiceListas, PlayerInventoryLlenya
    if nena.overlaps_with(NPCs[0]):
        multiplicador_array = 0
    elif nena.overlaps_with(NPCs[1]):
        multiplicador_array = 1
    else:
        multiplicador_array = 2
    if controller.A.is_pressed():
        music.play(music.melody_playable(music.jump_up),
            music.PlaybackMode.IN_BACKGROUND)
        music.set_volume(120)
        i1 = 2 * multiplicador_array
        i2 = i1 + 1
        if game.ask("Vols " + NPC_inventari[i1] + ("? Tinc " + NPC_inventari[i2])):
            input2 = game.ask_for_number("Digue'm, quants vols?", 2)
            if input2 > parse_float(NPC_inventari[i2]) or input2 % 1 != 0:
                if input2 % 1 != 0:
                    game.splash("No ho dividiré a troços!")
                    pass
                else:
                    game.splash("Aclara't!")
            else:
                if PlayerInventoryLlenya >= input2:
                    game.splash("Genial! Aquí tens!")
                    PlayerInventory.append(NPC_inventari[i1])
                    PlayerInventory.append(convert_to_text(input2))
                    indiceListas = producte2.index_of(NPC_inventari[i1])
                    PlayerInventoryLlenya += 0 - input2 / cantitat[indiceListas] * preu[indiceListas]
                else:
                    game.splash("Surt d'aquí pobre!")
                    game.splash("Torna quan puguis pagar el que vols!")
        else:
            game.show_long_text("Oh... Una pena...\\nEns veiem!", DialogLayout.BOTTOM)
            music.play(music.melody_playable(music.jump_down),
                music.PlaybackMode.IN_BACKGROUND)
            music.set_volume(120)
        pause(100)
sprites.on_overlap(SpriteKind.player, SpriteKind.NPC, on_on_overlap)

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

def setNPCInventari():
    global lista
    lista = 0
    for index in range(3):
        if 0 == 0 % 1:
            NPC_inventari.append(producte2._pick_random())
            NPC_inventari.append(convert_to_text(randint(1, 10)))
        else:
            NPC_inventari.append("llenya")
            NPC_inventari.append(convert_to_text(randint(1, 10)))
    return NPC_inventari

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

lista = 0
indiceListas = 0
input2 = 0
i2 = 0
i1 = 0
multiplicador_array = 0
i = 0
NPC_inventari: List[str] = []
PlayerInventoryLlenya = 0
producte2: List[str] = []
cantitat: List[number] = []
preu: List[number] = []
nena: Sprite = None
NPCs: List[Sprite] = []
PlayerInventory: List[str] = []
j = 0
PlayerInventory = []
music.play(music.create_song(hex("""
        0078000408020700001c00010a006400f401640000040000000000000000000000000005000004360000000400011d08000c00011910001400011e14001800011918001c00011b1c002000011d20002400012028002c00011e30003400011d01001c000f05001202c102c20100040500280000006400280003140006020004180000000400012510001400012020002400012730003400012502001c000c960064006d019001000478002c010000640032000000000a060005060038003c00012903001c0001dc00690000045e0100040000000000000000000005640001040003060038004000012507001c00020a006400f401640000040000000000000000000000000000000003360000000400012008000c00011d10001400011b14001800011d18001c00011e1c002000012020002400012428002c00012230003400012008001c000e050046006603320000040a002d0000006400140001320002010002180000001000012910002000012720003000012a30003c00012909010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c8003000000001000100040005000100100011000100140015000100200021000100240025000100300031000100340035000100
        """)),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)
music.set_volume(20)
NPCs = [sprites.create(img("""
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
        SpriteKind.NPC),
    sprites.create(img("""
            . . . . . . 5 . 5 . . . . . . .
            . . . . . f 5 5 5 f . . . . . .
            . . . . f 6 2 5 5 6 f . . . . .
            . . . f 6 6 6 6 1 6 6 f . . . .
            . . . f 6 6 6 6 6 1 6 f . . . .
            . . . f d f d 6 6 6 1 f . . . .
            . . . f d f d 6 6 6 6 f f . . .
            . . . f d 3 d d 6 6 6 f 6 f . .
            . . . . f d d d f f 6 f f . . .
            . . . . . f f 5 3 f 6 6 6 f . .
            . . . . f 5 3 3 f f f f f . . .
            . . . . f 3 3 f d f . . . . . .
            . . . . . f 3 f d f . . . . . .
            . . . . f 3 5 3 f d f . . . . .
            . . . . f f 3 3 f f . . . . . .
            . . . . . . f f f . . . . . . .
            """),
        SpriteKind.NPC),
    sprites.create(img("""
            . . . . . f f 4 4 f f . . . . .
            . . . . f 5 4 5 5 4 5 f . . . .
            . . . f e 3 3 3 3 3 3 e f . . .
            . . f b 3 3 3 3 3 3 3 3 b f . .
            . . f 3 3 3 3 3 3 3 3 3 3 f . .
            . f 3 3 3 3 3 3 3 3 3 3 3 3 f .
            . f b 3 3 3 3 3 3 3 3 3 3 b f .
            . f b b 3 3 3 3 3 3 3 3 b b f .
            . f b b b b b b b b b b b b f .
            f c b b b b b b b b b b b b c f
            f b b b b b b b b b b b b b b f
            . f c c b b b b b b b b c c f .
            . . e 4 c f f f f f f c 4 e . .
            . . e f b d b d b d b b f e . .
            . . . f f 1 d 1 d 1 d f f . . .
            . . . . . f f b b f f . . . . .
            """),
        SpriteKind.NPC)]
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
    nivel1
    """))
scene.camera_follow_sprite(nena)
setNPCLocation()
tiles.place_on_tile(nena, tiles.get_tile_location(6, 2))
nena.set_stay_in_screen(False)
preu = [6, 2, 5, 3, 12]
cantitat = [1, 1.5, 1, 12, 1]
producte2 = ["gallines", "kg de patates", "cabres", "ous", "cavalls"]
PlayerInventoryLlenya = 100
NPC_inventari = setNPCInventari()
PlayerInventory = []

def on_forever():
    if controller.down.is_pressed():
        walkSound()
    if controller.up.is_pressed():
        walkSound()
    if controller.left.is_pressed():
        walkSound()
    if controller.right.is_pressed():
        walkSound()
forever(on_forever)
