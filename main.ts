namespace SpriteKind {
    export const NPC = SpriteKind.create()
}
controller.right.onEvent(ControllerButtonEvent.Released, function () {
    if (controller.left.isPressed()) {
        if (controller.up.isPressed()) {
            if (controller.up.isPressed()) {
                animation.runImageAnimation(
                nena,
                assets.animation`nena-animation-left`,
                100,
                true
                )
            }
        } else if (controller.down.isPressed()) {
            animation.runImageAnimation(
            nena,
            assets.animation`nena-animation-down`,
            100,
            true
            )
        } else {
            animation.runImageAnimation(
            nena,
            assets.animation`nena-animation-left`,
            100,
            true
            )
        }
    } else if (controller.up.isPressed()) {
        if (controller.down.isPressed()) {
            animation.runImageAnimation(
            nena,
            [img`
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
                `],
            0,
            false
            )
        } else {
            animation.runImageAnimation(
            nena,
            assets.animation`nena-animation-up`,
            100,
            true
            )
        }
    } else if (controller.down.isPressed()) {
        animation.runImageAnimation(
        nena,
        assets.animation`nena-animation-down`,
        100,
        true
        )
    } else {
        animation.runImageAnimation(
        nena,
        [img`
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
            `],
        0,
        false
        )
    }
})
function walkSound () {
    music.rest(music.beat(BeatFraction.Triplet))
    music.play(music.melodyPlayable(music.footstep), music.PlaybackMode.InBackground)
}
controller.left.onEvent(ControllerButtonEvent.Released, function () {
    if (controller.right.isPressed()) {
        if (controller.down.isPressed()) {
            if (controller.up.isPressed()) {
                animation.runImageAnimation(
                nena,
                assets.animation`nena-animation-right`,
                100,
                true
                )
            }
        } else if (controller.up.isPressed()) {
            animation.runImageAnimation(
            nena,
            assets.animation`nena-animation-up`,
            100,
            true
            )
        } else {
            animation.runImageAnimation(
            nena,
            assets.animation`nena-animation-right`,
            100,
            true
            )
        }
    } else if (controller.up.isPressed()) {
        if (controller.down.isPressed()) {
            animation.runImageAnimation(
            nena,
            [img`
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
                `],
            0,
            false
            )
        } else {
            animation.runImageAnimation(
            nena,
            assets.animation`nena-animation-up`,
            100,
            true
            )
        }
    } else if (controller.down.isPressed()) {
        animation.runImageAnimation(
        nena,
        assets.animation`nena-animation-down`,
        100,
        true
        )
    } else {
        animation.runImageAnimation(
        nena,
        [img`
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
            `],
        0,
        false
        )
    }
})
scene.onHitWall(SpriteKind.Player, function (sprite, location) {
	
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.NPC, function (sprite, otherSprite) {
    if (controller.A.isPressed()) {
        music.play(music.melodyPlayable(music.baDing), music.PlaybackMode.InBackground)
        game.showLongText("Hola! Quiero 2 GALLINAS", DialogLayout.Bottom)
        music.play(music.melodyPlayable(music.powerDown), music.PlaybackMode.InBackground)
        pause(100)
    }
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    if (controller.up.isPressed()) {
        if (controller.left.isPressed()) {
            if (controller.right.isPressed()) {
                animation.runImageAnimation(
                nena,
                [img`
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
                    `],
                0,
                false
                )
            } else {
                animation.runImageAnimation(
                nena,
                assets.animation`nena-animation-left`,
                100,
                true
                )
            }
        } else if (controller.right.isPressed()) {
            animation.runImageAnimation(
            nena,
            assets.animation`nena-animation-right`,
            100,
            true
            )
        } else {
            animation.runImageAnimation(
            nena,
            [img`
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
                `],
            0,
            false
            )
        }
    } else {
        animation.runImageAnimation(
        nena,
        assets.animation`nena-animation-down`,
        100,
        true
        )
    }
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    if (controller.left.isPressed()) {
        if (controller.down.isPressed()) {
            if (controller.up.isPressed()) {
                animation.runImageAnimation(
                nena,
                [img`
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
                    `],
                0,
                false
                )
            } else {
                animation.runImageAnimation(
                nena,
                assets.animation`nena-animation-up`,
                100,
                true
                )
            }
        } else if (controller.down.isPressed()) {
            animation.runImageAnimation(
            nena,
            assets.animation`nena-animation-down`,
            100,
            true
            )
        } else {
            animation.runImageAnimation(
            nena,
            [img`
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
                `],
            0,
            false
            )
        }
    } else {
        animation.runImageAnimation(
        nena,
        assets.animation`nena-animation-right`,
        100,
        true
        )
    }
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    if (controller.right.isPressed()) {
        if (controller.up.isPressed()) {
            if (controller.down.isPressed()) {
                animation.runImageAnimation(
                nena,
                [img`
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
                    `],
                0,
                false
                )
            } else {
                animation.runImageAnimation(
                nena,
                assets.animation`nena-animation-up`,
                100,
                true
                )
            }
        } else if (controller.down.isPressed()) {
            animation.runImageAnimation(
            nena,
            assets.animation`nena-animation-down`,
            100,
            true
            )
        } else {
            animation.runImageAnimation(
            nena,
            [img`
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
                `],
            0,
            false
            )
        }
    } else {
        animation.runImageAnimation(
        nena,
        assets.animation`nena-animation-left`,
        100,
        true
        )
    }
})
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    if (controller.down.isPressed()) {
        if (controller.left.isPressed()) {
            if (controller.right.isPressed()) {
                animation.runImageAnimation(
                nena,
                [img`
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
                    `],
                0,
                false
                )
            } else {
                animation.runImageAnimation(
                nena,
                assets.animation`nena-animation-left`,
                100,
                true
                )
            }
        } else if (controller.right.isPressed()) {
            animation.runImageAnimation(
            nena,
            assets.animation`nena-animation-right`,
            100,
            true
            )
        } else {
            animation.runImageAnimation(
            nena,
            [img`
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
                `],
            0,
            true
            )
        }
    } else {
        animation.runImageAnimation(
        nena,
        assets.animation`nena-animation-up`,
        100,
        true
        )
    }
})
controller.down.onEvent(ControllerButtonEvent.Released, function () {
    if (controller.up.isPressed()) {
        if (controller.left.isPressed()) {
            if (controller.right.isPressed()) {
                animation.runImageAnimation(
                nena,
                assets.animation`nena-animation-up`,
                100,
                true
                )
            }
        } else if (controller.right.isPressed()) {
            animation.runImageAnimation(
            nena,
            assets.animation`nena-animation-right`,
            100,
            true
            )
        } else {
            animation.runImageAnimation(
            nena,
            assets.animation`nena-animation-up`,
            100,
            true
            )
        }
    } else if (controller.left.isPressed()) {
        if (controller.right.isPressed()) {
            animation.runImageAnimation(
            nena,
            [img`
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
                `],
            0,
            false
            )
        } else {
            animation.runImageAnimation(
            nena,
            assets.animation`nena-animation-left`,
            100,
            true
            )
        }
    } else if (controller.right.isPressed()) {
        animation.runImageAnimation(
        nena,
        assets.animation`nena-animation-right`,
        100,
        true
        )
    } else {
        animation.runImageAnimation(
        nena,
        [img`
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
            `],
        0,
        false
        )
    }
})
controller.up.onEvent(ControllerButtonEvent.Released, function () {
    if (controller.down.isPressed()) {
        if (controller.left.isPressed()) {
            if (controller.right.isPressed()) {
                animation.runImageAnimation(
                nena,
                [img`
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
                    `],
                0,
                true
                )
            }
        } else if (controller.right.isPressed()) {
            animation.runImageAnimation(
            nena,
            assets.animation`nena-animation-right`,
            100,
            true
            )
        } else {
            animation.runImageAnimation(
            nena,
            [img`
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
                `],
            0,
            true
            )
        }
    } else if (controller.left.isPressed()) {
        if (controller.right.isPressed()) {
            animation.runImageAnimation(
            nena,
            [img`
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
                `],
            0,
            false
            )
        } else {
            animation.runImageAnimation(
            nena,
            assets.animation`nena-animation-left`,
            100,
            true
            )
        }
    } else if (controller.right.isPressed()) {
        animation.runImageAnimation(
        nena,
        assets.animation`nena-animation-right`,
        100,
        true
        )
    } else {
        animation.runImageAnimation(
        nena,
        [img`
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
            `],
        0,
        false
        )
    }
})
let nena: Sprite = null
music.play(music.createSong(hex`0078000408020700001c00010a006400f401640000040000000000000000000000000005000004360000000400011d08000c00011910001400011e14001800011918001c00011b1c002000011d20002400012028002c00011e30003400011d01001c000f05001202c102c20100040500280000006400280003140006020004180000000400012510001400012020002400012730003400012502001c000c960064006d019001000478002c010000640032000000000a060005060038003c00012903001c0001dc00690000045e0100040000000000000000000005640001040003060038004000012507001c00020a006400f401640000040000000000000000000000000000000003360000000400012008000c00011d10001400011b14001800011d18001c00011e1c002000012020002400012428002c00012230003400012008001c000e050046006603320000040a002d0000006400140001320002010002180000001000012910002000012720003000012a30003c00012909010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c8003000000001000100040005000100100011000100140015000100200021000100240025000100300031000100340035000100`), music.PlaybackMode.LoopingInBackground)
let npc1 = sprites.create(img`
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
    `, SpriteKind.NPC)
nena = sprites.create(assets.image`nena-front`, SpriteKind.Player)
controller.moveSprite(nena)
scene.setBackgroundImage(img`
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
    `)
tiles.setTilemap(tilemap`airport`)
scene.cameraFollowSprite(nena)
nena.setStayInScreen(false)
tiles.placeOnTile(npc1, tiles.getTileLocation(2, 1))
tiles.placeOnTile(nena, tiles.getTileLocation(7, 2))
let preu = [
6,
2,
5,
3,
12
]
let cantitat = [
1,
1.5,
12,
1
]
let producte = [
"gallina",
"patata",
"cabra",
"ou",
"cavall"
]
forever(function () {
    if (controller.down.isPressed()) {
        walkSound()
    }
    if (controller.up.isPressed()) {
        walkSound()
    }
    if (controller.left.isPressed()) {
        walkSound()
    }
    if (controller.right.isPressed()) {
        walkSound()
    }
})
