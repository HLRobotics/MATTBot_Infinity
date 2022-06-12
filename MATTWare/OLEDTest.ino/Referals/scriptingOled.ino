#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
 
#define OLED_RESET -1
Adafruit_SSD1306 display(128, 64, &Wire, OLED_RESET);

void setup(){
    
display.begin(SSD1306_SWITCHCAPVCC, 0x3C); //or 0x3D// need to identify address using code
Serial.begin(9600);  
String action;
display.clearDisplay();
display.setTextSize(2);
display.setTextColor(WHITE);
display.setCursor(0, 10); 
display.println("MATTBot");
display.println("2021");
display.display();
}

void loop() 
{ 

  

  

}
