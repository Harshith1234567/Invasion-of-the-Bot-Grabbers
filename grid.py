#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 19:01:01 2023

@author: admin
"""
import pygame
import random 
import copy

class Grid(object):
    
    
    def __init__(self, row, column, pixel_w, pixel_h):
        self.row = row
        self.column = column
        self.h = row
        self.w = column
        self.pixel_w = pixel_w
        self.pixel_h = pixel_h
        self.xscale = pixel_w / column
        self.yscale = pixel_h / row
        self.create()
        
        
    def value(self, x, y):
        index = x + (self.w * y)
        return self.data[index]

    def draw(self, screen, x_offset, y_offset):
        color = (255, 255, 255)
        for x in range(self.w):
            for y in range(self.h):
                bx = x * self.xscale
                by = y * self.yscale
                if self.value(x, y) == 1:
                    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(bx + x_offset, by + y_offset, self.xscale, self.yscale))
       
    def create(self):
        
        def checkForOutOfBound(x,y,row,col):
            if x>=row or x<0 or y<0 or y>=col:
                return True
            return False
        
        def matrixUpdate(grid,randRow,randCol,row,column):
            moves=[[0,1],[1,0],[0,-1],[-1,0]]
            for move in moves:
                neighbourRow = randRow+move[0]
                neighbourCol = randCol+move[1]
                res = checkForOutOfBound(neighbourRow,neighbourCol,row,column)
                if res == False  :
                    grid[neighbourRow][neighbourCol] +=1 
        
        cop=[0]*self.column
        grid=[]
        for i in range(self.row):
            grid.append(copy.deepcopy(cop))
        
        #print(grid)
        
        randRow = random.randint(1, self.row-2)
        randCol = random.randint(1, self.column-2)
        print(randRow,randCol)
        grid[randRow][randCol]=5
        #print(grid)
        matrixUpdate(grid,randRow,randCol,self.row,self.column)

        #print(grid)
        
        
        for i in range((self.row*self.column)//2):
            loop=0
            #print(i)
            while loop<1000:
                loop +=1
                randRow = random.randint(0, self.row-1)
                randCol = random.randint(0, self.column-1)
                #print("printing random",randRow,randCol)
                if grid[randRow][randCol]==1:
                    grid[randRow][randCol]=5
                    matrixUpdate(grid,randRow,randCol,self.row,self.column)  
                    
                    break
        self.data = []
        self.openSpaces=[]
        for p in range(self.row):
            for q in range(self.column):
                if grid[p][q] >= 5:
                    grid[p][q]=1
                    self.openSpaces.append([p,q])
                else:
                    grid[p][q]=0
                
                
                self.data.append(grid[p][q])
        
        self.grid=grid
        print(grid)
        print(self.openSpaces)
        #return grid
