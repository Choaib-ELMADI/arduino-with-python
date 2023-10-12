#include <cvzone.h>
#define RLed 2
#define YLed 3
#define GLed 4

SerialData data(3, 1); // (number of received values, number of digits in each value)
int receivedVals[3];

void setup() {
    data.begin();
    pinMode(RLed, OUTPUT);
    pinMode(YLed, OUTPUT);
    pinMode(GLed, OUTPUT);
}

void loop() {
    int leds[3] = {RLed, YLed, GLed};
    data.Get(receivedVals);
    for (int i=0; i<3; ++i) {
        digitalWrite(leds[i], receivedVals[i]);
    }
    delay(10);
}
