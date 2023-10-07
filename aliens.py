#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 08:37:41 2023

@author: admin
"""
import copy,random,pygame

class Aliens(object):
    def __init__(self, k,openSpaces,row,column, pixel_w, pixel_h):
        self.k=k
        self.openSpaces = openSpaces
        self.alienSpaces = random.sample(self.openSpaces,k)
        self.row=row
        self.column=column
        self.h = row
        self.w = column
        self.pixel_w = pixel_w
        self.pixel_h = pixel_h
        self.xscale = pixel_w / column
        self.yscale = pixel_h / row
 
        
    def moveAlien(self, screen, x_offset, y_offset):
        
        def checkForOutOfBound(x,y,row,col):
            if x>=row or x<0 or y<0 or y>=col:
                return True
            return False
        
        
        
        
        moves=[[0,1],[1,0],[0,-1],[-1,0],[0,0]]
        random.shuffle(self.alienSpaces)
        aliensCopy=copy.deepcopy(self.alienSpaces)
        for alien in aliensCopy:
            #print(alien)
            move=random.sample(moves,5)
            for move in moves:
                neighbourRow = alien[0]+move[0]
                neighbourCol = alien[1]+move[1]
                res = checkForOutOfBound(neighbourRow,neighbourCol,self.row,self.column)
                if [neighbourRow,neighbourCol] not in self.alienSpaces and res == False and [neighbourRow,neighbourCol] in self.openSpaces:
                    self.alienSpaces.remove(alien)
                    self.alienSpaces.append([neighbourRow,neighbourCol])
                    break
        print("alienspaces",self.alienSpaces)
        for x,y in self.alienSpaces:
            bx = y * self.xscale
            by = x * self.yscale
            pygame.draw.rect(screen, (255, 5, 5), pygame.Rect(bx + x_offset, by + y_offset, self.xscale, self.yscale))
        
    
    