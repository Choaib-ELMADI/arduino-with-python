#include <cvzone.h>
#define led01 2
#define led02 3
#define led03 4

int LEDs[] = {led01, led02, led03};

SerialData data(1, 1);
int receivedVals[1];

void setup() {
    data.begin();
    for (int i=0; i<3; ++i) {
        pinMode(LEDs[i], OUTPUT);
    }
}

void loop() {
    for (int i=0; i<3; ++i) {
        digitalWrite(LEDs[i], LOW);
    }
    
    data.Get(receivedVals);
    for (int i=0; i<receivedVals[0]; ++i) {
        digitalWrite(LEDs[i], HIGH);
    }
}
