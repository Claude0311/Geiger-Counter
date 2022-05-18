#include <Event.h>
#include <Timer.h>

Timer t;
int report_min = 10;
int counts = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(2,INPUT);
  attachInterrupt(digitalPinToInterrupt(2),trigger,RISING);
  t.every(60000*report_min,report_event);
  Serial.println("Hello Muon World!");
}

void loop() {
  // put your main code here, to run repeatedly:
//  Serial.print(".");
  delay(6000);
  t.update();
}

void report_event() {
//  Serial.println("");
//  Serial.print("Trg ");
  Serial.println(counts);
  counts = 0;
}

void trigger(){
  counts = counts + 1;
//  Serial.print("total counts:");
//  Serial.println(counts);
}
