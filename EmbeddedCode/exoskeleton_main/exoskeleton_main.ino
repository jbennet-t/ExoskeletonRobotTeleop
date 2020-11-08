//program to transmit the readout data from one potentiometer 
//via serial to a python program


//arduino serial monitor must be closed to transmit serial data

#include <ResponsiveAnalogRead.h>

//Left side
const int potL1 = A14;  // analog pin used to connect the potentiometer
const int potL2 = A15;
const int potL3 = A16;
const int potL4 = A17;
const int potL5 = A18;
const int potL6 = A19;

int aL1, aL2, aL3, aL4, aL5, aL6;

//Right side 

//const int potR1 = A2;
/*
const int potR2 = A3;
const int potR3 = A6;
const int potR4 = A7;
const int potR5 = A8;
const int potR6 = A9;
*/

ResponsiveAnalogRead analogL1(potL1, true);
ResponsiveAnalogRead analogL2(potL2, true);
ResponsiveAnalogRead analogL3(potL3, true);
ResponsiveAnalogRead analogL4(potL4, true);
ResponsiveAnalogRead analogL5(potL5, true);
ResponsiveAnalogRead analogL6(potL6, true);


//ResponsiveAnalogRead analogR1(potR1, true);
/*
ResponsiveAnalogRead analogR2(potR2, true);
ResponsiveAnalogRead analogR3(potR3, true);
ResponsiveAnalogRead analogR4(potR4, true);
ResponsiveAnalogRead analogR5(potR5, true);
ResponsiveAnalogRead analogR6(potR6, true);
*/
//                   analog2(potpin2, true); etc for more pots
// make a ResponsiveAnalogRead object, pass in the pin, and either true or false depending on if you want sleep enabled
// enabling sleep will cause values to take less time to stop changing and potentially stop changing more abruptly,
// where as disabling sleep will cause values to ease into their correct position smoothly and more accurately


int val1;


void setup()                    
{
  Serial.begin(9600);     

  analogWriteResolution(13);
  analogReadResolution(13);
  
  analogL1.setAnalogResolution(8192);
  analogL2.setAnalogResolution(8192);
  analogL3.setAnalogResolution(8192);
  analogL4.setAnalogResolution(8192);
  analogL5.setAnalogResolution(8192);
  analogL6.setAnalogResolution(8192);

  //analogR1.setAnalogResolution(8192);
}

void loop()                      
{
  analogL1.update(); //updates ResponsiveAnalogRead every loop
  analogL2.update();
  analogL3.update();
  analogL4.update();
  analogL5.update();
  analogL6.update();

  //analogR1.update();

  aL1 = analogL1.getValue();
  aL2 = analogL2.getValue();
  aL3 = analogL3.getValue();
  aL4 = analogL4.getValue();
  aL5 = analogL5.getValue();
  aL6 = analogL6.getValue();

  aL1 = map(aL1, 0, 8191, 0, 179); //maps 13 bit range to 0-180 angle range
  aL2 = map(aL2, 0, 8191, 0, 180); 
  aL3 = map(aL3, 0, 8191, 0, 180); 
  aL4 = map(aL4, 0, 8191, 0, 180); 
  aL5 = map(aL5, 0, 8191, 0, 180); 
  aL6 = map(aL6, 0, 8191, 0, 180); 
 
  
  Serial.print(aL1); Serial.print(",");
  Serial.print(aL2); Serial.print(",");
  Serial.print(aL3); Serial.print(",");
  Serial.print(aL4); Serial.print(",");
  Serial.print(aL5); Serial.print(",");
  Serial.print(aL6); Serial.print(";");
  
  
  //Serial.print(analogR1.getValue());
  
  
  /*
  Serial.print("\t");
  val1 = analog1.getValue();
  val1 = map(val1, 0, 8191, 0, 179);
  Serial.print(val1);

  if(analog1.hasChanged()) {
    Serial.print("\tchanged");
  }
  */
  Serial.println("");

  delay(50);
                          
}


// 120,32,43,52,154,4;55,25,13,123,64,178;....
