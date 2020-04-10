//
//  dot.cpp
//  mySketch
//
//  Created by waihin_chan on 2020/1/30.
//

#include <stdio.h>
#include "dot.h"


void dot::setup(int _x, int _y,int _scl){
    x = _x;//positionx
    y = _y;//positiony
    cx = _x;
    cy = _y;//not necessary
    scl = _scl;//scale
    acc.set(0,0);
    speed.set(0, 0);
    pos.set(x,y);
    direction.set(0,0);
    maxspeed = 1;
    edge =10;
}

void dot::posupdate(){
    acc+=direction;
    speed+=acc;
    speed.limit(maxspeed);
    pos+=speed;
    acc*=0;
}

void dot::checkchange(){
    if(abs((ofGetMouseX()-y))<scl && abs(ofGetMouseY()-x)<scl){
        direction.set(ofGetMouseY()-ofGetPreviousMouseY(),ofGetMouseX()-ofGetPreviousMouseX());//count the destination
    }
}
void dot::edges(int width,int height){
    if(abs(pos.x-x)>edge || abs(pos.y-y)>edge || pos.x<0 || pos.y<0 || pos.x>height || pos.y>width){
        pos.set(x,y);//go back to the original position
    }
}

