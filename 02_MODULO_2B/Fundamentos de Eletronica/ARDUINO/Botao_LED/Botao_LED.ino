int pinBotao = 2;
int estadoBotao = 0;

void setup()
{

pinMode(pinBotao, INPUT);
pinMode (3, OUTPUT);

}

void loop()
{
estadoBotao = digitalRead(pinBotao);
  
  if(estadoBotao == HIGH) {
    digitalWrite (3, HIGH); 
  }
  else{
    digitalWrite (3, LOW);
    }
}
