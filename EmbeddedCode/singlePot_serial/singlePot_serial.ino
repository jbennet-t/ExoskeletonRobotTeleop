//program to transmit the readout data from one potentiometer 
//via serial to a python program




//arduino serial monitor must be closed to transmit serial data

#include <ResponsiveAnalogRead.h>

const int potpin1 = A2;  // analog pin used to connect the potentiometer

ResponsiveAnalogRead analog1(potpin1, true);
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
  
  analog1.setAnalogResolution(8192);
}

void loop()                      
{
  analog1.update(); //updates ResponsiveAnalogRead every loop
  
  Serial.print(analog1.getValue());
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
