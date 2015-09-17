import pygame
import pygame.camera
from pygame.locals import *
pygame.init()
pygame.camera.init()


import pygame.camera,os,time
pygame.camera.init()
cam =pygame.camera.Camera(pygame.camera.list_cameras()[0])
cam.start()
import pygame.image
img = cam.get_image()
pygame.image.save(img, "photo.bmp")
pygame.camera.quit()
os.system('start C:/Python34/photo.bmp')
import pygame.image
while True:
    try:
        pygame.image.save(cam.get_image(), "photo.bmp")
        pygame.camera.quit()
        time.sleep(2)
    except:
        pass

