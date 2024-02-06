# 🔥 🌲 ☁️ ⚡ 🌊 🚁 💛 🟩 🏥 🏦 🧯 🏆 ☁ ❄

from pynput import keyboard
from clouds import Clouds
from map import Map
import time
import os
import json
from helicopter import Helicopter as Helico



TICK_SLEEP = 0.05
TREE_UP = 50
FIRE_UP = 75
CLOUDS_UP = 100
MAP_W, MAP_H = 20, 10

field = Map(MAP_W, MAP_H)
clouds = Clouds(MAP_W, MAP_H)
helico = Helico(MAP_W, MAP_H)
tick = 1

MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1),}
# f - сохранеие, g - восстановление
def pr_key(key):
    global helico, tick, clouds, field
    c = key.char.lower()
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helico.move(dx, dy)
    elif c == 'f':
        data = {'helicopter': helico.export_data(), 
                    'clouds': clouds.export_data(), 
                    'field': field.export_data(),
                    'tick': tick}
        with open('level.json', 'w') as lvl:
            json.dump(data, lvl)
    elif c == 'g':
        with open('level.json', 'r') as lvl:
            data = json.load(lvl)
            tick = data['tick'] or 1
            helico.import_data(data['helicopter'])
            field.import_data(data['field'])
            clouds.import_data(data['clouds'])

listener = keyboard.Listener(
    on_press=None,
    on_release=pr_key,)
listener.start()

while True:
    os.system('cls')
    field.pr_helico(helico, clouds)
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
    
    