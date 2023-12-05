import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Создаем фигуру и оси
fig, ax = plt.subplots()

# Инициализация прямоугольника
rectangle = plt.Rectangle((0, 0), 0.1, 0.1, fc='green')
ax.add_patch(rectangle)

# Устанавливаем пределы осей
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Функция для инициализации анимации
def init():
    return rectangle,

# Функция для обновления каждого кадра
def update(frame):
    x, y = rectangle.get_xy()
    rectangle.set_xy((x + 0.01, y))
    return rectangle,

# Создаем анимацию
ani = animation.FuncAnimation(fig, update, frames=100, init_func=init, blit=True)

print('start')

# Показываем анимацию
plt.show()
