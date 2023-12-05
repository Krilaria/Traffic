import matplotlib.pyplot as plt
import matplotlib.animation as animation

car1_x = float(0)
time = float(0)
colors = ["green", 'yellow', 'red']

# Создаем фигуру и оси
fig, ax = plt.subplots()

# Инициализация дороги и машины
road = plt.Rectangle((0, 0.40), 1, 0.2, color='grey')
car1 = plt.Rectangle((0, 0.45), 0.1, 0.07, color='blue')
light1 = plt.Circle((0.5, 0.1),0.05, color="green")
cross1 = plt.Rectangle((0.48, 0.40), 0.04, 0.2, color='black')

ax.add_patch(road)
ax.add_patch(car1)
ax.add_patch(light1)
ax.add_patch(cross1)


# Текстовое поле для отображения значения car1_x
text = ax.text(0.4, 0.9, f'Car1_x: {car1_x:.2f}', transform=ax.transAxes)

# Устанавливаем пределы осей
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Функция для инициализации анимации
def init():
    return car1, text, light1


# Функция для обновления каждого кадра
def update(frame):
    global car1_x
    global time
    global light1
    col = ''
    x, y = car1.get_xy()
    if car1_x < 0.35 and light1.get_fc()[1] == 0:
        car1_x += 0.01
    if round(light1.get_fc()[1],1) == 0.5 or car1_x > 0.5:
        car1_x += 0.01
    if time > 0 and time % 6 < 3:
        light1.set_facecolor("green")
    else:
        light1.set_facecolor("red")

    time += 0.1
    if car1_x > 1:
        car1_x = 0

    car1.set_xy((car1_x, y))

    # Обновляем значение текстового поля в зависимости от цвета светофора
    if light1.get_fc()[1] == 1:
        col ='yellow'
    elif light1.get_fc()[1] == 0:
        col ='red'
    elif round(light1.get_fc()[1],1) == 0.5:
        col ='green'
    # Обновляем значение текстового поля
    text.set_text(f'Car1_x: {car1_x:.2f} time: {time:.1f} color: {col}')
    return car1, light1, text

# Создаем анимацию
ani = animation.FuncAnimation(fig, update, frames=10, init_func=init, blit=True, interval=50)

print('start')

# Показываем анимацию
plt.show()

# yellow 1 1 0 1
# red 1 0 0 1
# green 0 0.5019607843137255 0 1