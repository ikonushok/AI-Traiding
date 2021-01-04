import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

# Данные для построения графика
close = [10, 12, 11, 13, 12, 15, 13, 14, 12, 13, 11, 12, 10]
x = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# Построение графика plot
plt.scatter(8, close[7], label='trend= 2')
plt.scatter(10, close[9], label='trend= 4')
plt.plot(x, close, label='Close')
plt.title('Запаздывание сигналов от нейронки\nпри торговле по предсказанию тренда')
plt.legend()
plt.show()

print('Рост = 1', '\nПлато = 0', '\nПадение = -1\n')

def signal(x):
    if x > 0: signal = 1
    elif x < 0: signal = -1
    elif x == 0: signal = 0
    return signal

def trend(n, close = close):
    arr_trend = []
    for i in range(0, len(close)):
        if i < n: arr_trend.append(0) # пишем 0, если i меньше тренда
        else:
            x = close[i] - close[i - n] # находим разницу между close в начале и конце тренда
            arr_trend.append(signal(x))
    return arr_trend

# Попробуем определить тренд попарными разностями
print('Тренд по разностям (Close[i] - Close[i-1]): ', trend(1))

# Определим тренд из 2х баров
print('Тренд по разностям (Close[i] - Close[i-2]): ', trend(2))

# Определим тренд из 3х и 4х баров
print('Тренд по разностям (Close[i] - Close[i-3]): ', trend(3))
print('Тренд по разностям (Close[i] - Close[i-4]): ', trend(4))
print('Вывод: Важно правильно подобрать тренд!')