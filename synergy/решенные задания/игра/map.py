# 🟩 🌲 🌊 🏥 🏦 ⬛ 🔥 ☁️ ⚡ 🚁 💛 🧯 🏆 💭
'''
0 - поле
1 - дерево
2 - река
3 - госпиталь
4 - магазин
5 - огонь 
'''
from utils import randbool
from utils import randcell
from utils import randcell2
import os

CELL_TYPES = '🟩🌲🌊🏥🏦🔥'
TREE_BONUS = 100
UP_COST = 500
L_COST = 1000

class Map:
        
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]
        self.generate_forest(6, 10)
        self.generate_river(500)
        self.generate_river(500)
        self.generate_ups()
        self.generate_upl()
        
    def check_bounds(self, x, y):
        if (x < 0 or y < 0 or x >= self.h or y >= self.w):
            return False
        return True
    
    def print_map(self, helico, clouds):
        print('⬛' * (self.w + 2))
        for ri in range(self.h):
            print('⬛', end = '')
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if (clouds.cells[ri][ci] == 1):
                    print('💭', end='')
                elif (clouds.cells[ri][ci] == 2):
                    print('⚡', end='')
                elif (helico.x == ri and helico.y == ci):
                    print('🚁', end='')
                elif (cell >= 0 and cell <= len(CELL_TYPES)):
                    print(CELL_TYPES[cell], end = '')
            print('⬛', end = '')
            print ()
        print('⬛' * (self.w + 2))
        
    def generate_tree(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if (self.check_bounds(cx, cy) and self.cells[cx][cy] == 0 and self.cells[cx][cy] != 2):
            self.cells[cx][cy] = 1
        
    
    def generate_forest(self, r, mxr):
        for ri in range(self.h):
            for ci in range(self.w):
                if randbool(r, mxr):
                    self.cells[ri][ci] = 1
                    
    def generate_river(self, l):
        rc = randcell(self.w, self.h)
        rx, ry = rc[0], rc[1]
        self.cells[rx][ry] = 2
        test = 0 #Переменная для перывания цикла если "река" замкнулась (со всех сторон вода или край карты)
        while l>0:
            rc2 = randcell2(rx, ry)
            rx2, ry2 = rc2[0], rc2[1]
            test += 1
            if test == 10: 
                break            
            if (self.check_bounds(rx2, ry2)) and (self.cells[rx2][ry2] !=2):
                test = 0
                self.cells[rx2][ry2] = 2
                rx, ry = rx2, ry2
                l -= 1
                    
    def add_fire(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if (self.cells[cx][cy] == 1 and self.cells[cx][cy] != 2):
            self.cells[cx][cy] = 5    
    def up_fires(self):
        for ri in range(self.h):
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if cell == 5:
                    self.cells[ri][ci] = 0
        for i in range(10):
            self.add_fire()
            
    def generate_ups(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        while True:        
            if (self.cells[cx][cy] != 2):
                self.cells[cx][cy] = 4
                break
            
    def generate_upl(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        while True:        
            if (self.cells[cx][cy] != 2 and self.cells[cx][cy] != 4):
                self.cells[cx][cy] = 3
                break
     
    def pr_helico(self, helico, clouds):
        c = self.cells[helico.x][helico.y]
        d = clouds.cells[helico.x][helico.y]
        if (c == 2):
            helico.tank = helico.mxtank
        if (c == 5 and helico.tank > 0):
            helico.tank -=1
            self.cells[helico.x][helico.y] = 1
            helico.score += TREE_BONUS
        if (c == 4 and helico.score >= UP_COST):
            helico.mxtank += 1
            helico.score -= UP_COST
        if (c == 3 and helico.score >= L_COST):
            helico.lives += 10
            helico.score -= L_COST
        if (d == 2):
            helico.lives -= 1
            if helico.lives <= 1:
                os.system('cls')
                print(f'Игра окончена, Вы програли и зарабоали: {helico.score}, очков')
                exit(0)
    
    def export_data(self):
        return {'cells': self.cells}
    
    def import_data(self, data):
        self.cells = data['cells'] or [[0 for i in range(self.w)] for j in range(self.h)]