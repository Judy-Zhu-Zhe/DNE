import pygame
def main():
   pygame.init()
   pygame.display.set_caption('DNG')  # 游戏标题
   win = pygame.display.set_mode((1000, 1000))  # 窗口尺寸
   map = pygame.image.load('img/map.jpeg').convert_alpha()
   map = pygame.transform.scale(map, (1000, 1000))

   archer = pygame.image.load('img/archer.gif')
   archer = pygame.transform.scale(archer, (20, 20))

   running = True
   while running:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:  # 点击左上角或者右上角的x关闭窗口时，停止程序
               running = False
       win.blit(map, (0, 0))  # 背景图最先加载，坐标是(left, top)
       win.blit(archer, (200, 300))
       pygame.display.flip()
main()