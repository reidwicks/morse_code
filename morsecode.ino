/*
  morsecode

  Based on the "blink" application that comes with the Arduino IDE
  
*/

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
}


// the loop function runs over and over again forever
void loop() {
  // 0 is a dot
  // 1 is a dash
  // 2 is a space between letters
  // 3 is a space between words
  long dotDash[] = {0,0,0,0,2,0,2,0,1,0,0,2,0,1,0,0,3,0,1,1,2,1,1,1,2,0,1,0,2,0,1,0,0,2,1,0,0};
  // copy/paste output from convert_to_morse program and paste in line above
  delay(600);
  for (int item : dotDash){
      if (item == 0){
        digitalWrite(LED_BUILTIN, HIGH);
        delay(100);
        digitalWrite(LED_BUILTIN, LOW);
        delay(100);
      }
      else if (item == 1){
        digitalWrite(LED_BUILTIN, HIGH);
        delay(300);
        digitalWrite(LED_BUILTIN, LOW);
        delay(100);
      }
      else if (item == 2){
        delay(200);
      }
      else if(item == 3){
        delay(600);
      }
  }
}
