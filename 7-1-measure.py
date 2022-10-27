import RPi.GPIO as GPIO
import sys
import time
from matplotlib import pyplot
dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17

GPIO.setmode (GPIO.BCM)
GPIO.setup(dac,GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(leds ,GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def adc():
    k = 0
    for i in range(7, -1, -1):
        k += 2**i
        GPIO.output(dac, binary(k))
        time.sleep(0.01)
        if GPIO.input(comp) == 0:
            k -= 2**i
    return k
#перевод в двоичную
def binary(a):
    return [int(elem) for elem in bin(a)[2:].zfill(8)]

try:
    voltage = 0
    count = 0
    result_value = []
    time_start = time.time()

    #зарядка конденсатора
    while voltage < 256*0.97:
        voltage = adc()
        result_value.append(voltage)
        time.sleep(0)
        count += 1
        GPIO.output(leds, binary(voltage))
    
    GPIO.setup(troyka, GPIO.OUT, initial=GPIO.LOW)

    #разрядка конденсатора
    while voltage > 256*0.02:
        voltage = adc()
        result_value.append(voltage)
        time.sleep(0)
        count += 1
        GPIO.output(leds, binary(voltage))

    time_measure = time.time() - time_start
    
    #создание файлов, содержащих данные измерений
    with open ("data.txt", "w") as f:
        for i in result_value:
            f.write(str(i) + '\n')
    with open ("settings.txt", "w") as f:
            f.write(str(1/time_measure/count) + '\n')  
            f.write('0.01289')                           
    print('общая продолжительность эксперимента{}, период одного измерения {}, средняя частота дискретизации {}, шаг квантования АЦП {}'.format(time_measure, time_measure/count, 1/time_measure/count, 0.01289))
    #построение графиков
    y = [i/256*3.3 for i in result_value]
    x = [i*time_measure/count for i in range(len(result_value))]
    pyplot.plot (x,y)
    pyplot.xlabel('время')
    pyplot.ylabel('напряжение')
    pyplot.show()
    
finally:
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    GPIO.cleanup()