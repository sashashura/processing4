import processing.core.*; import java.applet.*; import java.awt.*; import java.awt.image.*; import java.awt.event.*; import java.io.*; import java.net.*; import java.text.*; import java.util.*; import java.util.zip.*; public class EmbeddingPushPop extends PApplet {/**
 * Embedding Push Pop 
 * by Chris Noessel. 
 * 
 * Embedding pop() and push() within a for() loop. 
 * 
 * Created 9 December 2002
 */

int xgridcount = 4; 
int ygridcount = 4; 
int zgridcount = 4; 
int halfx = xgridcount / 2; 
int halfy = ygridcount / 2; 
int halfz = zgridcount / 2;   
float a = 0.0f;   
float boxsize = 0; 
int gDistance;  
  
public void setup() 
{ 
  size(200, 200, P3D); 
  noStroke(); 
  colorMode(HSB, 100); 
  gDistance = width - width/4;  
} 

public void draw() 
{ 
  background(51);
  
  translate(halfx*gDistance -gDistance, halfy*gDistance -gDistance,-gDistance *10); 
 
  // First number is pauses between timechange, 
  // lower 2nd number = faster speed 
  a += abs(sin(millis()/1500)/500);                                 
  
  for(int i=halfx *-1; i<=halfx; i+=1) { 
    translate(gDistance, 0, 0); 
    rotateX(a*.9f); 
  
    pushMatrix(); 
    for(int j=halfy *-1; j<= halfy; j+=1){ 
      translate(-width/2, gDistance, 0); 
      rotateZ(a*1.1f); 
      pushMatrix(); 
      for(int k=halfz * -1; k<= halfz; k+=1){ 
        translate(0, 0, gDistance); 
        rotateY(a); 
 
        boxsize = 30 + (sin(i*j*k*a) *(gDistance)*1.66f); 
  
        fill(0, 0, 100-boxsize/5.1f);          
        box(boxsize, boxsize, boxsize); 
      } 
     popMatrix(); 
    } 
    popMatrix(); 
  } 
} 
static public void main(String args[]) {   PApplet.main(new String[] { "EmbeddingPushPop" });}}