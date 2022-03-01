# Irrigador
Programa em Python de comando de automação de irrigador com Raspberry pi zero.

Hardware:
Raspberry pi zero
Bomba d'água 5V
Módulo Rele 5V Optoacoplador
Bóia nível de água 3V
Sensor de umidade do solo

Descrição:
O Irrigador só fica ativo entre às 8h e 20h. Durante este período, ele verifica o nível de água do reservatório (nível aceitável = luz verde) e a umidade do solo. 
Caso o mesmo esteja seco, ele liga o rele e consequentemente a bomba d'água por 20 segundos. Após isso, ele espera 6h para verificar novamente o nível de água do reservatório e
a umidade do solo. Caso este solo esteja úmido, o programa espera 2h para verificar novamente. Se o nível de água estiver baixo, ele desliga o led verde e acende o vermelho,
além de pausar o programa até que o operador restabeleça o nível de água do reservatório.
