//program to transmit the readout data from one potentiometer 
//via serial to a python program

//arduino serial monitor must be closed to transmit serial data

#include <ResponsiveAnalogRead.h>

//Left side instantiation
const float potL1 = A14;  // analog pin used to connect the potentiometer
const float potL2 = A15;
const float potL3 = A16;
const float potL4 = A17;
const float potL5 = A18;
const float potL6 = A19;

//Right side instantiation
const int potR1 = A2;
const int potR2 = A3;
const int potR3 = A6;
const int potR4 = A7;
const int potR5 = A8;
const int potR6 = A9;

float aL1, aL2, aL3, aL4, aL5, aL6;
float aR1, aR2, aR3, aR4, aR5, aR6; //floats for later mapping

ResponsiveAnalogRead analogL1(potL1, true);
ResponsiveAnalogRead analogL2(potL2, true);
ResponsiveAnalogRead analogL3(potL3, true);
ResponsiveAnalogRead analogL4(potL4, true);
ResponsiveAnalogRead analogL5(potL5, true);
ResponsiveAnalogRead analogL6(potL6, true);

ResponsiveAnalogRead analogR1(potR1, true);
ResponsiveAnalogRead analogR2(potR2, true);
ResponsiveAnalogRead analogR3(potR3, true);
ResponsiveAnalogRead analogR4(potR4, true);
ResponsiveAnalogRead analogR5(potR5, true);
ResponsiveAnalogRead analogR6(potR6, true);

// make a ResponsiveAnalogRead object, pass in the pin, and either true or false depending on if you want sleep enabled
// enabling sleep will cause values to take less time to stop changing and potentially stop changing more abruptly,
// where as disabling sleep will cause values to ease into their correct position smoothly and more accurately


int val1;

void setup()                    
{
  Serial.begin(9600);     

  analogWriteResolution(13);//setting analog write/read resolution to 13 bits
  analogReadResolution(13);
  
  analogL1.setAnalogResolution(8192); //setting 13 bit resolution for responsiveanalogread objects
  analogL2.setAnalogResolution(8192);
  analogL3.setAnalogResolution(8192);
  analogL4.setAnalogResolution(8192);
  analogL5.setAnalogResolution(8192);
  analogL6.setAnalogResolution(8192);

  analogR1.setAnalogResolution(8192);
  analogR2.setAnalogResolution(8192);
  analogR3.setAnalogResolution(8192);
  analogR4.setAnalogResolution(8192);
  analogR5.setAnalogResolution(8192);
  analogR6.setAnalogResolution(8192);
}

void loop()                      
{
  analogL1.update(); //updates ResponsiveAnalogRead every loop
  analogL2.update();
  analogL3.update();
  analogL4.update();
  analogL5.update();
  analogL6.update();

  analogR1.update();
  analogR2.update();
  analogR3.update();
  analogR4.update();
  analogR5.update();
  analogR6.update();

  aL1 = analogL1.getValue(); //passing ResponsiveAnalogRead object vals to long variable
  aL2 = analogL2.getValue();
  aL3 = analogL3.getValue();
  aL4 = analogL4.getValue();
  aL5 = analogL5.getValue();
  aL6 = analogL6.getValue();

  aR1 = analogR1.getValue();
  aR2 = analogR2.getValue();
  aR3 = analogR3.getValue();
  aR4 = analogR4.getValue();
  aR5 = analogR5.getValue();
  aR6 = analogR6.getValue();

/*
  Serial.print(aL1); Serial.print(",");
  Serial.print(aL2); Serial.print(",");
  Serial.print(aL4); Serial.print(",");
  Serial.print(aL3); Serial.print(",");
  Serial.print(aL5); Serial.print(",");
  Serial.print("0"); Serial.print(","); //not yet used
  Serial.print(aR1); Serial.print(",");
  Serial.print(aR2); Serial.print(",");
  Serial.print(aR4); Serial.print(",");
  Serial.print(aR3); Serial.print(",");
  Serial.print(aR5); Serial.print(",");
  Serial.print("0"); //Serial.print(","); //not yet used
  */


  //mapping 13 bit ranges to radian ranges for Nao robots prior to pass over serial
  aL1 = map(aL1, 1100, 6570, -2.0857, 2.0857) + 1.20; //maps 13 bit range to radian range for shoulder pitch, pots go from 0-8191
  aL2 = map(aL2, 4690, 7190, -0.3142, 1.3265); //shoulder roll
  aL3 = map(aL3, 1602, 6995, -2.0857, 2.0857)* 1; //elbow yaw
  aL4 = map(aL4, 1430, 6570, -1.5446, -0.0349)* 1; //elbow roll
  aL5 = map(aL5, 1730, 7220, -1.8238, 1.8238); //wrist yaw
  aL6 = map(aL6, 0, 8191, -2.0857, 2.0857); //wrist roll - not used (for now)

  aR1 = map(aR1, 1240, 6609, -2.0857, 2.0857)*-1 + 1.20; //maps 13 bit range to radian range for shoulder pitch
  aR2 = map(aR2, 4407, 6721, -0.3142, 1.3265)* -1; //shoulder roll
  aR3 = map(aR3, 1770, 6780, -2.0857, 2.0857)* -1; //elbow yaw
  aR4 = map(aR4, 1947, 6553, -1.5446, -0.0349)* -1; //elbow roll
  aR5 = map(aR5, 1190, 6631, -1.8238, 1.8238)* -1; //wrist yaw
  aR6 = map(aR6, 0, 8191, -2.0857, 2.0857); //wrist roll - not used (for now)

/*
  Serial.print("0"); Serial.print(",");
  Serial.print("0"); Serial.print(",");
  Serial.print("-1"); Serial.print(",");
  Serial.print("0"); Serial.print(",");
  Serial.print("0"); Serial.print(",");
  Serial.print("0"); Serial.print(",");
  Serial.print(aL2); Serial.print(",");
  Serial.print(aL1); Serial.print(",");
  Serial.print(aL3); Serial.print(",");
  Serial.print(aL4); Serial.print(",");
  Serial.print(aL5); Serial.print(",");
  Serial.print("0"); //Serial.print(",");
 */


 //passing comma seperated vals to serial for transmission to Python program
  Serial.print(aL1); Serial.print(",");
  Serial.print(aL2); Serial.print(",");
  Serial.print(aL3); Serial.print(",");
  Serial.print(aL4); Serial.print(",");
  Serial.print(aL5); Serial.print(",");
  Serial.print("0"); Serial.print(","); //not yet used
  Serial.print(aR1); Serial.print(",");
  Serial.print(aR2); Serial.print(",");
  Serial.print(aR3); Serial.print(",");
  Serial.print(aR4); Serial.print(",");
  Serial.print(aR5); Serial.print(",");
  Serial.print("0"); //Serial.print(","); //not yet used
 
  
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
