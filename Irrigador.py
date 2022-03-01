import datetime
import math
import smtplib
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Pinagem
boia_pin = 7 #terra = 9
led_verm_pin = 13 #terra = 14
led_verd_pin = 22 #terra = 20
solo_pin = 32 #terra = 30
bomba_pin = 23 #terra = 25 NA VERDADE É O PINO DO RELÉ
#O positivo do relé deve ser conectado no pino de 3,3V do Raspberry pi

GPIO.setup(boia_pin, GPIO.IN)
GPIO.setup(led_verm_pin, GPIO.OUT)
GPIO.setup(led_verd_pin, GPIO.OUT)
GPIO.setup(solo_pin, GPIO.IN)
GPIO.setup(bomba_pin, GPIO.OUT)

print("Inicializando a irrigação automática, aguarde...")

while True:
    #Guardando a hora local
    now = datetime.datetime.now()
    hora_agora = now.hour
    #print(type(hora_agora))
    print(hora_agora,"hs")
   
    if hora_agora < 8:
        segundos = int(((8 - hora_agora)*3600)+5)
        print(segundos)
        print("Aguardando horário ativo (8-21h)-1")
        time.sleep(segundos)
   
    elif hora_agora >= 22:
        segundos = int((((24 - hora_agora)+8)*3600)+5)
        print(segundos)
        print("Aguardando horário ativo (8-21h)-2")
        time.sleep(segundos)
   
    if GPIO.input(boia_pin) == 0:
        now = datetime.datetime.now()
        print("Reservatório com água", now)
        GPIO.output(led_verd_pin, GPIO.HIGH)
        GPIO.output(led_verm_pin, GPIO.LOW)
        agua = 1
           
        if agua == 1:
            if GPIO.input(solo_pin):
                now = datetime.datetime.now()
                print("Solo seco!!! Ligar a Bomba D'água", now)
                GPIO.output(bomba_pin, 1) #Ligando a Bomba!
                print("BOMBA LIGADA!!!")
               
                time.sleep(20) #Tempo da Bomba ligada
                   
                GPIO.output(bomba_pin, 0)
                print("Bomba desligada... por 6 horas", now)
                time.sleep(21600) #Tempo de espera para recomeçar a irrigação = 2 horas (7200secs) 6 horas (21600SEC)
               
            else:
                now = datetime.datetime.now()
                print("Solo úmido... Bomba desligada")
                GPIO.output(bomba_pin, 0)
                print("BOMBA DESLIGADA...... por 2 horas", now)
                time.sleep(7200) #Tempo de espera para recomeçar a análise do solo = 2 horas, 6 horas
    else:
        now = datetime.datetime.now()
        print("Reservatório vazio! Encher...!!!", now)
        GPIO.output(led_verd_pin, GPIO.LOW)
        GPIO.output(led_verm_pin, GPIO.HIGH)
        agua = 0
         
        time.sleep(21600) #6h Tempo de espera para próximo aviso! 