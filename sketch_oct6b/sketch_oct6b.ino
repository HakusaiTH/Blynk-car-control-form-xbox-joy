#define BLYNK_TEMPLATE_ID "TMPL6h3lxIOey"
#define BLYNK_TEMPLATE_NAME "rainbowsix"
#define BLYNK_AUTH_TOKEN "ZRiWOcaUHqvET-v0i4KiSw-hwQBqIubT"

#define BLYNK_PRINT Serial

#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>

const int motorPins[] = {12, 14, 4, 5};  // H-Bridge pins: in1, in2, in3, in4

char ssid[] = "FF1_1";
char pass[] = "123456789";

void setup() {
  Serial.begin(115200);
  
  for (int i = 0; i < 4; i++) {
    pinMode(motorPins[i], OUTPUT);
  }

  Blynk.begin(BLYNK_AUTH_TOKEN, ssid, pass);
}

void moveMotors(int in1, int in2, int in3, int in4, const char* direction) {
  Serial.println(direction);
  digitalWrite(motorPins[0], in1);
  digitalWrite(motorPins[1], in2);
  digitalWrite(motorPins[2], in3);
  digitalWrite(motorPins[3], in4);
}

void stopMotors() {
  moveMotors(LOW, LOW, LOW, LOW, "stop");
}

BLYNK_WRITE(V0) { param.asInt() ? moveMotors(HIGH, LOW, HIGH, LOW, "fd") : stopMotors(); } // HIGH, LOW, HIGH, LOW
BLYNK_WRITE(V1) { param.asInt() ? moveMotors(LOW, HIGH, LOW, HIGH, "bk") : stopMotors(); } // LOW, HIGH, LOW, HIGH
BLYNK_WRITE(V2) { param.asInt() ? moveMotors(LOW, HIGH, HIGH, LOW, "tl") : stopMotors(); }
BLYNK_WRITE(V3) { param.asInt() ? moveMotors(HIGH, LOW, LOW, HIGH, "tr") : stopMotors(); }

void loop() {
  Blynk.run();
}
