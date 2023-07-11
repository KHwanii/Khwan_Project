#include "Led.h" // <~~.h>? μ§?? ? ?Ό?΄λΈλ¬λ¦¬μ? μ°ΎκΈ° 
                      // "~~.h"? ??¬ ?? ? λ¦¬μ? μ°Ύκ³ , κ·Έλ€? μ§??  ?μΉμ? μ°ΎκΈ°

Led::Led(int pin) : pin(pin) { // ?? :: λ©€λ²
  // this->pin = pin;
  pinMode(pin, OUTPUT);
}

void Led::on() {
  digitalWrite(pin, HIGH);
}

void Led::off() {
  digitalWrite(pin, LOW);
}

void Led::setValue(int value) {
  digitalWrite(pin, value);
}

int Led::toggle() {
  int v = !digitalRead(pin);
  digitalWrite(pin, v);
  return v;
}
