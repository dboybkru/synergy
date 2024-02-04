# 🔥 🌲 ☁️ ⚡ 🌊 🚁 💛 🟩 🏥 🏦 🧯 🏆 ☁ ❄

from map import Map
import time
import os
from helicopter import Helicopter as Helico
from clouds import Clouds
from pynput import keyboard

TICK_SLEEP = 0.1
TREE_UP = 50
FIRE_UP = 100
CLOUDS_UP = 30
MAP_W, MAP_H = 20, 10

field = Map(MAP_W, MAP_H)
# field.generate_forest(6, 10)
# field.generate_river(1500)
# field.generate_river(1500)
field.add_fire()
# field.generate_ups()

clouds = Clouds(MAP_W, MAP_H)
helico = Helico(MAP_W, MAP_H)

MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1),}


def pr_key(key):
    global helico
    c = key.char.lower()
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helico.move(dx, dy)
        
    
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


listener = keyboard.Listener(
    on_press=None,
    on_release=pr_key)
listener.start()

tick = 1





while True:
    os.system('cls')
    field.pr_helico(helico)
    helico.print_stats()
    field.print_map(helico, clouds)    
    print('Tick', tick)
    tick += 1
    time.sleep(TICK_SLEEP)
    if (tick % TREE_UP == 0):
        field.generate_tree()
        #field.add_fire()
    if (tick % FIRE_UP == 0):
        field.up_fires()
    if (tick % CLOUDS_UP == 0):
        clouds.up_clouds()
    
    