import numpy as np
import matplotlib.pyplot as plt
#1.Чтение файлов
with open("settings.txt", "r") as settings:
    tmp = [float(i) for i in settings.read().split("\n")]
data_array = np.loadtxt("data.txt",dtype=int)

#2.Перевод показаний АЦП в вольты, номеров отсчетов в секунды
volts = np.array(len(data_array))
times = np.linspace(0,len(data_array)*tmp[0], len(data_array))

volts = data_array * float(tmp[1])
for i in range(len(data_array)):
    times[i] = float(i*float(tmp[0]))

#3.Построение графика и сохранение в файл в формате .svg
x = times
y = volts

#4.Настройка цвета и формы линии, размера и цвета маркеров, частоты отображения
fig, ax = plt.subplots()
ax.plot(times, volts,linewidth=2.0, color = "green")
ax.scatter(times[::50], volts[::50],linewidth=2.5, color = "green")
ax.legend(['Основной график', 'Маркеры'])

#5.Задание максимальных и минимальных значений
ax.set_xlim([0, 12])
ax.set_ylim([0, 3])

#6.Подписи осей
ax.set_xlabel('Время, с')
ax.set_ylabel('Напряжение, В')

#7.Название графика
ax.set_title("Процесс заряда и разряда конденсатора в RC-цепочке")


#8.Сетка
ax.minorticks_on()
ax.grid(which = 'major', color = 'k', linewidth = 1, linestyle = "-")
ax.grid(which = 'minor', color = 'k', linewidth = 0.3, linestyle = ":" )

#9.Текст с временем зарядки и разрядки
ax.text(0.9, 0.5, 'Время зарядки 0.0062 с', horizontalalignment='center', verticalalignment='center', transform = ax.transAxes)
ax.text(0.9, 0.45, 'Время разрядки 0.0057 с', horizontalalignment='center', verticalalignment='center', transform = ax.transAxes)
print(volts.argmax()*tmp[0])
print(times[len(times)-1] - volts.argmax()*tmp[0])
fig.savefig("Graph.svg")
plt.show()
