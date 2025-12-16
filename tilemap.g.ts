// Código generado automáticamente. No editar.
namespace myTiles {
    //% fixedInstance jres blockIdentity=images._tile
    export const transparency16 = image.ofBuffer(hex``);

    helpers._registerFactory("tilemap", function(name: string) {
        switch(helpers.stringTrim(name)) {
            case "nivel1":
            case "nivel1":return tiles.createTilemap(hex`0d0009000d0d0d0d0d0d0d0d0d0d0d0d0d0b0b0103070c0b0b0307010c0c01010c060a0b010c060a010c0b0c0c0b060a0c0b0b060a0b0b0103050502020505050202050507040909020209090902020909080b0101060a010c0c060a0c0b0c0c0b0c060a0b0c01060a010c010b010c04080b010c04080b010b`, img`
. . . . . . . . . . . . . 
. . . . . . . . . . . . . 
. . . . . . . . . . . . . 
. . . . . . . . . . . . . 
. . . . . . . . . . . . . 
. . . . . . . . . . . . . 
. . . . . . . . . . . . . 
. . . . . . . . . . . . . 
. . . . . . . . . . . . . 
`, [myTiles.transparency16,sprites.castle.tileGrass2,sprites.castle.tilePath5,sprites.castle.tilePath1,sprites.castle.tilePath7,sprites.castle.tilePath2,sprites.castle.tilePath4,sprites.castle.tilePath3,sprites.castle.tilePath9,sprites.castle.tilePath8,sprites.castle.tilePath6,sprites.castle.tileGrass1,sprites.castle.tileGrass3,sprites.builtin.forestTiles22], TileScale.Sixteen);
        }
        return null;
    })

    helpers._registerFactory("tile", function(name: string) {
        switch(helpers.stringTrim(name)) {
            case "transparency16":return transparency16;
        }
        return null;
    })

}
// Código generado automáticamente. No editar.
