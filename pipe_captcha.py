
import pygame
import random
import sys
from collections import deque
import timeit as t

sys.setrecursionlimit(1000000)
WINDOW_WIDTH = 1260
WINDOW_HEIGHT = 840
tiletype_dict={1:(0,1,2,3), 2: (0,1,2,3), 3:(0,1), 4:(0,0)}

percentage = [1,1,1,1,1,1,1,1,2,2,2,2,3,3,4]

difficulty = 3

verify=0

tile_classes= [[0 for i in range(difficulty )] for j in range(difficulty)] 
tile_ids=[[0 for i in range(difficulty)] for j in range(difficulty)]

basic_tile = pygame.image.load("C:\pictures\start.png")
clock = pygame.time.Clock()


pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT),pygame.RESIZABLE)

running = True

class arrow(pygame.sprite.Sprite):
    def __init__(self,type):
        pygame.sprite.Sprite.__init__(self)
        self.direction = random.randint(1,2)
        self.centerx,self.centery=0,0
        if(type=='start'):
            self.arrowtype=5
        else:
            self.arrowtype=6
        self.image = pygame.image.load(f"C:\pictures\{self.arrowtype}_{self.direction}.png")
        self.image = pygame.transform.scale(self.image,(100,100))
    
    def set_position(self):
        if(self.arrowtype==5):
            if(self.direction==1):
                self.centerx,self.centery = (580-100*((difficulty//2)+1),370-100*((difficulty//2)))
                self.show_arrow()
            else:
                self.centerx,self.centery = (580-100*((difficulty//2)),370-100*((difficulty//2)+1))
                self.show_arrow()
        else:
            if(self.direction==1):
                self.centerx,self.centery = (580+100*((difficulty//2)+1),370+100*((difficulty//2)))
                self.show_arrow()
            else:
                self.centerx,self.centery = (580+100*((difficulty//2)),370+100*((difficulty//2)+1))
                self.show_arrow()
    
    def show_arrow(self):
        window.blit(self.image,(self.centerx, self.centery))
    
    def get_info(self):
        return self.direction





startarrow = arrow('start')
startarrow.set_position()
endarrow = arrow('end')  
endarrow.set_position()      

start_direction_1={10,20,21,23,31,40}
start_direction_2={12,20,21,22,30,40}

end_direction_1={12,21,22,23,31,40}
end_direction_2={10,20,22,23,30,40}

direction_up={10,13,20,22,23,30,40}
direction_down={11,12,20,21,22,30,40}
direction_left={12,13,21,22,23,31,40}
direction_right={10,11,20,21,23,31,40}
a=startarrow.get_info()
c=endarrow.get_info()

#bfs
def traversal(z,w):
    good=0
    visited=[[False for i in range(difficulty)] for j in range(difficulty)]
    Q=deque()
    Q.append((z,w))
    while Q:
        z,w=Q.popleft()
        if(z==difficulty-1 and w==difficulty-1):
            good=1
            print('터짐')
            break
        print(z,w)
        print(visited)
        print(tile_ids)
        f=tile_ids[z][w]
        visited[z][w]=True
        if(f==10):
            #하
            if(z<difficulty-1 and visited[z+1][w]==False and tile_ids[z+1][w] in direction_down):
                Q.append((z+1,w))
            #좌
            if(w>0 and visited[z][w-1]==False and tile_ids[z][w-1] in direction_left):
                Q.append((z,w-1))
        elif(f==11):
            #상
            if(z>0 and visited[z-1][w]==False and tile_ids[z-1][w] in direction_up):
                Q.append((z-1,w))
            #좌
            if(w>0 and visited[z][w-1]==False and tile_ids[z][w-1] in direction_left):
                Q.append((z,w-1))
        elif(f==12):
            #상
            if(z>0 and visited[z-1][w]==False and tile_ids[z-1][w] in direction_up):
                Q.append((z-1,w))
            #우
            if(w<difficulty-1 and visited[z][w+1]==False and tile_ids[z][w+1] in direction_right):
                Q.append((z,w+1))
        elif(f==13):
            #하
            if(z<difficulty-1 and visited[z+1][w]==False and tile_ids[z+1][w] in direction_down):
                Q.append((z+1,w))
            #우
            if(w<difficulty-1 and visited[z][w+1]==False and tile_ids[z][w+1] in direction_right):
                Q.append((z,w+1))
        elif(f==20):
            #상
            if(z>0 and visited[z-1][w]==False and tile_ids[z-1][w] in direction_up):
                Q.append((z-1,w))
            #좌
            if(w>0 and visited[z][w-1]==False and tile_ids[z][w-1] in direction_left):
                Q.append((z,w-1))
            #하
            if(z<difficulty-1 and visited[z+1][w]==False and tile_ids[z+1][w] in direction_down):
                Q.append((z+1,w))
        elif(f==21):
            #상
            if(z>0 and visited[z-1][w]==False and tile_ids[z-1][w] in direction_up):
                Q.append((z-1,w))
            #좌
            if(w>0 and visited[z][w-1]==False and tile_ids[z][w-1] in direction_left):
                Q.append((z,w-1))
            #우
            if(w<difficulty-1 and visited[z][w+1]==False and tile_ids[z][w+1] in direction_right):
                Q.append((z,w+1))
        elif(f==22):
            #상
            if(z>0 and visited[z-1][w]==False and tile_ids[z-1][w] in direction_up):
                Q.append((z-1,w))
            #우
            if(w<difficulty-1 and visited[z][w+1]==False and tile_ids[z][w+1] in direction_right):
                Q.append((z,w+1))
            #하
            if(z<difficulty-1 and visited[z+1][w]==False and tile_ids[z+1][w] in direction_down):
                Q.append((z+1,w))
        elif(f==23):
            #하
            if(z<difficulty-1 and visited[z+1][w]==False and tile_ids[z+1][w] in direction_down):
                Q.append((z+1,w))
            #좌
            if(w>0 and visited[z][w-1]==False and tile_ids[z][w-1] in direction_left):
                Q.append((z,w-1))
            #우
            if(w<difficulty-1 and visited[z][w+1]==False and tile_ids[z][w+1] in direction_right):
                Q.append((z,w+1))
        elif(f==30):
            #상
            if(z>0 and visited[z-1][w]==False and tile_ids[z-1][w] in direction_up):
                Q.append((z-1,w))
            #하
            if(z<difficulty-1 and visited[z+1][w]==False and tile_ids[z+1][w] in direction_down):
                Q.append((z+1,w))
        elif(f==31):
            #좌
            if(w>0 and visited[z][w-1]==False and tile_ids[z][w-1] in direction_left):
                Q.append((z,w-1))
            #우
            if(w<difficulty-1 and visited[z][w+1]==False and tile_ids[z][w+1] in direction_right):
                Q.append((z,w+1))
        else:
            #하
            if(z<difficulty-1 and visited[z+1][w]==False and tile_ids[z+1][w] in direction_down):
                Q.append((z+1,w))
            #좌
            if(w>0 and visited[z][w-1]==False and tile_ids[z][w-1] in direction_left):
                Q.append((z,w-1))
            #상
            if(z>0 and visited[z-1][w]==False and tile_ids[z-1][w] in direction_up):
                Q.append((z-1,w))
            #우
            if(w<difficulty-1 and visited[z][w+1]==False and tile_ids[z][w+1] in direction_right):
                Q.append((z,w+1))
    if(good==1):
        return True
    else:
        return False
    

font = pygame.font.SysFont('arial', 30, True, True)    

class Not_Robot(object):
    def __init__(self):
        self.text = font.render('Verified as human', True, (0,0,0))
    
    def show_result(self):
        window.blit(self.text, (500,400))

class left_time(object):
    def __init__(self):
        self.start = t.default_timer()
        self.now = 0
        self.text =font.render(str(int(self.now - self.start)), True, (0,0,0))

    def start_time(self):
        self.now = t.default_timer()
    
    def show_time(self):
        self.text = font.render(str(int(self.now - self.start)), True, (0,0,0))
        window.blit(self.text, (600,50))
    
    def get_time(self):
        return int(self.now - self.start)
timer = left_time()

verified=Not_Robot()

class Done(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f"C:\pictures\done.png")
        self.image = pygame.transform.scale(self.image, (100,100))
        self.hitbox = pygame.Rect(0,0,100,100)
        self.centerx, self.centery=0,0

    def click_check(self, x, y):
        global verify
        global a,c
        print(tile_ids)
        if(self.hitbox.collidepoint(x,y)):
            print('클릭 감지')
            if(a==1 and c==1):
                print('a')
                if(tile_ids[0][0] in start_direction_1 and tile_ids[difficulty-1][difficulty-1] in end_direction_1):
                    if(traversal(0,0)==True):
                        print('verified as 1')
                        verify=1
            elif(a==1 and c==2):
                print('b')
                if(tile_ids[0][0] in start_direction_1 and tile_ids[difficulty-1][difficulty-1] in  end_direction_2):
                    if(traversal(0,0)==True):
                        print('verified as 2')
                        verify=1
            elif(a==2 and c==1):
                print('c')
                if(tile_ids[0][0] in start_direction_2 and tile_ids[difficulty-1][difficulty-1] in end_direction_1):
                    if(traversal(0,0)==True):
                        print('verified as 3')
                        verify=1
            else:
                print('d')
                if(tile_ids[0][0] in start_direction_2 and tile_ids[difficulty-1][difficulty-1] in end_direction_2):
                    if(traversal(0,0)==True):
                        print('verified as 4')
                        verify=1

    def show_done(self):
        window.blit(self.image,(self.centerx, self.centery))

final = Done()

class Reset(pygame.sprite.Sprite):
        def __init__(self):
            self.image = pygame.image.load(f"C:\pictures\\reset.png")
            self.image = pygame.transform.scale(self.image, (100,100))
            self.hitbox = pygame.Rect(1160,740,100,100)
            self.centerx, self.centery =0 , 0

        def click_check(self,x,y):
            if(self.hitbox.collidepoint(x,y)):
                reset_normal()
                print(tile_ids)
        
        def show_reset(self):
            window.blit(self.image,(1160,740))

rezero=Reset()

class Tile(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.tiletype = random.choice(percentage)
        self.rotation = random.choice(tiletype_dict[self.tiletype])
        self.id = self.tiletype*10+self.rotation
        self.image = pygame.image.load(f"C:\pictures\{self.tiletype}_{self.rotation}.png")
        self.image = pygame.transform.scale(self.image, (100,100))
        self.center_x, self.center_y = 0 , 0
        self.pp, self.qq =0 , 0
        self.hitbox = pygame.Rect(0,0,100,100)
        window.blit(self.image, (self.center_x,self.center_y))

    def rotate(self):
        if(self.tiletype==1):
            if(self.rotation==3):
                self.rotation=0
            else:
                self.rotation +=1
        elif(self.tiletype==2):
            if(self.rotation==3):
                self.rotation=0
            else:
                self.rotation +=1
        elif(self.tiletype==3):
            if(self.rotation==1):
                self.rotation=0
            else:
                self.rotation +=1
        self.image= pygame.image.load(f"C:\pictures\{self.tiletype}_{self.rotation}.png")
        self.image = pygame.transform.scale(self.image, (100,100))
        self.edit_id()

        window.blit(self.image, (self.center_x,self.center_y))

    def give_pq(self,p,q):
        self.pp=p
        self.qq=q

    def get_id(self):
        return self.id
    
    def set_position(self, pos_x, pos_y):
        self.center_x, self.center_y = pos_x, pos_y
        self.hitbox = pygame.Rect(self.center_x,self.center_y,100,100)
     
    def show_tile(self):
        window.blit(self.image, (self.center_x, self.center_y))
    
    def click_check(self, x, y):
        if(self.hitbox.collidepoint(x,y)):
            self.rotate()

    def edit_id(self):
        self.id = self.tiletype*10+self.rotation
        tile_ids[self.pp][self.qq]=self.id

hard = difficulty//2
hardish=list(range(-hard, hard+1))

for p in range(difficulty):
    for q in range(difficulty):
        x = Tile()
        x.set_position(580+100*hardish[q],370+100*hardish[p])
        x.give_pq(p,q)
        tile_ids[p][q]=x.get_id()
        tile_classes[p][q]=x

def reset_normal():
    global a,c,difficulty,timer
    global final,startarrow, endarrow
    global tile_ids,tile_classes
    tile_ids = [[0 for i in range(difficulty)] for j in range(difficulty)]
    tile_classes=[[0 for i in range(difficulty)] for j in range(difficulty)]
    hard = difficulty//2
    hardish=list(range(-hard, hard+1))
    final=Done()
    timer=left_time()
    for p in range(difficulty):
        for q in range(difficulty):
            x = Tile()
            x.set_position(580+100*hardish[q],370+100*hardish[p])
            x.give_pq(p,q)
            tile_ids[p][q]=x.get_id()
            tile_classes[p][q]=x

    startarrow = arrow('start')
    startarrow.set_position()
    endarrow = arrow('end')  
    endarrow.set_position() 
    a=startarrow.get_info()
    c=endarrow.get_info()

def reset_InNormal():
    global difficulty
    difficulty+=2
    reset_normal()
    
#runtime
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if(verify==0):
                mouse_x,mouse_y  = event.pos
                final.click_check(mouse_x,mouse_y)
                rezero.click_check(mouse_x,mouse_y)
                for p in tile_classes:
                    for q in p:
                        q.click_check(mouse_x,mouse_y)
    window.fill((255,255,255))
    if(verify==0):
        for p in tile_classes:
            for q in p:
                q.show_tile()
        startarrow.show_arrow()
        endarrow.show_arrow()
        timer.start_time()
        timer.show_time()
        rezero.show_reset()
        if(timer.get_time()==(30*(difficulty//2))):
           reset_InNormal()
    final.show_done()
    if(verify==1):
        verified.show_result()
    pygame.display.update()
    clock.tick(100)