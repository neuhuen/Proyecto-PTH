#pgzero
import random
import time

WIDTH = 1070
HEIGHT = 600

TITLE = "Alien Sweep"
FPS = 30

#--------------------------------------PLAYER--------------------------------------
ship = Actor("player1", (535, 500))

#--------------------------------------BACKGROUND--------------------------------------
background = Actor("LVL1", size=(WIDTH,HEIGHT))
background2 = Actor("LVL22", size=(WIDTH,HEIGHT))
background3 = Actor("LVL33", size=(WIDTH,HEIGHT))
boss = Actor("boss1", (535,0), size=(870, 100))
bala_boss = Actor("laserRed1", (535,350), size=(200,600))
carga_boss = Actor("laserRedShot1", (535,80), size=(400,70))
carga_boss.angle=90
fail = Actor("fail1", size=(WIDTH,HEIGHT))

play = Actor("play1" , (535, 300), size=(200,100))
title = Actor("titulo1",(535,50))
carga = Actor("carga1",(535,300), size=(1070,600))

mode = "LVL3"

#--------------------------------------ENEMIGOS / BALAS--------------------------------------
enemigos = []
balas = []
balas_boss = []

def spawn_enemigos(level):
    enemigos = []

    if level == "LVL1":
        for i in range(10):
            x = random.randint(20, 1050)
            y = random.randint(-500, -50)
            enemy = Actor("enemy1", (x, y))
            enemy.vida = 1
            enemigos.append(enemy)

    if level == "LVL2":
        for i in range(10):
            x = random.randint(20, 1050)
            y = random.randint(-500, -50)
            enemy = Actor("enemy1", (x, y))
            enemy.vida = 1
            enemigos.append(enemy)

        for i in range(5):
            x = random.randint(20, 1050)
            y = random.randint(-500, -50)
            enemy2 = Actor("enemy22", (x, y))
            enemy2.vida = 3
            enemigos.append(enemy2)

    if level == "LVL3":
        for i in range(15):
            x = random.randint(20, 1050)
            y = random.randint(-500, -50)
            enemy2 = Actor("enemy22", (x, y))
            enemy2.vida = 3
            enemigos.append(enemy2)
        
        for i in range(1):
            x = random.randint(400, 700)
            y = random.randint(500, 50)
            bala_boss = Actor("laserRed", (x, y))
            balas_boss.append(bala_boss)
    return enemigos

#----------------------------------------DRAW---------------------------------
def draw():
    if mode=="menu":
        background.draw()
        play.draw()
        title.draw()

    if mode=="LVL1":
        background.draw()
        ship.draw()
        for bala in balas:
            bala.draw()
        for enemigo in enemigos:
            enemigo.draw()

    if mode=="LVL2":
        background2.draw()
        ship.draw()
        for bala in balas:
            bala.draw()
        for enemigo in enemigos:
            enemigo.draw()

    if mode=="LVL3":
        background3.draw()
        ship.draw()
        boss.draw()
        carga_boss.draw()
        for bala in balas:
            bala.draw()
        for enemigo in enemigos:
            enemigo.draw()

    if mode=="fail":
        fail.draw()
        screen.draw.text("Presiona TAB para reiniciar", pos=(10, 10), fontsize= 40)

boss

#----------------------------------------MOUSE---------------------------------
def on_mouse_move(pos):
    ship.pos = pos

def on_mouse_down(button, pos):
    global mode, enemigos, balas
    if mode == "menu" and play.collidepoint(pos):
        mode = "LVL1"
        enemigos = spawn_enemigos("LVL1")
        balas = []

    if mode in ("LVL1","LVL2","LVL3") and button == mouse.LEFT:
        bala = Actor("laserGreen11", pos=ship.pos)
        balas.append(bala)

#----------------------------------------KEYS---------------------------------
def on_key_down(key):
    global mode
    if mode in ("LVL1", "LVL2", "LVL3", "fail"):
        if key == keys.TAB:
            mode = "menu"

#----------------------------------------UPDATE---------------------------------
def movement():
    global active
    active=True

clock.schedule(movement, 1)
active = True

def update(dt):
    global mode, enemigos, balas, active

    if mode in ("LVL1","LVL2","LVL3"):

        # --- mover enemigos ---
        if active == True:
            for enemigo in enemigos:
                enemigo.y += random.randint(3,5)
                rng = random.randint(1,2)
                if rng == 1:
                    enemigo.x -= random.randint(2,5)
                
                elif rng == 2:
                    enemigo.x += random.randint(2,5)
                    
                if enemigo.y > 650:
                    mode = "fail"
                    return

        # --- mover balas ---
        for bala in balas[:]:
            bala.y -= 10
            if bala.y < 0:
                balas.remove(bala)

        # --- colision ship vs enemigos ---
        if ship.collidelist(enemigos) != -1:
            mode = "fail"
            return

        # --- colision balas vs enemigos ---
        for bala in balas:
            enemy_index = bala.collidelist(enemigos)
            if enemy_index != -1:
                enemy=enemigos[enemy_index]
                enemy.vida -= 1
                balas.remove(bala)
                if enemy.vida == 0:
                    enemigos.pop(enemy_index)
                break
            


        # --- cambio de nivel ---
        if mode == "LVL1" and len(enemigos) == 0:
            mode = "LVL2"
            enemigos = spawn_enemigos("LVL2")

        if mode == "LVL2" and len(enemigos) == 0:
            mode = "LVL3"
            enemigos = spawn_enemigos("LVL3")

