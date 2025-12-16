// Código generado automáticamente. No editar.
namespace myTiles {
    //% fixedInstance jres blockIdentity=images._tile
    export const transparency16 = image.ofBuffer(hex``);

    helpers._registerFactory("tilemap", function(name: string) {
        switch(helpers.stringTrim(name)) {
            case "airport":
            case "airport1":return tiles.createTilemap(hex`10000900040504050405040504050405040504050103020108090203030108090303020303030202070e03020102070e0301020202010303070e03010303070e02030103080c0c0c06060c0c0c0c06060c0c0c090b0d0d0d06060d0d0d0d06060d0d0d0a02020302070e01020302070e0201010302010302070e03020103070e01020202030302010b0a010303020b0a03020301`, img`
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
`, [myTiles.transparency16,sprites.castle.tileGrass2,sprites.castle.tileGrass1,sprites.castle.tileGrass3,sprites.castle.saplingOak,sprites.castle.saplingPine,sprites.castle.tilePath5,sprites.castle.tilePath4,sprites.castle.tilePath1,sprites.castle.tilePath3,sprites.castle.tilePath9,sprites.castle.tilePath7,sprites.castle.tilePath2,sprites.castle.tilePath8,sprites.castle.tilePath6], TileScale.Sixteen);
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
