import pygame,random, sys
from pygame import Rect, mixer

############################################################### eventprocess
def menueventprocess():
    global menu, playing,setting, description
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
            elif howtoplaybutton.collidepoint(pos):
                menu = False
                description = True


def settingeventprocess():
    global menu , setting, easy, medium, hard, music
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                setting = False
                menu = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            MOUSE_X,MOUSE_Y = pygame.mouse.get_pos()
            if MOUSE_X >= 150 and MOUSE_X <= 350 and MOUSE_Y >= 37 and MOUSE_Y <= 97:
                easy = True
                medium = False
                hard = False
            if MOUSE_X >= 150 and MOUSE_X <= 350 and MOUSE_Y >= 137 and MOUSE_Y <= 197:
                easy = False
                medium = True
                hard = False
            if MOUSE_X >= 150 and MOUSE_X <= 350 and MOUSE_Y >= 237 and MOUSE_Y <= 297:
                easy = False
                medium = False
                hard = True
            if MOUSE_X >= 45 and MOUSE_X <= 245 and MOUSE_Y >= 337 and MOUSE_Y <= 397:
                music = True
                mixer.music.play()
            if MOUSE_X >= 225 and MOUSE_X <= 425 and MOUSE_Y >= 337 and MOUSE_Y <= 397:
                music = False
                mixer.music.stop()

def descriptioneventprocess():
    global menu, setting, description, pageflip
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                description = False
                menu = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            MOUSE_X,MOUSE_Y = pygame.mouse.get_pos()
            if MOUSE_X >= screensize-70 and MOUSE_X <= screensize and MOUSE_Y >= screensize-70 and MOUSE_Y <= screensize:
                if pageflip == True:
                    pageflip = False
                elif pageflip == False:
                    pageflip = True

def eventprocess():
    global easy, medium, hard, playing, menu, end, gaineditem, playerspeed
    if easy == True:
        playerspeed = 2
    if easy == False:
        playerspeed = 3
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                playing = False
                menu = True
                redo()
            if event.key == pygame.K_LEFT:
                move.x -= playerspeed
            if event.key == pygame.K_RIGHT:
                move.x += playerspeed
            if event.key == pygame.K_UP:
                move.y -= playerspeed
            if event.key == pygame.K_DOWN:
                move.y += playerspeed
            if event.key == pygame.K_SPACE:
                if end:
                    redo()
            if event.key == pygame.K_e:
                if easy == True or gaineditem > 0:
                    makefireball()
                    gaineditem -=1
        if event.type == pygame.KEYUP:
            move.x = 0
            move.y = 0


