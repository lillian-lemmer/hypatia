# py.test/test_tiles.py
# Lillian Lemmer <lillian.lynn.lemmer@gmail.com>
#
# This module is part of Hypatia and is released under the
# MIT license: http://opensource.org/licenses/MIT

"""py.test unit testing for hypatia/tiles.py

Run py.test on this module to assert hypatia.tiles
is completely functional.

Example:
  $ py.test tests/

"""

import os

from hypatia import tiles
import pygame

# this script must be ran from project root
os.chdir("demo")


def test_coord_to_index():
    """Tests the coord_to_index lambda functoin from tiles.py"""

    # coords_to_index(row_width, x, y)

    #    0  1  2
    # -----------
    # 0| 00 01 02
    # 1| 03 04 05
    # 2| 06 07 08
    assert tiles.coord_to_index(3, 2, 2) == 8

    #    0  1  2  3  4
    # -----------------
    # 0| 00 01 02 03 04
    # 1| 05 06 07 08 09
    # 2| 10 11 12 13 14
    assert tiles.coord_to_index(5, 4, 2) == 14


def test_tile():
    """Tests Tile() from tiles.py"""

    # first let's be clear about our variables
    faux_tilesheet = pygame.Surface((800, 600))
    tile_id = 1
    tile_size = (10, 10)
    tile_flags = set(['impass_all'])
    subsurface_topleft = (20, 30)
    # ... create tile
    tile = tiles.Tile(tile_id, faux_tilesheet, tile_size,
                      subsurface_topleft, tile_flags)

    # test tile
    assert tile.size == tile_size
    assert tile.id == tile_id
    assert tile.flags == tile_flags
    assert tile.subsurface.get_rect().topleft == (0, 0)
    assert tile.area_on_tilesheet.topleft == (20, 30)


def test_tilesheet():
    """Tests Tilesheet() from tiles.py.

    Note:
      We use the 'debug' resources for predictable output.

    """

    tilesheet = tiles.Tilesheet.from_name('debug')
    tile_width, tile_height = tilesheet.tile_size
    tilesheet_width_in_tiles = (tilesheet.surface.get_rect().width /
                                tile_width)
    tilesheet_height_in_tiles = (tilesheet.surface.get_rect().height /
                                 tile_height)

    # Assert the number of tiles consisting the tilesheet is the
    # product of its width and height in tiles.
    assert (len(tilesheet.tiles) == (tilesheet_width_in_tiles *
                                     tilesheet_height_in_tiles))

    # Assert a known tile's properties to be impassable, as tile #99
    # in the debug tilesheet is defined as impassable.
    assert tilesheet[99].flags == set(['impass_all'])

    # test tile animations

    # The debug tilesheet has two animated tiles. One is animated
    # through chaining, the other is animated through the palette
    # cycle effect.
    assert len(tilesheet.tile_animations) == 2

    # Assert known animated tiles by the PROPER id. The proper ID is
    # either its ID, or the ID of the first tile in a chain animation.
    assert 29 in tilesheet.tile_animations  # the water tile chain
    assert 21 in tilesheet.tile_animations  # cycle effect waterfall

