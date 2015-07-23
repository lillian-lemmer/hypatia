# Hypatia 0.2.27 (alpha)

![Hypatia 0.2](https://lillian-lemmer.github.io/hypatia/media/logos/logotype-blacktext-transparentbg.png)

[![GitHub license](https://img.shields.io/github/license/lillian-lemmer/hypatia.svg?style=flat-square)](https://raw.githubusercontent.com/lillian-lemmer/hypatia/master/LICENSE) [![PyPI Version](https://img.shields.io/pypi/v/hypatia_engine.svg?style=flat-square)](https://pypi.python.org/pypi/hypatia_engine/) [![Travis](https://img.shields.io/travis/lillian-lemmer/hypatia.svg?style=flat-square)](https://travis-ci.org/lillian-lemmer/hypatia) [![Coveralls](https://img.shields.io/coveralls/lillian-lemmer/hypatia.svg?style=flat-square)](https://coveralls.io/r/lillian-lemmer/hypatia) [![Code Climate](https://img.shields.io/codeclimate/github/lillian-lemmer/hypatia.svg?style=flat-square)](https://codeclimate.com/github/lillian-lemmer/hypatia) [![PyPI Popularity](https://img.shields.io/pypi/dm/hypatia_engine.svg?style=flat-square)](https://pypi.python.org/pypi/hypatia_engine/) [![Gratipay](https://img.shields.io/gratipay/lillian-lemmer.svg?style=flat-square)](https://gratipay.com/~lillian-lemmer/) [![Bountysource](https://img.shields.io/bountysource/team/hypatia/activity.svg?style=flat-square)](https://www.bountysource.com/teams/hypatia) [![Donate with Paypal](https://img.shields.io/badge/paypal-donate-ff69b4.svg?style=flat-square)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=YFHB5TMMXMNT6) [![Donate with Patreon](https://img.shields.io/badge/patreon-donate%20monthly-ff69b4.svg?style=flat-square)](https://www.patreon.com/lilylemmer) [![My Amazon Wishlist](https://img.shields.io/badge/amazon%20wishlist-buy%20me%20things-ff69b4.svg?style=flat-square)](http://amzn.com/w/NKBZ0CX162S9)

Make 2D action adventure games. For programmers and nonprogrammers alike.

Create a games like [_Legend of Zelda: Oracle of Ages_ and _Oracle of Seasons_](http://en.wikipedia.org/wiki/The_Legend_of_Zelda:_Oracle_of_Seasons_and_Oracle_of_Ages).

The included demo game (`demo/game.py`) in action:

![The demo game in action.](http://lillian-lemmer.github.io/hypatia/media/recordings/2015-06-28-develop-640x480.gif)

[Cross-platform (Windows, Mac, Linux, BSD), putting FreeBSD development first.](https://github.com/lillian-lemmer/hypatia/wiki/Platform-Support)

A labor of love, [permissively (MIT) licensed](https://raw.githubusercontent.com/lillian-lemmer/hypatia/master/LICENSE), and crafted by [Lillian Lemmer](http://github.com/lillian-lemmer/hypatia/wiki/About-the-Creator).

[Please read about how you can help support Hypatia!](https://github.com/lillian-lemmer/hypatia/wiki/Support-the-Project)

# Resources

  * [Installation instructions](https://github.com/lillian-lemmer/hypatia/wiki/Installation-Instructions).
  * [Hypatia Wiki](https://github.com/lillian-lemmer/hypatia/wiki/) (great resource for nonprogrammers, too!)
  * [Hypatia API Docs](https://lillian-lemmer.github.io/hypatia/api)
  * For people, checkout the [socialization and contact methods for the Hypatia project](https://github.com/lillian-lemmer/hypatia/wiki/Profiles).
  * [The official Hypatia website](http://lillian-lemmer.github.io/hypatia/)
  * Official support chat: [#hypatia on Freenode (webui!)](http://webchat.freenode.net/?channels=hypatia)
  * You can contact the author via email: lillian.lynn.lemmer@gmail.com, [@LilyLemmer](https:/twitter.com/LilyLemmer) on Twitter.

# Dive in without any programming

The included demo allows you to mess with all of its resources (see the `resources` directory!). With it you can:

  * [Create tilesheets to make tilemaps](https://github.com/lillian-lemmer/hypatia/wiki/Tilesheets)
    * Configure tiles from the tilesheet
    * Chain tiles together to create animations
    * Apply the "cycle" effect, which takes a non-animated tile, and creates an animated tile by rotating the colors used in the tile
    * Set tile flags, like the `impass_all` flag which makes a flag impassable to the player
  * [Create tilemaps with an arbitrary number of layers, using plaintext files](https://github.com/lillian-lemmer/hypatia/wiki/tilemap.txt)
  * [Create scenes, with configurable NPCs, configurable scene data (player start position)](https://github.com/lillian-lemmer/hypatia/wiki/Nonprogrammer-Guide#editing-scene-data)
  * [Create character sprites using animated or non-animated GIFs](https://github.com/lillian-lemmer/hypatia/wiki/Walkabout-Sprites)

For more information, please read the [official wiki guide for non-programmers](https://github.com/lillian-lemmer/hypatia/wiki/Nonprogrammer-Guide).

# Quick Demo

## Windows

Simply run `game.exe` after extracting [hypatia-demo-windows-current.zip](https://lillian-lemmer.github.io/hypatia/releases/hypatia-demo-windows-current.zip).

## Other

To get setup quickly and start tinkering around with the demo, simply issue the following commands:

  1. `pip install hypatia_engine`
  2. `cd demo`
  3. `python game.py`

# File and Directory Notes

## IMPORTANT

These files are *IMPORTANT* and you should read them before getting started with Hypatia (excluding this README.md):

  * CHANGELOG.md
  * LICENSE
  * CONTRIBUTING.md
  * CODE-OF-CONDUCT.md

## Install Scripts

The following scripts are available for installing Hypatia on specific platfroms from the repo source in the form `platform-major python version.sh`:

  * `install-netbsd-python2.sh`
  * `install-ubuntu-python2.sh`
  * `install-linuxmint-python3.sh`
  * `install-linuxmint-python2.sh`
  * `install-freebsd-python2.sh`
  * `install-base-python2.sh`: this shouldn't be directly ran.

## distribute.sh

This script is used for distributing A NEW RELEASE to PyPi.

## demo/

This directory hosts `game.py`, which is a demo of Hypatia. It also hosts the demo's editable resources.

## docs/

Sphinx docs source. Use the custom `make-sphinx.sh` to build the sphinx documentation from the docstrings.

The *built* Sphinx docs are published to the official Hypatia website, at the following URI: http://lillian-lemmer.github.io/hypatia/api

## etc/

*OPTIONAL* configurations/configuration scripts, helper files, etc. Worth checking out! Has a `objecttypes.xml` for Tiled editor!

## hypatia/

The actual Python package source.

## media/

Media, namely pictures, officially related to Hypatia as a project, e.g., logos, icons.

## requirements/

The requirements files installable by `pip`. Notes on the files:

|Requirements File|You'd want to use if...                        |
|-----------------|-----------------------------------------------|
|base.txt         |ALWAYS!                                        |
|python2.txt      |You use Python 2.x!                            |
|testing.txt      |You want to test and/or contribute to the code!|
|travis.txt       |NEVER                                          |

# tests/

Unit tests for py.test and Travis Continuous Integration. These files are for assuring Hypatia's API remains consistent, reproducible, functional, etc. They are in part what determines build success/fail according to Travis CI. See our `build` badge.

See also: `test.sh`, it's the official script to run when testing any changes.
