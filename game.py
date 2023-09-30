#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 20:22:38 2023

@author: admin
"""
import pygame, math, sys, random
from grid import Grid
from aliens import Aliens
from crew import Crew


SCREEN_W, SCREEN_H = 640, 480
row,column=5,5
k=3

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption('grid game')

    font = pygame.font.SysFont('arialrounded', 12)

    
    clock = pygame.time.Clock()
    done = False

    grid_pixel_w, grid_pixel_h = 460, 460
    grid = Grid(row,column, grid_pixel_w, grid_pixel_h)
    crew = Crew(grid.openSpaces,row,column, grid_pixel_w, grid_pixel_h)
    
    #aliensSpaces=random.sample(grid.openSpaces,k)
    aliens=Aliens(k,grid.openSpaces,row,column,grid_pixel_w, grid_pixel_h)
    
    xscale = grid_pixel_w / grid.w
    yscale = grid_pixel_h / grid.h
    
    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                
        screen.fill((0, 0, 0))

        x_offset = (SCREEN_W - grid_pixel_w) / 2
        y_offset = (SCREEN_H - grid_pixel_h) / 2
    
        grid.draw(screen, x_offset, y_offset)
        aliens.moveAlien(screen, x_offset, y_offset)
    

        crew.new(screen, x_offset, y_offset)
        print(xscale,yscale,x_offset, y_offset)
        for i in range(1,row+2):
            new_height = round((i-1) * xscale)
            new_width = round(i * yscale)
            pygame.draw.line(screen,  (255,255,0), (x_offset, new_height+y_offset), (550, new_height+y_offset), 2)
            pygame.draw.line(screen, (255,255,0), (new_width-2, y_offset), (new_width-2, grid_pixel_h+10), 2)
        
        text1 = "Green - Bot"
        label1 = font.render(text1, 1, (255, 255, 255))
        text2 = "Red - Aliens"
        label2 = font.render(text2, 1, (255, 255, 255))
        text3 = "Blue - Crew"
        label3 = font.render(text3, 1, (255, 255, 255))
        text4 = "White-Opened"
        label4 = font.render(text4, 1, (255, 255, 255))
        text5 = "Grid"
        label5 = font.render(text5, 1, (255, 255, 255))
        screen.blit(label1, (5, 5))
        screen.blit(label2, (5, 15))
        screen.blit(label3, (5, 25))
        screen.blit(label4, (5, 35))
        screen.blit(label5, (40, 45))
        
        pygame.display.flip()
        clock.tick(60)


    
    
if __name__ == '__main__':
    main()