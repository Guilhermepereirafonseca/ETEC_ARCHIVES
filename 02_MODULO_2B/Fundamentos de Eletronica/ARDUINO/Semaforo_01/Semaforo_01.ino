                    /* VARIAVEIS */

int ledVermelho = 2;
int ledVerde = 4;
int ledAmarelo = 3; 

void setup() {
  /* DECLARANDO ELAS COM A FUNÇÃO 'pinMode', colocando nome das mesmas */
  pinMode (ledVermelho, OUTPUT);
  pinMode (ledVerde, OUTPUT);
  pinMode (ledAmarelo, OUTPUT);
  }

void loop() {
  /* NOSSO PROJETO - 29/02/24 */
  digitalWrite (ledVerde, HIGH);
  delay(4000);
  digitalWrite (ledVerde, LOW);
  digitalWrite (ledAmarelo, HIGH);
  delay (3000);
  digitalWrite (ledAmarelo, LOW);
  digitalWrite (ledVermelho, HIGH);
  delay(5000);
  digitalWrite (ledVermelho, LOW);
  }
