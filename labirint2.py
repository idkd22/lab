# Разработай свою игру в этом файле!
from pygame import *
display.set_caption("Лабиринт")
window = display.set_mode((500, 500))
back = (200, 255, 255)
window.fill(back)
picture = transform.scale(image.load("ghost.png"),(500,500))
wall = transform.scale(image.load("stick.png"),(500,500))

class GameSprite(sprite.Sprite):
    def __init__():
        super().__init__(self,player_image,w,h,x,y,speed)
        self.image-transform.scale(image.load(picture), (w,h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

barriers = sprite.Group()

class Player(GameSprite):
    def __init__(self, x_speed, y_speed, player_x, player_y, size_x, size_y):
        super().__init__(self)
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        if packman.rect.x <= win_width-80 and packman.x_speed > 0 or packman.rect.x >= 0 and packman.x_speed < 0:
            self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)
        if packman.rect.y <= win_height-80 and packman.y_speed > 0 or packman.rect.y >= 0 and packman.y_speed < 0:
            self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0:
            for p in platforms_touched:
                self.rect.bottom = min(self.rect.bottom, p.rect.top)
        elif self.y_speed > 0:
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)

class Enemy(GameSprite):
    side = "left"
    def __Init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed

    def update(self):
        if self.rect.x <= 420:
            self.side = 'fight'
        if self.rect.x >= win_width - 85:
            self.side = 'left'
        if self.side == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed)
    GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
    self.speed = player_speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.x = win_width+10:
            self.kill()

w1 = GameSprite('stick.png', win_width / 2 - win_width / 3, win_height / 2, 300, 50)
w2 = GameSprite('stick.png', 370, 100, 50, 400)

barriers.add(w1)
barriers.add(w2)
packman = Player('ghost.png', 5, win_height - 80, 80, 80, 0, 0)
monster = GameSprite('pngegg.png', win_width - 80, 100, 80, 80)
final_sprite = GameSprite('stick.png', win_width - 85, win_height - 100, 80, 80)

finish = False
run = True
while run:
    time.delay(50)
    window.blit(picture,(0,0))
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                packman.x_speed = -5
            elif e.key == K_RIGHT:
                packman.x_speed = 5
            elif e.key == K_UP:
                packman.y_speed = -5
            elif e.key == K_DOWN:
                packman.y_speed = 5
        elif e.type == KEYUP:
            if e.key == K_LEFT:
                packman.x_speed = 0
            elif e.key == K_RIGHT:
                packman.x_speed = 0
            elif e.key == K_UP:
                packman.y_speed = 0
            elif e.key == K_DOWN:
                packman.y_speed = 0

if not finish:
    window.fill(back)
    barriers.draw(window)
    monster.reset()
    final_sprite.reset()
    packman.reset()
    packman.update()

    if sprite.collide_rect(packman, monster):
        finish = True
        img = image.load('game-over_1.jpeg')
        d = img.get_width() // img.get_height()
        window.fill(255, 255, 255)
        window.blit(transform.scale(img, (win_height * d, win_height)), (90, 0))
    if sprite.collide_rect(packman, final_sprite):
        finish = True
        img = image.load(stick.png)
        window.fill(255, 255, 255)
        window.blit(transform.scale(img, (win_width, win_height)), (0, 0))

    display.update()