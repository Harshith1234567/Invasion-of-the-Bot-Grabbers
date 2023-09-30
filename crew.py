#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random,pygame 


class Crew(object):
    def __init__(self,openSpaces,row,column, pixel_w, pixel_h):
        
       
        self.openSpaces=openSpaces
        
        
        
        self.xscale = pixel_w / column
        self.yscale = pixel_h / row
        
    def new(self, screen, x_offset, y_offset):
        crewNew=random.sample(self.openSpaces,1)[0]
        #self.x=crewNew[0] * self.xs
        #self.y=crewNew[1] * self.ys
        print(crewNew)
        bx = crewNew[1] * self.xscale
        by = crewNew[0] * self.yscale
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(bx + x_offset, by + y_offset, self.xscale, self.yscale))
        
        
        