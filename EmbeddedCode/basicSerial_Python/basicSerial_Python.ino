// Program for basic communication between microcontroller and python
// pair with basicSerial_Python arduino program
// reference: https://makersportal.com/blog/2018/2/25/python-datalogger-reading-the-serial-output-from-arduino-to-analyze-data-using-pyserial
// reference: https://pyserial.readthedocs.io/en/latest/shortintro.html#

//arduino serial monitor must be closed to transmit serial data

void setup()                    
{
  Serial.begin(9600);           
  
}

void loop()                      
{
int count = 0;
  for(int i = 0; i < 100000; i++){
    Serial.println(count);
    count++;
    delay(50);  
  }
                          
}
