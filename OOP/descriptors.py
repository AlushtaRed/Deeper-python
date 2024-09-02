class Worker():
    def __init__(self, hours, rate):
        if hours < 0:
            raise ValueError('Недопустимое значение')
        if rate < 0:
            raise ValueError('Недопустимое значение')
        self.hours = hours
        self.rate = rate

    @property
    def hours(self):
        return self.hours
    @hours.setter
    def hours(self, value):
        if value < 0:
            raise ValueError('Недопустимое значение')
        self.hours = value
    @property
    def rate(self):
        return self.rate
    @rate.setter
    def rate(self, value):
        if value < 0:
            raise ValueError('Недопустимое значение')
        self.rate = value

    def calculation(self):
        return self.rate*self.hours


w = Worker(-10, 100)
print(w.calculation())
w.hours = -10
print(w.calculation())
