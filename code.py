#define echoPin 13
#define trigPin 12

#define led1Pin 7
#define led2Pin 6
#define led3Pin 5
#define led4Pin 4
#define led5Pin 3

long duration, distance;

void setup() {

Serial.begin (9600);
pinMode(trigPin, OUTPUT);
pinMode(echoPin, INPUT);
    pinMode(led1Pin, OUTPUT);
pinMode(led2Pin, OUTPUT);
pinMode(led3Pin, OUTPUT);
pinMode(led4Pin, OUTPUT);
pinMode(led5Pin, OUTPUT);
}

void loop()
{
digitalWrite(trigPin, LOW);
delayMicroseconds(2);
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(echoPin, LOW);
    duration = pulseIn(echoPin, HIGH);
    
    distance = duration/40;
    
    
    if(distance<40)
        {
        digitalWrite(led1Pin, 150);
    }
    else
        {
        digitalWrite(led1Pin, 0);
    }
    if(distance<30)
        {
        digitalWrite(led2Pin, 150);
    }
    else
        {
        digitalWrite(led2Pin, 0);
    }
    
    if(distance<20)
        {
        digitalWrite(led3Pin, 150);
    }
    else
        {
        digitalWrite(led3Pin, 0);
    }
    
    if(distance<15)
        {
        digitalWrite(led4Pin, 150);
    }
    else
        {
        digitalWrite(led4Pin, 0);
    }
    
    if(distance<10)
        {
        digitalWrite(led5Pin, 150);
    }
    else
        {
        digitalWrite(led5Pin, 0);
}

}
