#include "ofApp.h"
#include "dot.h"
int imgw;
int imgh;
int samplelength;
std::vector<int> sample;
std::vector<dot> dots;
int scl = 5;

//--------------------------------------------------------------
void ofApp::setup(){
    myImage.load("bbb.jpg");//setup path
    myImage.setImageType(OF_IMAGE_COLOR);//setup the  color mode
    ofLoadImage(pxdata, "bbb.jpg");//original pixel
    ofLoadImage(pxempty, "bbb.jpg");//empty pixel, but i don't know why i can't just create a empty pixels
    imgw = myImage.getWidth();//width
    imgh = myImage.getHeight();//height
    int precision = 2;//decide how many pixels in the picture
    samplelength = imgw * imgh / precision; // the sampling length
    for(int i = 0; i < samplelength; i++){//sampling process this array is for draw
        sample.push_back(int(ofRandom(imgh*imgw)));//pick pixel randomly

    }

    for(int i = 0; i<imgh;i++){
        for(int j = 0; j<imgw;j++){
            dots.push_back(dot());
            dots[imgw*i+j].setup(i, j, scl);
            std::cout<<dots[imgw*i+j].edge<<endl;
            //现在我们有所有的像素点都变成dot类了，但是这时候只有xy坐标数值没有rgb
        }
    }
}

//--------------------------------------------------------------
void ofApp::update(){

}

//--------------------------------------------------------------
void ofApp::draw(){
    if(ofGetMousePressed()){
                    for(int i = 0; i< imgh;i++){
                        for(int j = 0; j < imgw; j++){
                                dots[(imgw*i+j)].checkchange();
                            }
                        }
        
    }
    pxempty.allocate(imgw, imgh, OF_IMAGE_COLOR);
    pxempty.setColor(ofColor::white);//turn all the pixels into white. now the pxempty is empty.
    for(int i = 0; i < samplelength; i ++){ //push original data into the pxempty.
        int index = sample[i];
        dots[index].posupdate();//update the pos to the pxempty
        dots[index].edges(imgw, imgh);//limit the pos
        int x = dots[index].pos.x;
        int y = dots[index].pos.y;
        int cx = dots[index].cx;
        int cy = dots[index].cy;
        pxempty.getData()[(x*imgw+y)*3] = pxdata.getData()[(cx*imgw+cy)*3];
        pxempty.getData()[(x*imgw+y)*3+1] = pxdata.getData()[(cx*imgw+cy)*3+1];
        pxempty.getData()[(x*imgw+y)*3+2] = pxdata.getData()[(cx*imgw+cy)*3+2];

    }

//    for(int i = 0; i < imgh*imgw; i ++){ //itlooksugly
//        int index = i;
//        dots[index].posupdate();//update the pos to the pxempty
//        dots[index].edges(imgw, imgh);//limit the pos
//        int x = dots[index].pos.x;
//        int y = dots[index].pos.y;
//        int cx = dots[index].cx;
//        int cy = dots[index].cy;
//        pxempty.getData()[(x*imgw+y)*3] = pxdata.getData()[(cx*imgw+cy)*3];
//        pxempty.getData()[(x*imgw+y)*3+1] = pxdata.getData()[(cx*imgw+cy)*3+1];
//        pxempty.getData()[(x*imgw+y)*3+2] = pxdata.getData()[(cx*imgw+cy)*3+2];
//
//    }
    
    
    texture.loadData(pxempty);//push the data to the texture
    texture.draw(0, 0);//this is like the putimagedata



}

//--------------------------------------------------------------
void ofApp::keyPressed(int key){
}

//--------------------------------------------------------------
void ofApp::keyReleased(int key){

}

//--------------------------------------------------------------
void ofApp::mouseMoved(int x, int y ){

}

//--------------------------------------------------------------
void ofApp::mouseDragged(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mousePressed(int x, int y, int button){

    
}

//--------------------------------------------------------------
void ofApp::mouseReleased(int x, int y, int button){

}



//--------------------------------------------------------------
void ofApp::mouseEntered(int x, int y){

}

//--------------------------------------------------------------
void ofApp::mouseExited(int x, int y){

}

//--------------------------------------------------------------
void ofApp::windowResized(int w, int h){

}

//--------------------------------------------------------------
void ofApp::gotMessage(ofMessage msg){

}

//--------------------------------------------------------------
void ofApp::dragEvent(ofDragInfo dragInfo){ 

}
