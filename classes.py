import matplotlib.pyplot as plt
import random as r


class Road:
    def __init__(self, ax):
        self.figure_x = plt.Rectangle((0, 0.40), 1, 0.2, color='grey')
        self.figure_y = plt.Rectangle((0.40, 0), 0.2, 1, color='grey')
        
        self.ax = ax
        self.ax.add_patch(self.figure_x)
        self.ax.add_patch(self.figure_y)


# заранее создаём много машин и каждая может появиться с некоторой вероятностью
class Car:
    def __init__(self, ax, x, y, color='blue'):
        self.rect = plt.Rectangle((x, y), 0.1, 0.07, color=color)
        self.ax = ax
        self.restt = 0
        self.ax.add_patch(self.rect)

    def update(self, v, tr):
        x, y = self.rect.get_xy()
        self.stop = bool(False)
        if v > 0:
            if tr.get_circle_color() == 'green' or x > 0.3:
                x += v
            elif tr.get_circle_color() == 'red' and x < 0.17:
                x += v
            else:
                self.stop = True

        elif v < 0:
            if tr.get_circle_color() == 'green' or x < (1-0.3):
                x += v
            elif tr.get_circle_color() == 'red' and x > (1-0.17):
                x += v
            else:
                self.stop = True

        if x > 1 and r.random() > 0.98:
            x = 0
        if x < 0 and r.random() > 0.98:
            x = 1

        self.rect.set_xy((x, y))
        return self.stop

    def set_animated(self, *args, **kwargs):
        pass


class TrafficLight:
    def __init__(self, ax, id, x=0.1, y=0.1):
        self.circle = plt.Circle((x, y), 0.05, color="green")
        self.time = 0
        self.ax = ax
        self.ax.add_patch(self.circle)
        self.id = id


    def update(self):
        self.time += 0.1
        color1 = ''
        if self.time % 6 < 3:
            color1 = "green"
            self.circle.set_facecolor(color1)
        else:
            color1 = "red"
            self.circle.set_facecolor(color1)

    def get_circle_color(self):
        if round(self.circle.get_facecolor()[1],1) == 0.5:
            color = 'green'
        elif self.circle.get_facecolor()[1] == 1:
            color = 'yellow'
        elif self.circle.get_facecolor()[1] == 0:
            color = 'red'
        # print(circle.get_facecolor())
        return color

    def set_animated(self, *args, **kwargs):
        pass


class Pedestrian:
    def __init__(self, ax, x, y, color='black'):
        self.rect = plt.Rectangle((x, y), 0.04, 0.04, color=color)
        self.ax = ax
        self.ax.add_patch(self.rect)

    def update(self, v, tr):
        x, y = self.rect.get_xy()
        if v > 0:
            if tr.get_circle_color() == 'red' or y > 0.37:
                y += v
            if tr.get_circle_color() == 'green' and y < 0.3:
                y += v
        elif v < 0:
            if tr.get_circle_color() == 'red' or y < (1-0.37):
                y += v
            if tr.get_circle_color() == 'green' and y > (1-0.3):
                y += v
        if y > 1:
            y = 0
        if y < 0:
            y = 1

        self.rect.set_xy((x, y))