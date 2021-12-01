/*
 * IRremote: IRrecvDemo - demonstrates receiving IR codes with IRrecv
 * An IR detector/demodulator must be connected to the input RECV_PIN.
 * Version 0.1 July, 2009
 * Copyright 2009 Ken Shirriff
 * http://arcfn.com
 * miuns = FFE01F
 * add = FFA857
 */
 
#include <IRremote.h>     // IRremote库声明
 
int RECV_PIN = 11;        //定义红外接收器的引脚为11
int rtime = 0;
int ltime = 0;
IRrecv irrecv(RECV_PIN); 
 
decode_results results;
 
void setup()
{
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  Serial.begin(9600);
  irrecv.enableIRIn(); // 启动接收器
}
 
void loop() {
  if (irrecv.decode(&results)) 
  {
    Serial.println(results.value, HEX);
    irrecv.resume(); // 接收下一个值
    if(results.value == 0xFFE01F){
      if(rtime == 1){
        digitalWrite(2,LOW);
        rtime = 0;
        }
      else{
         digitalWrite(2,HIGH);
         rtime = 1;
        }
     
    }
    if(results.value == 0xFFA857){
      if(ltime == 1){
        digitalWrite(3,LOW);
        ltime = 0;
        }
      else{
         digitalWrite(3,HIGH);
         ltime = 1;
        }
    }
    delay(100);
      }
  }
