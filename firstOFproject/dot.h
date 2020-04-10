//
//  dot.h
//  mySketch
//
//  Created by waihin_chan on 2020/1/30.
//
#include "ofMain.h"
#ifndef dot_h
#define dot_h

class dot{
public:
    //varibale, init the data at setup, not here
    int x; //pos x
    int y; //pos y
    int cx;
    int cy;
    int scl; //scale
    ofVec2f speed;//speed
    ofVec2f acc;
    ofVec2f pos; //position
    ofVec2f direction;//direction
    ofVec2f destination;//destination
    int maxspeed;
    int edge;


    //function
    void setup(int _x, int _y,int _scl);//constructor
    void posupdate();//change the postion
    void checkchange();//use the mouse position to change the direction
    void edges(int width, int height);//limit the edge by the width&height


};

#endif /* dot_h */

