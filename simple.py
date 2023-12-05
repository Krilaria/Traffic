import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random as r
from classes import Road, Car, TrafficLight, Pedestrian

time = float(0)
rest1 = float(0)
fig, ax = plt.subplots()


road = Road(ax)
tr1 = TrafficLight(ax, 1)

car1 = Car(ax, 0, 0.42, 'blue')
car2 = Car(ax, 0, 0.52, 'red')
p1 = Pedestrian(ax, 0.35, 0.35)

text = ax.text(0.05, 0.9, f' time: {time:.1f}, stop  {round(rest1/(time+00.1), 2)}', transform=ax.transAxes)


def update(frame):
    global time
    global rest1
    car1.update(0.01, tr1)
    car2.update(-0.013, tr1)
    tr1.update()
    p1.update(0.01, tr1)
    text.set_text(f' time: {time:.1f}, stop  {round(rest1/(2*time+00.1), 2)}')
    time += 0.1
    if car1.update(0.01, tr1) == True:
        rest1 += 0.1
    if car2.update(-0.013, tr1) == True:
        rest1 += 0.1




# Получение цвета круга
current_color = tr1.get_circle_color()
print(current_color)

ani = animation.FuncAnimation(fig, update, frames=10, interval=50)

plt.show()
