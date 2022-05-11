import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro-')
# plt.axis([0, 6, 0, 20])
# plt.show()
#
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r')
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'o')
#
# plt.axis([0, 6, 0, 20])
# plt.show()

# t = np.arange(0., 5., 0.2)
#
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.legend(labels=['liniowa', 'kwadratowa', 'szescienna'])
# plt.show()

# x = np.linspace(0, 2, 100)
#
# plt.plot(x, x, label="liniowa")
# plt.plot(x, x**2, label="kwadratowa")
# plt.plot(x, x**3, label="szescienna")
#
# plt.xlabel('etykieta x')
# plt.ylabel('etykieta y')
#
# plt.title("prosty wykres")
#
# plt.legend()
# plt.savefig('wykres matplot.png')
#
# plt.show()
# im1 = Image.open('wykres matplot.png')
# im1 = im1.convert('RGB')
# im1.save('nowy.jpg')

# x = np.arange(0, 10, 0.1)
# s = np.sin(x)
# plt.plot(x, s, label="sin(x)")
#
# plt.xlabel('x')
# plt.ylabel('sin(x)')
#
# plt.title('Wykres sin(x)')
#
# plt.legend()
# plt.show()

# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100
#
# print(f"a={data['a'][0]}, b={data['b'][0]}, c={data['c'][0]}, d={data['d'][0]}")
# plt.scatter('a', 'b', c='c', s='d', data=data)
# plt.xlabel('wartosc a')
# plt.ylabel('wartosc b')
# plt.show()

# x1 = np.arange(0, 2, 0.02)
# x2 = np.arange(0, 2, 0.02)
#
# y1 = np.sin(2 * np.pi * x1)
# y2 = np.cos(2 * np.pi * x2)
#
# plt.subplot(2, 1, 1)
# plt.plot(x1, y1, '-')
# plt.title('wykres sin(x)')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
#
# ax=plt.subplot(2, 1, 2)
# plt.plot(x2, y2, 'r-')
#
# plt.xlabel('x')
# plt.ylabel('cos(x)')
# plt.title('wykres cos(x)')
# plt.subplots_adjust(hspace=0.5)
# plt.show()

# x1 = np.arange(0.0, 2.0, 0.02)
# x2 = np.arange(0.0, 2.0, 0.02)
# y1 = np.sin(2 * np.pi * x1)
# y2 = np.cos(2 * np.pi * x2)
#
# fig, axs = plt.subplots(3, 2, )
#
# axs[0, 0].plot(x1, y1, '-')
# axs[0, 0].set_title('wykres sin(x)')
# axs[0, 0].set_xlabel('x')
# axs[0, 0].set_ylabel('sin(x)')
#
# axs[1, 1].plot(x2, y2, 'r-')
# axs[1, 1].set_title('wykres cos(x)')
# axs[1, 1].set_xlabel('x')
# axs[1, 1].set_ylabel('cos(x)')
#
# axs[2, 0].plot(x2, y2, 'r-')
# axs[2, 0].set_title('wykres cos(x)')
# axs[2, 0].set_xlabel('x')
# axs[2, 0].set_ylabel('cos(x)')
#
# fig.delaxes(axs[0, 1])
# fig.delaxes(axs[1, 0])
# fig.delaxes(axs[2, 1])
# plt.show()

# ZAD 1
# x = np.arange(1, 20, 2.5)
# s = 1/x
# plt.plot(x, s, label="1/x")
#
# plt.xlabel('f(x)')
# plt.ylabel('x')
#
# plt.title('Wykres funkcji f(x) dla x[1, 20]')
#
# plt.legend()
# plt.show()

# ZAD 2

# x = np.arange(1, 20, 2.5)
# s = 1/x
# plt.plot(x, s, 'g^--', label="1/x")
#
# plt.xlabel('f(x)')
# plt.ylabel('x')
#
# plt.title('Wykres funkcji f(x) dla x[1, 20]')
#
# plt.legend()
# plt.show()


# ZAD 3 ale na oddzielnych wykresach

# x1 = np.arange(0, 30, 0.1)
# x2 = np.arange(0, 30, 0.1)
#
# y1 = np.sin(x1)
# y2 = np.cos(x2)
#
# plt.subplot(2, 1, 1)
# plt.plot(x1, y1, label='sin(x)')
# plt.title('wykres sin(x)')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.legend()
#
# ax = plt.subplot(2, 1, 2)
# plt.plot(x2, y2, label='cos(x)')
#
# plt.xlabel('x')
# plt.ylabel('cos(x)')
# plt.title('wykres cos(x)')
# plt.subplots_adjust(hspace=0.5)
# plt.legend()
# plt.show()

# ZAD 3 ale na tym samym wykresie

# x = np.arange(0, 30, 0.1)
# y1 = np.sin(x)
# y2 = np.cos(x)
# plt.plot(x, y1, x, y2)
# plt.legend(labels=['sin(x)', 'cos(x)'])
# plt.show()

# ZAD 5

# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
# print(df)
#
# x1 = np.arange(0, 30, 0.1)
# x2 = np.arange(0, 30, 0.1)
# x3 = np.arange()
#
# y1 = np.sin(x1)
# y2 = np.cos(x2)
# y3 =
#
# plt.subplot(2, 1, 1)
# plt.plot(x1, y1, label='sin(x)')
# plt.title('wykres sin(x)')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.legend()
#
# ax = plt.subplot(2, 1, 2)
# plt.plot(x2, y2, label='cos(x)')
#
# plt.xlabel('x')
# plt.ylabel('cos(x)')
# plt.title('wykres cos(x)')
# plt.subplots_adjust(hspace=0.5)
# plt.legend()
# plt.show()