############################################################### display
def settingoptions():
    global easy,medium,hard,color1,color2,color3, musicoff, musicon
    screen.fill((50,50,50))
    if easy == True:
        color1 = chosen
        color2 = gray
        color3 = gray
    if medium == True:
        color1 = gray
        color2 = chosen
        color3 = gray
    if hard == True:
        color1 = gray
        color2 = gray
        color3 = chosen
    if music == True:
        musicon = chosen
        musicoff = gray
    if music == False:
        musicoff = chosen
        musicon = gray
    screen.blit(color1,(150,37))
    screen.blit(color2,(150,137))
    screen.blit(color3,(150,237))
    screen.blit(musicon,(45,337))
    screen.blit(musicoff,(255,337))
    screen.blit(text1,((screensize - text1.get_width())//2, 50))
    screen.blit(text2,((screensize - text1.get_width())//2, 150))
    screen.blit(text3,((screensize - text1.get_width())//2, 250))
    screen.blit(text4,(screensize/2-gray.get_width()+5, 350))
    screen.blit(text5,(screensize-gray.get_width()-35, 350))

def rule():
    screen.blit(nextpage,(430,430))
    screen.blit(pygame.transform.scale(person,(50,50)),(61,25))
    screen.blit(pygame.transform.scale(water[0],(50,50)),(61,125))
    screen.blit(pygame.transform.scale(item,(50,50)),(61,225))
    screen.blit(pygame.transform.scale(fire,(50,50)),(61,325))
    screen.blit(pygame.transform.scale(charge1,(50,50)),(61,425))

    screen.blit(text10,(160,40))
    screen.blit(text11,(160,140))
    screen.blit(text12,(160,240))
    screen.blit(text13,(160,340))
    screen.blit(text14,(160,440))

def explaining():
    screen.blit(previouspage,(430,430))
    screen.blit(up,(61,10))
    screen.blit(down,(61,61))
    screen.blit(right,(112,61))
    screen.blit(left,(10,61))
    screen.blit(E,(61,160))
    screen.blit(esc,(61,260))
    screen.blit(space,(61,360))

    screen.blit(text6,(185,77))
    screen.blit(text7,(185,275))
    screen.blit(text8,(185,175))
    screen.blit(text9,(185,375))
############################################################### sprite
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

def makerain():
    if end:
        return
    if delay():
        if hard == False:
            index = random.randint(0,len(water)-1)
            if rain[index].y == -1:
                rain[index].x = random.randint(0,screensize)
                rain[index].y = 0
        if hard == True:
            index = random.randint(0,len(water2)-1)
            if rain2[index].y == -1:
                rain2[index].x = random.randint(0,screensize)
                rain2[index].y = 0

def rainmovement():
    global speed
    if medium == True:
        speed = 1
    if medium == False:
        speed = 2
    makerain()
    if hard == False:
        for i in range(len(water)):
            if rain[i].y == -1:
                continue
            if not end:
                rain[i].y += speed
            if rain[i].y > screensize:
                rain[i].y = 0
            screen.blit(water[i],rain[i])
    if hard == True:
        for i in range(len(water2)):
            if rain2[i].y == -1:
                continue
            if not end:
                rain2[i].y += speed
            if rain2[i].y > screensize:
                rain2[i].y = 0
            screen.blit(water2[i],rain2[i])

def makeitem():
    if end or itemout == True:
        return
    if Item.y == -40:
        Item.x = random.randint(0,screensize)
        Item.y =0

def itemmovement():
    global items, itemout, getitem
    if not end:
        if easy == True:
            return
        if itemout == False and Item.y < 0 and getitem != 'fire' and hard == True:
            items = ['fire',
                     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                     ]
            getitem = random.choice(items)
        if hard == False and itemout == False and Item.y < 0:
            getitem = 'fire'
        if getitem == 'fire':
            makeitem()
            Item.y += 1
            itemout = True
        if Item.y > screensize:
            Item.y = -40
            itemout = False
            getitem = 0
    screen.blit(item,Item)

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



############################################################### collision
def fireraincollision():
    global end, score
    if end:
        return
    for area in rain:
        if area.y == -1:
            continue
        if area.top < Fire.bottom and Fire.top < area.bottom and area.left < Fire.right and area.right > Fire.left:
            area.y = -1
            Fire.y = -40
            score += 10
            break
    for area in rain2:
        if area.y == -1:
            continue
        if area.top < Fire.bottom and Fire.top < area.bottom and area.left < Fire.right and area.right > Fire.left:
            area.y = -1
            Fire.y = -40
            score += 10
            break

def personraincollision():
    global end
    if end:
        return
    for area in rain:
        if area == -1:
            continue
        if area.top < Person.bottom and Person.top < area.bottom and area.left < Person.right and area.right > Person.left:
            print("OOPS")
            end = True
            break
    for area in rain2:
        if area == -1:
            continue
        if area.top < Person.bottom and Person.top < area.bottom and area.left < Person.right and area.right > Person.left:
            print("OOPS")
            end = True
            break

def personitemcollision():
    global itemout, getitem, gaineditem
    if end:
        return
    if Item.top < Person.bottom and Person.top < Item.bottom and Item.left < Person.right and Item.right > Person.left:
        Item.y = -40
        itemout = False
        getitem = ''
        gaineditem += 1


############################################################### leftover functions
def delay():
    global delaytime
    if delaytime > 10:
        delaytime = 0
        return True
    delaytime += 1
    return False

def text():
    screen.blit(font.render(f'score : {score}',True,'blue'),(10,10,0,0))
    if end and blink():
        gameovertext = font.render("GAME OVER" , True , 'dark red')
        screen.blit(gameovertext, ((screensize - gameovertext.get_width())//2, 250))
        playagaintext = font.render("[SPACE] to Play Again" , True , 'dark red')
        screen.blit(playagaintext, ((screensize - playagaintext.get_width())//2,350))

def blink():
    global delaytime2, blinking
    delaytime2 += 1
    if delaytime2 > 40:
        delaytime2 =0
        blinking = ~blinking
    return blinking

def redo():
    global end, score, getitem, itemout, gaineditem
    end = False
    score = 0
    for i in range(len(water)):
        rain[i].y = -1
    for i in range(len(water2)):
        rain2[i].y = -1
    Fire.y = -40
    Item.y = -40
    Person.centerx = screensize/2
    Person.centery = screensize/2
    getitem = 0
    itemout = False
    gaineditem = 0


############################################################### bunch of variables
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
easy = True
medium = False
hard = False
speed= 2
playerspeed = 3
itemout = False
getitem = ''
gaineditem = 0
description = False
music = True
pageflip = False

############################################################### font stuff
font = pygame.font.SysFont("terminal",50,True,False)
text1 = font.render("Lv.1",True, "green")
text2 = font.render("Lv.2",True, "blue")
text3 = font.render("Lv.3",True, "red")
text4 = font.render("Music On",True,"Black")
text5 = font.render("Music Off",True,"black")
#bauhaus93 28
#script 30



font2 = pygame.font.SysFont("bauhaus93",28,False,False)
text6 = font2.render("Arrows to Move",True,"Black")
text7 = font2.render("ESC to Go Back to Menu",True,"Black")
text8 = font2.render("E to Fire Fireball",True,"Black")
text9 = font2.render("Space to Restart",True,"Black")
text10 = font2.render("the character",True,"Black")
text11 = font2.render("the acid rain",True,"Black")
text12 = font2.render("the item that gives fireball",True,"Black")
text13 = font2.render("the fireball",True,"Black")
text14 = font2.render("the charge of fireball",True,"Black")

############################################################### image load stuff
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

water2 = []
rain2 = []
for i in range(50):
    water2.append((pygame.image.load("water.png")))
rain2 = [None for i in range(len(water2))]
for i in range(len(water2)):
    water2[i] = pygame.transform.scale(water2[i],(30,30))
    rain2[i] = water2[i].get_rect()
    rain2[i].y = -1


fire = pygame.image.load("fireball.jpg")
fire = pygame.transform.scale(fire,(25,40))
Fire = fire.get_rect()
Fire.y = -1

item = pygame.image.load("item.png")
Item = item.get_rect()
Item.y = -40

menubackground = pygame.image.load("menu.png")
start = pygame.image.load("start.png")
level = pygame.image.load("level.png")
gray = pygame.image.load("gray.png")
chosen = pygame.image.load("chosen.png")
color1 = chosen
color2 = gray
color3 = gray
musicoff = gray
musicon = chosen
charge1 = pygame.image.load("slot.png")
charge2 = pygame.image.load("slot.png")
howtoplay = pygame.image.load("howtoplay.png")
up = pygame.image.load("up.png")
down = pygame.image.load("down.png")
right = pygame.image.load("right.png")
left = pygame.image.load("left.png")
esc = pygame.image.load("esc.png")
E = pygame.image.load("E.png")
space = pygame.image.load("space.png")
nextpage = pygame.image.load("next page.png")
previouspage = pygame.image.load("previous page.png")

############################################################### music
mixer.init()
mixer.music.load("fresh wave.wav")
mixer.music.play(-1)


############################################################### game loop
while True:
    while menu == True:
        screen.blit(menubackground,(0,0))
        startbutton = screen.blit(start,(125,270))
        levelbutton = screen.blit(level,(160,360))
        howtoplaybutton = screen.blit(howtoplay, (185,430))
        menueventprocess()
        pygame.display.flip()
    while setting == True:
        screen.fill((225,225,225))
        settingoptions()
        settingeventprocess()
        pygame.display.flip()
    while description == True:
        screen.fill((200,200,200))
        if pageflip == False:
            rule()
        elif pageflip == True:
            explaining()
        descriptioneventprocess()
        pygame.display.flip()
    while playing == True:
        screen.fill((0,0,0))
        eventprocess()
        personmovement()
        rainmovement()
        itemmovement()
        fireball()
        fireraincollision()
        personraincollision()
        personitemcollision()
        if gaineditem > 0:
            screen.blit(charge2, (screensize - 75, screensize - 75))
            if gaineditem > 1:
                screen.blit(charge1, (screensize - 150, screensize - 75))
        text()
        pygame.display.flip()
        clock.tick(100)
