// Program for basic communication between microcontroller and python
// pair with basicSerial_Python arduino program
// reference: https://makersportal.com/blog/2018/2/25/python-datalogger-reading-the-serial-output-from-arduino-to-analyze-data-using-pyserial
// reference: https://pyserial.readthedocs.io/en/latest/shortintro.html#

//arduino serial monitor must be closed to transmit serial data

#include <ResponsiveAnalogRead.h>
#include <String.h> 

const int potpin1 = A2;  // analog pin used to connect the potentiometer
//const int potpin2 = A2;
//const int potpin3 = A4;

ResponsiveAnalogRead analog1(potpin1, true);
//ResponsiveAnalogRead analog2(potpin2, true);
//ResponsiveAnalogRead analog3(potpin3, true);

void setup()                    
{
  Serial.begin(9600);           
}

void loop()                      
{
  //analogWriteResolution(13);
  //analogReadResolution(13);

  analog1.setAnalogResolution(8192);
  
  analog1.update(); //updates ResponsiveAnalogRead every loop
  //analog2.update();
  //analog3.update();

  int a1 = analog1.getValue(); //updates ResponsiveAnalogRead every loop
  //int a2 = analog2.getValue();
  //int a3 = analog3.getValue();

  char buff[80];
  //sprintf(buff,"%d,%d,%d",a1,a2,a3);
  //sprintf(buff,"%d",a1);
  //string formatted_buff = str(buff);
  Serial.println(a1);
  //Serial.println(analog1.getValue());
  

                          
}
