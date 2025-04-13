from sys import *
import matplotlib.pyplot as plt
from tkinter import*
from manager_ui import Window
import constants

win = Window()
win.create_ui()
win.fill_entry_for_test()
win.mainloop()


import matplotlib.pyplot as plt


# СПИСКИ В СПИСКАХ - МЕСЯЦЫ
# СЮДА БУДЕМ ПЕРЕНОСИТЬ ЗНАЧЕНИЯ ПЕРЕМЕННЫХ
# ИЗ ДРУГОГО СПИСКА
january = [0]
february = [0]
march = [0]
april = [0]
may = [0]
june = [0]
july = [0]
august = [0]
september = [0]
october = [0]
november = [0]
december = [0]
#вывод списка в косоль
mount = [january,february,march,april,may,june,july,august,september,october,november,december]
print(mount)
#####################################
#
#var = [T_KR_K,T_TR_K,T_TO_3_K,T_KR_K1,T_TR_K1,T_TO_3_K1,DT_T_KR,DT_T_TR,DT_T_TO_3,MTZ2_T_KR,MTZ2_T_TR,MTZ2_T_TO_3,MZT_T_KR,MZT_T_TR,MZT_T_TO_3,T40_T_KR,T40_T_TR,T40_T_TO_3,T25_T_KR,T25_T_TR,T25_T_TO_3,T16_T_KR,T16_T_TR,T16_T_TO_3]
#
#


var = [T_TR_SZ,T_TR_BDT,PLN_T_TR,KKU_T_TR,T_TO_2_CK,T_TR_CK,T_KR_K,T_TR_K,T_TO_3_K,T_KR_K1,T_TR_K1,T_TO_3_K1,DT_T_KR,DT_T_TR,DT_T_TO_3,MTZ2_T_KR,MTZ2_T_TR,MTZ2_T_TO_3,MZT_T_KR,MZT_T_TR,MZT_T_TO_3,T40_T_KR,T40_T_TR,T40_T_TO_3,T25_T_KR,T25_T_TR,T25_T_TO_3,T16_T_KR,T16_T_TR,T16_T_TO_3,T_TO_2_UAZ,T_TO_1_UAZ,T_TO_2_KAMAZ,T_TO_1_KAMAZ,T_TO_2_GAZ,T_TO_1_GAZ,T_TO_2_ZIL,T_TO_1_ZIL]
print(type(var))
print(len(var))
var.sort()


x = (len(var))
print(type(x))  # int
print(x)


print("--------------------------------------------------------------------------------------------")



print(var)
x = len(var)
d = 1
while var[0] == 0:
	var.pop(0)


while x != d:

	if len(var) > d:
		july = list(july)
		july.append(var[0])
		print('july',july)
		jl = sum(map(float,july))
		print(jl)
		var.pop(0)

		if len(var) > d:
			june.append(var[0])
			print('june',june)
			jn = sum(map(float,june))
			print(jn)
			var.pop(0)

			if len(var) > d:
				august.append(var[0])
				print('august',august)
				aug = sum(map(float,august))
				print(aug)
				var.pop(0)

				if len(var) > d:
					may.append(var[0])
					print('may',may)
					m = sum(map(float,may))
					print(m)
					var.pop(0)

					if len(var) > d:
						september.append(var[0])
						print('september',september)
						sept = sum(map(float,september))
						print(sept)
						var.pop(0)

						if len(var) > d:
							april.append(var[0])
							print('april',april)
							apr = sum(map(float,april))
							print(apr)
							var.pop(0)

							if len(var) > d:
								october.append(var[0])
								print('october',october)
								octo = sum(map(float,october))
								print(octo)
								var.pop(0)


								if len(var) > d:

									march.append(var[0])
									print('march',march)
									mar = sum(map(float, march))
									print(mar)
									var.pop(0)

									if len(var) > d:
										november.append(var[0])
										print('november',november)
										nov = sum(map(float,november))
										print(nov)
										var.pop(0)

										if len(var) > d:
											february.append(var[0])
											print('february',february)
											feb = sum(map(float,february))
											print(feb)
											var.pop(0)

											if len(var) > d:
												december.append(var[0])
												print('december',december)
												dec = sum(map(float,december))
												print(dec)
												var.pop(0)

												if len(var) > d:
													january.append(var[0])
													print('january',january)
													jan = sum(map(float,january))
													print(jan)
													var.pop(0)
	else:
		break


import matplotlib.pyplot as plt

print('='*50)


print(jan)
print(feb)
print(mar)
print(apr)
print(m)
print(jn)
print(jl)
print(aug)
print(sept)
print(octo)
print(nov)
print(dec)


s = [jan, feb, mar, apr, m, jn, jl, aug, sept, octo, nov, dec]
x = range(len(s))
ax = plt.gca()
ax.bar(x, s, align='edge')  #align='edge' - выравнивание по границе, а не по центру
ax.set_xticks(x)
ax.set_xticklabels(('янв', 'фев', 'март', 'апр','май','июнь','июль','авг','сент','окт','нояб','дек'))
plt.show()

