#define THINGER_SERIAL_DEBUG

#include <ThingerESP8266.h>
#include "secret.h"

#include <Event.h>
#include <Timer.h>
int counts = 0;
void ICACHE_RAM_ATTR mytrigger();

Timer t;
int report_min = 10;

ThingerESP8266 thing(USERNAME, DEVICE_ID, DEVICE_CREDENTIAL);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  thing.add_wifi(SSID, SSID_PASSWORD);
  pinMode(LED_BUILTIN, OUTPUT);
  thing["led"] << digitalPin(LED_BUILTIN);
  
  pinMode(4,INPUT);
  attachInterrupt(digitalPinToInterrupt(4),mytrigger,RISING);
  t.every(60000*report_min,report_event);

  thing["Count"] >> [](pson &out){ 
    out["count"] = counts;
  };
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print(".");
  for(int i=0; i<6; i=i+1){
    thing.handle();
    delay(1000);
  }
  t.update();
}

void mytrigger(){
  Serial.println("count++");
  counts = counts + 1;
}

void report_event() {
  Serial.println("");
  Serial.print("count = ");
  Serial.println(counts);
  thing.write_bucket(BucketId, "Count");
  counts = 0;
}
