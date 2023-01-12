import pygame,random, sys
from pygame import Rect

#screen

###########################################################


#############################################
def menueventprocess():
    global menu, playing,setting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if startbutton.collidepoint(pos):
                menu = False
                playing = True
            elif levelbutton.collidepoint(pos):
                menu = False
                setting = True
def settingeventprocess():
    global menu , setting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                setting = False
                menu = True


def eventprocess():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_LEFT:
                move.x = -2
            if event.key == pygame.K_RIGHT:
                move.x = 2
            if event.key == pygame.K_UP:
                move.y = -2
            if event.key == pygame.K_DOWN:
                move.y = 2
            if event.key == pygame.K_SPACE:
                redo()
            if event.key == pygame.K_e:
                makefireball()
        if event.type == pygame.KEYUP:
            move.x = 0
            move.y = 0

def personmovement():
    if not end:
        Person.x += move.x
        Person.y += move.y

    if Person.x < 0:
        Person.x = 0
    if Person.x > screensize-Person.width:
        Person.x = screensize-Person.width
    if Person.y < 0:
        Person.y = 0
    if Person.y > screensize - Person.height:
        Person.y = screensize - Person.height

    screen.blit(person,Person)


def delay():
    global delaytime
    if delaytime > 5:
        delaytime = 0
        return True
    delaytime += 1
    return False


def makerain():
    if end:
        return
    if delay():
        index = random.randint(0,len(water)-1)
        if rain[index].y == -1:
            rain[index].x = random.randint(0,screensize)
            rain[index].y = 0

def rainmovement():
    makerain()
    for i in range(len(water)):
        if rain[i].y == -1:
            continue
        if not end:
            rain[i].y += 1
        if rain[i].y > screensize:
            rain[i].y = 0

        screen.blit(water[i],rain[i])

def makeitem():
    global itemfire

    items = ['fire', 'umbrella',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if end:
        return




fire = pygame.image.load("fireball.jpg")
fire = pygame.transform.scale(fire,(25,40))
Fire = fire.get_rect()
Fire.y = -1

def makefireball():
    if end:
        return
    if Fire.y == -40:
        Fire.x = Person.x
        Fire.y = Person.y


def fireball():
    if not end:
        Fire.y -= 1
        if Fire.y < 0:
            Fire.y = -40
    screen.blit(fire,Fire)
def fireraincollision():
    global end
    if end:
        return
    for area in rain:
        if area == -1:
            continue

        if area.top < Fire.bottom and Fire.top < area.bottom and area.left < Fire.right and area.right > Fire.left:
            area.y = -1
            Fire.y = -40
            break

def personraincollision():
    global score,end
    if end:
        return
    for area in rain:
        if area == -1:
            continue
        if area.top < Person.bottom and Person.top < area.bottom and area.left < Person.right and area.right > Person.left:
            print("OOPS")
            end = True
            break
    score += 1

def text():
    font = pygame.font.SysFont("OCR",20,True,False)
    screen.blit(font.render(f'score : {score}',True,'blue'),(10,10,0,0))

    if end and blink():
        screen.blit(font.render("GAME OVER" , True , 'dark red'),(205,300,0,0))
        screen.blit(font.render("[SPACE] to Play Again" , True , 'dark red'),(170,320,0,0))

def blink():
    global delaytime2, blinking
    delaytime2 += 1
    if delaytime2 > 40:
        delaytime2 =0
        blinking = ~blinking
    return blinking

def redo():
    global end, score
    end = False
    score = 0
    for i in range(len(water)):
        rain[i].y = -1
    Fire.y = -40
    Person.centerx = screensize/2
    Person.centery = screensize/2


pygame.init()
screensize = 500
screen = pygame.display.set_mode((screensize,screensize))
playing = False
pygame.display.set_caption('hahahahahaha')
move = Rect(0,0,0,0)
clock = pygame.time.Clock()
delaytime = 0
delaytime2 = 0
blinking = False
score = 0
end = False
itemFire = False
setting = False
menu = True

###############################################################
person = pygame.image.load("person.png")
Person = person.get_rect()
Person.centerx = screensize/2
Person.centery = screensize/2

water = []
rain = []
for i in range(40):
    water.append((pygame.image.load("water.png")))
rain = [None for i in range(len(water))]
for i in range(len(water)):
    water[i] = pygame.transform.scale(water[i],(20,20))
    rain[i] = water[i].get_rect()
    rain[i].y = -1

menubackground = pygame.image.load("menu.png")
start = pygame.image.load("start.png")
level = pygame.image.load("level.png")
print("haha")






#game
while True:
    while menu == True:
        screen.blit(menubackground,(0,0))
        startbutton = screen.blit(start,(125,300))
        levelbutton = screen.blit(level,(160,400))
        menueventprocess()
        pygame.display.flip()

    while setting == True:
        screen.fill((225,225,225))
        settingeventprocess()
        pygame.display.flip()
    while playing == True:
        screen.fill((0,0,0))
        eventprocess()
        personmovement()
        rainmovement()
        fireball()
        fireraincollision()
        personraincollision()
        text()
        pygame.display.flip()
        clock.tick(100)

