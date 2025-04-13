from sys import *
import matplotlib.pyplot as plt
from tkinter import*
from manager_ui import Window
import constants

win = Window()
win.create_ui()
win.fill_entry_for_test()
win.mainloop()


def create_table():

	print ()
	print (("_") * 75)
	print ("ТАБЛИЦА РЕМОНТОВ И ТО С\Х МАШИН:")
	print (("_") * 75)
	print ()

	th = ['МАРКА', 'КОЛ-ВО', 'КОЭФ.РЕМ.', 'КОЭФ.ПСТО', 'КОЛ-ВО ТР', 'КОЛ-ВО ПСТО']

	td = ['ККУ-2 А', KKU, "0.8", "1", KKU_NTR_d, KKU_NCTO,
		'ПЛН-4-35', PLN, "0.8", "2", PLN_NTR_d, PLN_NCTO,
		'БДТ-3', BDT, '0.78', "2", BDT_NTR_d, BDT_NCTO,
		'СЗ-3-6', SZ, "0.78", "2", SZ_NTR_d, SZ_NCTO,
		'СК-5', CK, '-', "1", NTR_CK_d, NCTO_CK]


with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nК-700:')

################################################    NKR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNкр')
	file_object.write(' = ')
	file_object.write(str(K_700_NKR_U))
	file_object.write(' * ')
	file_object.write(str(K_700))
	file_object.write(' / ')
	file_object.write(str(K_700_NKR_N))
	file_object.write(' = ')
	file_object.write(str(NKR_K_700))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NKR_K_700_d))

################################################   NTR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNтр')
	file_object.write(' = ')
	file_object.write(str(K_700_NKR_U))
	file_object.write(' * ')
	file_object.write(str(K_700))
	file_object.write(' / ')
	file_object.write(str(K_700_NTR_N))
	file_object.write(' - ')
	file_object.write(str(NKR_K_700_d))
	file_object.write(' = ')
	file_object.write(str(NTR_K_700))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_2_K_700_d))

################################################    NTO-3
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-3')
	file_object.write(' = ')
	file_object.write(str(K_700_NKR_U))
	file_object.write(' * ')
	file_object.write(str(K_700))
	file_object.write(' / ')
	file_object.write(str(NKR_K_700_d))
	file_object.write(' - ')
	file_object.write(str(K_700_NTO_3_N))
	file_object.write(' - ')
	file_object.write(str(NKR_K_700_d))
	file_object.write(' - ')
	file_object.write(str(NTO_2_K_700_d))
	file_object.write(' = ')
	file_object.write(str(NTO_3_K_700))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_3_K_700_d))

################################################    NTO-2
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-2')
	file_object.write(' = ')
	file_object.write(str(K_700_NKR_U))
	file_object.write(' * ')
	file_object.write(str(K_700))
	file_object.write(' / ')
	file_object.write(str(NKR_K_700_d))
	file_object.write(' - ')
	file_object.write(str(K_700_NTO_3_N))
	file_object.write(' - ')
	file_object.write(str(NKR_K_700_d))
	file_object.write(' - ')
	file_object.write(str(NTO_2_K_700_d))
	file_object.write(' - ')
	file_object.write(str(K_700_NTO_2_N))
	file_object.write(' = ')
	file_object.write(str(NTO_2_K_700))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_2_K_700_d))

################################################    NTO-1
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-1')
	file_object.write(' = ')
	file_object.write(str(K_700_NKR_U))
	file_object.write(' * ')
	file_object.write(str(K_700))
	file_object.write(' / ')
	file_object.write(str(NKR_K_700_d))
	file_object.write(' - ')
	file_object.write(str(K_700_NTO_3_N))
	file_object.write(' - ')
	file_object.write(str(NKR_K_700_d))
	file_object.write(' - ')
	file_object.write(str(NTO_2_K_700_d))
	file_object.write(' - ')
	file_object.write(str(K_700_NTO_2_N))
	file_object.write(' - ')
	file_object.write(str(K_700_NTO_1_N))
	file_object.write(' = ')
	file_object.write(str(NTO_1_K_700))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_1_K_700_d))



################################################    NCTO
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNсто')
	file_object.write(' = ')
	file_object.write(str(K_700_NKR_U))
	file_object.write(' * ')
	file_object.write(str(K_700))
	file_object.write(' = ')
	file_object.write(str(K_700_N_CTO))

####################################################################
#                           K-701
####################################################################


# w перезапись с удалением всего что было
# a дозапись с сохранением старого
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\n')
	file_object.write('\nК-701:')

################################################    NKR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNкр')
	file_object.write(' = ')
	file_object.write(str(K_701_NKR_U))
	file_object.write(' * ')
	file_object.write(str(K_701))
	file_object.write(' / ')
	file_object.write(str(K_701_NKR_N))
	file_object.write(' = ')
	file_object.write(str(NKR_K_701))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NKR_K_701_d))

################################################   NTR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNтр')
	file_object.write(' = ')
	file_object.write(str(K_701_NKR_U))
	file_object.write(' * ')
	file_object.write(str(K_701))
	file_object.write(' / ')
	file_object.write(str(K_701_NTR_N))
	file_object.write(' - ')
	file_object.write(str(NKR_K_701_d))
	file_object.write(' = ')
	file_object.write(str(NTR_K_701))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_2_K_701_d))

################################################    NTO-3
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-3')
	file_object.write(' = ')
	file_object.write(str(K_701_NKR_U))
	file_object.write(' * ')
	file_object.write(str(K_701))
	file_object.write(' / ')
	file_object.write(str(NKR_K_701_d))
	file_object.write(' - ')
	file_object.write(str(K_701_NTO_3_N))
	file_object.write(' - ')
	file_object.write(str(NKR_K_701_d))
	file_object.write(' - ')
	file_object.write(str(NTO_2_K_701_d))
	file_object.write(' = ')
	file_object.write(str(NTO_3_K_701))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_3_K_701_d))

################################################    NTO-2
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-2')
	file_object.write(' = ')
	file_object.write(str(K_701_NKR_U))
	file_object.write(' * ')
	file_object.write(str(K_701))
	file_object.write(' / ')
	file_object.write(str(NKR_K_701_d))
	file_object.write(' - ')
	file_object.write(str(K_701_NTO_3_N))
	file_object.write(' - ')
	file_object.write(str(NKR_K_701_d))
	file_object.write(' - ')
	file_object.write(str(NTO_2_K_701_d))
	file_object.write(' - ')
	file_object.write(str(K_701_NTO_2_N))
	file_object.write(' = ')
	file_object.write(str(NTO_2_K_701))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_2_K_701_d))

################################################    NTO-1
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-1')
	file_object.write(' = ')
	file_object.write(str(K_701_NKR_U))
	file_object.write(' * ')
	file_object.write(str(K_701))
	file_object.write(' / ')
	file_object.write(str(NKR_K_701_d))
	file_object.write(' - ')
	file_object.write(str(K_701_NTO_3_N))
	file_object.write(' - ')
	file_object.write(str(NKR_K_701_d))
	file_object.write(' - ')
	file_object.write(str(NTO_2_K_701_d))
	file_object.write(' - ')
	file_object.write(str(K_701_NTO_2_N))
	file_object.write(' - ')
	file_object.write(str(K_701_NTO_1_N))
	file_object.write(' = ')
	file_object.write(str(NTO_1_K_701))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_1_K_701_d))

################################################    NCTO
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNсто')
	file_object.write(' = ')
	file_object.write(str(K_701_NKR_U))
	file_object.write(' * ')
	file_object.write(str(K_701))
	file_object.write(' = ')
	file_object.write(str(K_701_N_CTO))



####################################################################
#                           DT-75
####################################################################


# w перезапись с удалением всего что было
# a дозапись с сохранением старого
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\n')
	file_object.write('\nДТ-75 МВ:')

################################################    NKR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNкр')
	file_object.write(' = ')
	file_object.write(str(DT_NKR_U))
	file_object.write(' * ')
	file_object.write(str(DT))
	file_object.write(' / ')
	file_object.write(str(DT_NKR_N))
	file_object.write(' = ')
	file_object.write(str(NKR_DT))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NKR_DT_d))

################################################   NTR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNтр')
	file_object.write(' = ')
	file_object.write(str(DT_NKR_U))
	file_object.write(' * ')
	file_object.write(str(DT))
	file_object.write(' / ')
	file_object.write(str(DT_NTR_N))
	file_object.write(' - ')
	file_object.write(str(NKR_DT_d))
	file_object.write(' = ')
	file_object.write(str(NTR_DT))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_2_DT_d))

################################################    NTO-3
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-3')
	file_object.write(' = ')
	file_object.write(str(DT_NKR_U))
	file_object.write(' * ')
	file_object.write(str(DT))
	file_object.write(' / ')
	file_object.write(str(NKR_DT_d))
	file_object.write(' - ')
	file_object.write(str(DT_NTO_3_N))
	file_object.write(' - ')
	file_object.write(str(NKR_DT_d))
	file_object.write(' - ')
	file_object.write(str(NTO_2_DT_d))
	file_object.write(' = ')
	file_object.write(str(NTO_3_DT))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_3_DT_d))

################################################    NTO-2
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-2')
	file_object.write(' = ')
	file_object.write(str(DT_NKR_U))
	file_object.write(' * ')
	file_object.write(str(DT))
	file_object.write(' / ')
	file_object.write(str(NKR_DT_d))
	file_object.write(' - ')
	file_object.write(str(DT_NTO_3_N))
	file_object.write(' - ')
	file_object.write(str(NKR_DT_d))
	file_object.write(' - ')
	file_object.write(str(NTO_2_DT_d))
	file_object.write(' - ')
	file_object.write(str(DT_NTO_2_N))
	file_object.write(' = ')
	file_object.write(str(NTO_2_DT))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_2_DT_d))

################################################    NTO-1
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-1')
	file_object.write(' = ')
	file_object.write(str(DT_NKR_U))
	file_object.write(' * ')
	file_object.write(str(DT))
	file_object.write(' / ')
	file_object.write(str(NKR_DT_d))
	file_object.write(' - ')
	file_object.write(str(DT_NTO_3_N))
	file_object.write(' - ')
	file_object.write(str(NKR_DT_d))
	file_object.write(' - ')
	file_object.write(str(NTO_2_DT_d))
	file_object.write(' - ')
	file_object.write(str(DT_NTO_2_N))
	file_object.write(' - ')
	file_object.write(str(DT_NTO_1_N))
	file_object.write(' = ')
	file_object.write(str(NTO_1_DT))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_1_DT_d))

################################################    NCTO
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNсто')
	file_object.write(' = ')
	file_object.write(str(DT_NKR_U))
	file_object.write(' * ')
	file_object.write(str(DT))
	file_object.write(' = ')
	file_object.write(str(DT_N_CTO))



####################################################################
#                           MTZ2
####################################################################


# w перезапись с удалением всего что было
# a дозапись с сохранением старого
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\n')
	file_object.write('\nМТЗ-82:')

################################################    NKR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNкр')
	file_object.write(' = ')
	file_object.write(str(MTZ2_NKR_U))
	file_object.write(' * ')
	file_object.write(str(MTZ2))
	file_object.write(' / ')
	file_object.write(str(MTZ2_NKR_N))
	file_object.write(' = ')
	file_object.write(str(NKR_MTZ2))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NKR_MTZ2_d))

################################################   NTR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNтр')
	file_object.write(' = ')
	file_object.write(str(MTZ2_NKR_U))
	file_object.write(' * ')
	file_object.write(str(MTZ2))
	file_object.write(' / ')
	file_object.write(str(MTZ2_NTR_N))
	file_object.write(' - ')
	file_object.write(str(NKR_MTZ2_d))
	file_object.write(' = ')
	file_object.write(str(NTR_MTZ2))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_2_MTZ2_d))

################################################    NTO-3
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-3')
	file_object.write(' = ')
	file_object.write(str(MTZ2_NKR_U))
	file_object.write(' * ')
	file_object.write(str(MTZ2))
	file_object.write(' / ')
	file_object.write(str(NKR_MTZ2_d))
	file_object.write(' - ')
	file_object.write(str(MTZ2_NTO_3_N))
	file_object.write(' - ')
	file_object.write(str(NKR_MTZ2_d))
	file_object.write(' - ')
	file_object.write(str(NTO_2_MTZ2_d))
	file_object.write(' = ')
	file_object.write(str(NTO_3_MTZ2))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_3_MTZ2_d))

################################################    NTO-2
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-2')
	file_object.write(' = ')
	file_object.write(str(MTZ2_NKR_U))
	file_object.write(' * ')
	file_object.write(str(MTZ2))
	file_object.write(' / ')
	file_object.write(str(NKR_MTZ2_d))
	file_object.write(' - ')
	file_object.write(str(MTZ2_NTO_3_N))
	file_object.write(' - ')
	file_object.write(str(NKR_MTZ2_d))
	file_object.write(' - ')
	file_object.write(str(NTO_2_MTZ2_d))
	file_object.write(' - ')
	file_object.write(str(MTZ2_NTO_2_N))
	file_object.write(' = ')
	file_object.write(str(NTO_2_MTZ2))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_2_MTZ2_d))

################################################    NTO-1
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-1')
	file_object.write(' = ')
	file_object.write(str(MTZ2_NKR_U))
	file_object.write(' * ')
	file_object.write(str(MTZ2))
	file_object.write(' / ')
	file_object.write(str(NKR_MTZ2_d))
	file_object.write(' - ')
	file_object.write(str(MTZ2_NTO_3_N))
	file_object.write(' - ')
	file_object.write(str(NKR_MTZ2_d))
	file_object.write(' - ')
	file_object.write(str(NTO_2_MTZ2_d))
	file_object.write(' - ')
	file_object.write(str(MTZ2_NTO_2_N))
	file_object.write(' - ')
	file_object.write(str(MTZ2_NTO_1_N))
	file_object.write(' = ')
	file_object.write(str(NTO_1_MTZ2))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_1_MTZ2_d))

################################################    NCTO
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNсто')
	file_object.write(' = ')
	file_object.write(str(MTZ2_NKR_U))
	file_object.write(' * ')
	file_object.write(str(MTZ2))
	file_object.write(' = ')
	file_object.write(str(MTZ2_N_CTO))


####################################################################
#                           MZT
####################################################################


# w перезапись с удалением всего что было
# a дозапись с сохранением старого
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\n')
	file_object.write('\nМТЗ-80:')

################################################    NKR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNкр')
	file_object.write(' = ')
	file_object.write(str(MZT_NKR_U))
	file_object.write(' * ')
	file_object.write(str(MZT))
	file_object.write(' / ')
	file_object.write(str(MZT_NKR_N))
	file_object.write(' = ')
	file_object.write(str(NKR_MZT))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NKR_MZT_d))

################################################   NTR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNтр')
	file_object.write(' = ')
	file_object.write(str(MZT_NKR_U))
	file_object.write(' * ')
	file_object.write(str(MZT))
	file_object.write(' / ')
	file_object.write(str(MZT_NTR_N))
	file_object.write(' - ')
	file_object.write(str(NKR_MZT_d))
	file_object.write(' = ')
	file_object.write(str(NTR_MZT))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_2_MZT_d))

################################################    NTO-3
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-3')
	file_object.write(' = ')
	file_object.write(str(MZT_NKR_U))
	file_object.write(' * ')
	file_object.write(str(MZT))
	file_object.write(' / ')
	file_object.write(str(NKR_MZT_d))
	file_object.write(' - ')
	file_object.write(str(MZT_NTO_3_N))
	file_object.write(' - ')
	file_object.write(str(NKR_MZT_d))
	file_object.write(' - ')
	file_object.write(str(NTO_2_MZT_d))
	file_object.write(' = ')
	file_object.write(str(NTO_3_MZT))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_3_MZT_d))

################################################    NTO-2
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-2')
	file_object.write(' = ')
	file_object.write(str(MZT_NKR_U))
	file_object.write(' * ')
	file_object.write(str(MZT))
	file_object.write(' / ')
	file_object.write(str(NKR_MZT_d))
	file_object.write(' - ')
	file_object.write(str(MZT_NTO_3_N))
	file_object.write(' - ')
	file_object.write(str(NKR_MZT_d))
	file_object.write(' - ')
	file_object.write(str(NTO_2_MZT_d))
	file_object.write(' - ')
	file_object.write(str(MZT_NTO_2_N))
	file_object.write(' = ')
	file_object.write(str(NTO_2_MZT))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_2_MZT_d))

################################################    NTO-1
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-1')
	file_object.write(' = ')
	file_object.write(str(MZT_NKR_U))
	file_object.write(' * ')
	file_object.write(str(MZT))
	file_object.write(' / ')
	file_object.write(str(NKR_MZT_d))
	file_object.write(' - ')
	file_object.write(str(MZT_NTO_3_N))
	file_object.write(' - ')
	file_object.write(str(NKR_MZT_d))
	file_object.write(' - ')
	file_object.write(str(NTO_2_MZT_d))
	file_object.write(' - ')
	file_object.write(str(MZT_NTO_2_N))
	file_object.write(' - ')
	file_object.write(str(MZT_NTO_1_N))
	file_object.write(' = ')
	file_object.write(str(NTO_1_MZT))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_1_MZT_d))

################################################    NCTO
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNсто')
	file_object.write(' = ')
	file_object.write(str(MZT_NKR_U))
	file_object.write(' * ')
	file_object.write(str(MZT))
	file_object.write(' = ')
	file_object.write(str(MZT_N_CTO))



####################################################################
#                           T-40
####################################################################


# w перезапись с удалением всего что было
# a дозапись с сохранением старого
with open('KURSOVAYA_v1.txt', 'a')as file_object:

	file_object.write('\n')
	file_object.write('\nT40:')

################################################    NKR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNкр')
	file_object.write(' = ')
	file_object.write(str(T40_NKR_U))
	file_object.write(' * ')
	file_object.write(str(T40))
	file_object.write(' / ')
	file_object.write(str(T40_NKR_N))
	file_object.write(' = ')
	file_object.write(str(NKR_T40))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NKR_T40_d))

################################################   NTR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNтр')
	file_object.write(' = ')
	file_object.write(str(T40_NKR_U))
	file_object.write(' * ')
	file_object.write(str(T40))
	file_object.write(' / ')
	file_object.write(str(T40_NTR_N))
	file_object.write(' - ')
	file_object.write(str(NKR_T40_d))
	file_object.write(' = ')
	file_object.write(str(NTR_T40))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_2_T40_d))

################################################    NTO-3
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-3')
	file_object.write(' = ')
	file_object.write(str(T40_NKR_U))
	file_object.write(' * ')
	file_object.write(str(T40))
	file_object.write(' / ')
	file_object.write(str(NKR_T40_d))
	file_object.write(' - ')
	file_object.write(str(T40_NTO_3_N))
	file_object.write(' - ')
	file_object.write(str(NKR_T40_d))
	file_object.write(' - ')
	file_object.write(str(NTO_2_T40_d))
	file_object.write(' = ')
	file_object.write(str(NTO_3_T40))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_3_T40_d))

################################################    NTO-2
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-2')
	file_object.write(' = ')
	file_object.write(str(T40_NKR_U))
	file_object.write(' * ')
	file_object.write(str(T40))
	file_object.write(' / ')
	file_object.write(str(NKR_T40_d))
	file_object.write(' - ')
	file_object.write(str(T40_NTO_3_N))
	file_object.write(' - ')
	file_object.write(str(NKR_T40_d))
	file_object.write(' - ')
	file_object.write(str(NTO_2_T40_d))
	file_object.write(' - ')
	file_object.write(str(T40_NTO_2_N))
	file_object.write(' = ')
	file_object.write(str(NTO_2_T40))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_2_T40_d))

################################################    NTO-1
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-1')
	file_object.write(' = ')
	file_object.write(str(T40_NKR_U))
	file_object.write(' * ')
	file_object.write(str(T40))
	file_object.write(' / ')
	file_object.write(str(NKR_T40_d))
	file_object.write(' - ')
	file_object.write(str(T40_NTO_3_N))
	file_object.write(' - ')
	file_object.write(str(NKR_T40_d))
	file_object.write(' - ')
	file_object.write(str(NTO_2_T40_d))
	file_object.write(' - ')
	file_object.write(str(T40_NTO_2_N))
	file_object.write(' - ')
	file_object.write(str(T40_NTO_1_N))
	file_object.write(' = ')
	file_object.write(str(NTO_1_T40))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_1_T40_d))

################################################    NCTO
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNсто')
	file_object.write(' = ')
	file_object.write(str(T40_NKR_U))
	file_object.write(' * ')
	file_object.write(str(T40))
	file_object.write(' = ')
	file_object.write(str(T40_N_CTO))


####################################################################
#                           T25
####################################################################


# w перезапись с удалением всего что было
# a дозапись с сохранением старого
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\n')
	file_object.write('\nT-25:')

################################################    NKR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNкр')
	file_object.write(' = ')
	file_object.write(str(T25_NKR_U))
	file_object.write(' * ')
	file_object.write(str(T25))
	file_object.write(' / ')
	file_object.write(str(T25_NKR_N))
	file_object.write(' = ')
	file_object.write(str(NKR_T25))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NKR_T25_d))

################################################   NTR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNтр')
	file_object.write(' = ')
	file_object.write(str(T25_NKR_U))
	file_object.write(' * ')
	file_object.write(str(T25))
	file_object.write(' / ')
	file_object.write(str(T25_NTR_N))
	file_object.write(' - ')
	file_object.write(str(NKR_T25_d))
	file_object.write(' = ')
	file_object.write(str(NTR_T25))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_2_T25_d))

################################################    NTO-3
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-3')
	file_object.write(' = ')
	file_object.write(str(T25_NKR_U))
	file_object.write(' * ')
	file_object.write(str(T25))
	file_object.write(' / ')
	file_object.write(str(NKR_T25_d))
	file_object.write(' - ')
	file_object.write(str(T25_NTO_3_N))
	file_object.write(' - ')
	file_object.write(str(NKR_T25_d))
	file_object.write(' - ')
	file_object.write(str(NTO_2_T25_d))
	file_object.write(' = ')
	file_object.write(str(NTO_3_T25))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_3_T25_d))

################################################    NTO-2
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-2')
	file_object.write(' = ')
	file_object.write(str(T25_NKR_U))
	file_object.write(' * ')
	file_object.write(str(T25))
	file_object.write(' / ')
	file_object.write(str(NKR_T25_d))
	file_object.write(' - ')
	file_object.write(str(T25_NTO_3_N))
	file_object.write(' - ')
	file_object.write(str(NKR_T25_d))
	file_object.write(' - ')
	file_object.write(str(NTO_2_T25_d))
	file_object.write(' - ')
	file_object.write(str(T25_NTO_2_N))
	file_object.write(' = ')
	file_object.write(str(NTO_2_T25))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_2_T25_d))

################################################    NTO-1
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-1')
	file_object.write(' = ')
	file_object.write(str(T25_NKR_U))
	file_object.write(' * ')
	file_object.write(str(T25))
	file_object.write(' / ')
	file_object.write(str(NKR_T25_d))
	file_object.write(' - ')
	file_object.write(str(T25_NTO_3_N))
	file_object.write(' - ')
	file_object.write(str(NKR_T25_d))
	file_object.write(' - ')
	file_object.write(str(NTO_2_T25_d))
	file_object.write(' - ')
	file_object.write(str(T25_NTO_2_N))
	file_object.write(' - ')
	file_object.write(str(T25_NTO_1_N))
	file_object.write(' = ')
	file_object.write(str(NTO_1_T25))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_1_T25_d))

################################################    NCTO
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNсто')
	file_object.write(' = ')
	file_object.write(str(T25_NKR_U))
	file_object.write(' * ')
	file_object.write(str(T25))
	file_object.write(' = ')
	file_object.write(str(T25_N_CTO))


####################################################################
#                           T16
####################################################################


# w перезапись с удалением всего что было
# a дозапись с сохранением старого
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\n')
	file_object.write('\nT16:')

################################################    NKR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNкр')
	file_object.write(' = ')
	file_object.write(str(T16_NKR_U))
	file_object.write(' * ')
	file_object.write(str(T16))
	file_object.write(' / ')
	file_object.write(str(T16_NKR_N))
	file_object.write(' = ')
	file_object.write(str(NKR_T16))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NKR_T16_d))

################################################   NTR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNтр')
	file_object.write(' = ')
	file_object.write(str(T16_NKR_U))
	file_object.write(' * ')
	file_object.write(str(T16))
	file_object.write(' / ')
	file_object.write(str(T16_NTR_N))
	file_object.write(' - ')
	file_object.write(str(NKR_T16_d))
	file_object.write(' = ')
	file_object.write(str(NTR_T16))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_2_T16_d))

################################################    NTO-3
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-3')
	file_object.write(' = ')
	file_object.write(str(T16_NKR_U))
	file_object.write(' * ')
	file_object.write(str(T16))
	file_object.write(' / ')
	file_object.write(str(NKR_T16_d))
	file_object.write(' - ')
	file_object.write(str(T16_NTO_3_N))
	file_object.write(' - ')
	file_object.write(str(NKR_T16_d))
	file_object.write(' - ')
	file_object.write(str(NTO_2_T16_d))
	file_object.write(' = ')
	file_object.write(str(NTO_3_T16))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_3_T16_d))

################################################    NTO-2
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-2')
	file_object.write(' = ')
	file_object.write(str(T16_NKR_U))
	file_object.write(' * ')
	file_object.write(str(T16))
	file_object.write(' / ')
	file_object.write(str(NKR_T16_d))
	file_object.write(' - ')
	file_object.write(str(T16_NTO_3_N))
	file_object.write(' - ')
	file_object.write(str(NKR_T16_d))
	file_object.write(' - ')
	file_object.write(str(NTO_2_T16_d))
	file_object.write(' - ')
	file_object.write(str(T16_NTO_2_N))
	file_object.write(' = ')
	file_object.write(str(NTO_2_T16))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_2_T16_d))

################################################    NTO-1
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-1')
	file_object.write(' = ')
	file_object.write(str(T16_NKR_U))
	file_object.write(' * ')
	file_object.write(str(T16))
	file_object.write(' / ')
	file_object.write(str(NKR_T16_d))
	file_object.write(' - ')
	file_object.write(str(T16_NTO_3_N))
	file_object.write(' - ')
	file_object.write(str(NKR_T16_d))
	file_object.write(' - ')
	file_object.write(str(NTO_2_T16_d))
	file_object.write(' - ')
	file_object.write(str(T16_NTO_2_N))
	file_object.write(' - ')
	file_object.write(str(T16_NTO_1_N))
	file_object.write(' = ')
	file_object.write(str(NTO_1_T16))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_1_T16_d))

################################################    NCTO
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNсто')
	file_object.write(' = ')
	file_object.write(str(T16_NKR_U))
	file_object.write(' * ')
	file_object.write(str(T16))
	file_object.write(' = ')
	file_object.write(str(T16_N_CTO))




####################################################################
#                           УАЗ-469
####################################################################


# w перезапись с удалением всего что было
# a дозапись с сохранением старого
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\n')
	file_object.write('\nУАЗ-469:')

################################################    NKR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNкр')
	file_object.write(' = ')
	file_object.write(str(UAZ_NKR_U))
	file_object.write(' * ')
	file_object.write(str(UAZ))
	file_object.write(' / ')
	file_object.write(str(UAZ_NKR_N))
	file_object.write(' = ')
	file_object.write(str(NKR_UAZ))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NKR_UAZ_d))


################################################    NTO-2
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-2')
	file_object.write(' = ')
	file_object.write(str(UAZ_NKR_U))
	file_object.write(' * ')
	file_object.write(str(UAZ))
	file_object.write(' / ')
	file_object.write(str(UAZ_NTO_2_N))
	file_object.write(' - ')
	file_object.write(str(NKR_UAZ_d))
	file_object.write(' = ')
	file_object.write(str(NTO_2_UAZ))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_2_UAZ_d))

################################################    NTO-1
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-1')
	file_object.write(' = ')
	file_object.write(str(UAZ_NKR_U))
	file_object.write(' * ')
	file_object.write(str(UAZ))
	file_object.write(' / ')
	file_object.write(str(UAZ_NTO_1_N))
	file_object.write(' - ')
	file_object.write(str(NKR_UAZ_d))
	file_object.write(' - ')
	file_object.write(str(NTO_2_UAZ_d))
	file_object.write(' = ')
	file_object.write(str(NTO_1_UAZ))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_1_UAZ_d))



################################################    NCTO
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNсто')
	file_object.write(' = ')
	file_object.write(str(UAZ_NCTO))
	file_object.write(' * ')
	file_object.write(str(UAZ))
	file_object.write(' = ')
	file_object.write(str(UAZ_N_CTO))


####################################################################
#                           КАМАЗ-5320
####################################################################


# w перезапись с удалением всего что было
# a дозапись с сохранением старого
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\n')
	file_object.write('\nКАМАЗ-5320:')

################################################    NKR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNкр')
	file_object.write(' = ')
	file_object.write(str(KAMAZ_NKR_U))
	file_object.write(' * ')
	file_object.write(str(KAMAZ))
	file_object.write(' / ')
	file_object.write(str(KAMAZ_NKR_N))
	file_object.write(' = ')
	file_object.write(str(NKR_KAMAZ))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NKR_KAMAZ_d))


################################################    NTO-2
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-2')
	file_object.write(' = ')
	file_object.write(str(KAMAZ_NKR_U))
	file_object.write(' * ')
	file_object.write(str(KAMAZ))
	file_object.write(' / ')
	file_object.write(str(KAMAZ_NTO_2_N))
	file_object.write(' - ')
	file_object.write(str(NKR_KAMAZ_d))
	file_object.write(' = ')
	file_object.write(str(NTO_2_KAMAZ))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_2_KAMAZ_d))

################################################    NTO-1
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-1')
	file_object.write(' = ')
	file_object.write(str(KAMAZ_NKR_U))
	file_object.write(' * ')
	file_object.write(str(KAMAZ))
	file_object.write(' / ')
	file_object.write(str(KAMAZ_NTO_1_N))
	file_object.write(' - ')
	file_object.write(str(NKR_KAMAZ_d))
	file_object.write(' - ')
	file_object.write(str(NTO_2_KAMAZ_d))
	file_object.write(' = ')
	file_object.write(str(NTO_1_KAMAZ))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_1_KAMAZ_d))



################################################    NCTO
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNсто')
	file_object.write(' = ')
	file_object.write(str(KAMAZ_NCTO))
	file_object.write(' * ')
	file_object.write(str(KAMAZ))
	file_object.write(' = ')
	file_object.write(str(KAMAZ_N_CTO))


####################################################################
#                           ГАЗ-53
####################################################################


# w перезапись с удалением всего что было
# a дозапись с сохранением старого
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\n')
	file_object.write('\nГАЗ-53:')

################################################    NKR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNкр')
	file_object.write(' = ')
	file_object.write(str(GAZ_NKR_U))
	file_object.write(' * ')
	file_object.write(str(GAZ))
	file_object.write(' / ')
	file_object.write(str(GAZ_NKR_N))
	file_object.write(' = ')
	file_object.write(str(NKR_GAZ))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NKR_GAZ_d))


################################################    NTO-2
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-2')
	file_object.write(' = ')
	file_object.write(str(GAZ_NKR_U))
	file_object.write(' * ')
	file_object.write(str(GAZ))
	file_object.write(' / ')
	file_object.write(str(GAZ_NTO_2_N))
	file_object.write(' - ')
	file_object.write(str(NKR_GAZ_d))
	file_object.write(' = ')
	file_object.write(str(NTO_2_GAZ))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_2_GAZ_d))

################################################    NTO-1
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-1')
	file_object.write(' = ')
	file_object.write(str(GAZ_NKR_U))
	file_object.write(' * ')
	file_object.write(str(GAZ))
	file_object.write(' / ')
	file_object.write(str(GAZ_NTO_1_N))
	file_object.write(' - ')
	file_object.write(str(NKR_GAZ_d))
	file_object.write(' - ')
	file_object.write(str(NTO_2_GAZ_d))
	file_object.write(' = ')
	file_object.write(str(NTO_1_GAZ))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_1_GAZ_d))



################################################    NCTO
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNсто')
	file_object.write(' = ')
	file_object.write(str(GAZ_NCTO))
	file_object.write(' * ')
	file_object.write(str(GAZ))
	file_object.write(' = ')
	file_object.write(str(GAZ_N_CTO))



####################################################################
#                           ЗИЛ-130
####################################################################


# w перезапись с удалением всего что было
# a дозапись с сохранением старого
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\n')
	file_object.write('\nЗИЛ-130:')

################################################    NKR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNкр')
	file_object.write(' = ')
	file_object.write(str(ZIL_NKR_U))
	file_object.write(' * ')
	file_object.write(str(ZIL))
	file_object.write(' / ')
	file_object.write(str(ZIL_NKR_N))
	file_object.write(' = ')
	file_object.write(str(NKR_ZIL))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NKR_ZIL_d))


################################################    NTO-2
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-2')
	file_object.write(' = ')
	file_object.write(str(ZIL_NKR_U))
	file_object.write(' * ')
	file_object.write(str(ZIL))
	file_object.write(' / ')
	file_object.write(str(ZIL_NTO_2_N))
	file_object.write(' - ')
	file_object.write(str(NKR_ZIL_d))
	file_object.write(' = ')
	file_object.write(str(NTO_2_ZIL))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_2_ZIL_d))

################################################    NTO-1
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-1')
	file_object.write(' = ')
	file_object.write(str(ZIL_NKR_U))
	file_object.write(' * ')
	file_object.write(str(ZIL))
	file_object.write(' / ')
	file_object.write(str(ZIL_NTO_1_N))
	file_object.write(' - ')
	file_object.write(str(NKR_ZIL_d))
	file_object.write(' - ')
	file_object.write(str(NTO_2_ZIL_d))
	file_object.write(' = ')
	file_object.write(str(NTO_1_ZIL))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_1_ZIL_d))



################################################    NCTO
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNсто')
	file_object.write(' = ')
	file_object.write(str(ZIL_NCTO))
	file_object.write(' * ')
	file_object.write(str(ZIL))
	file_object.write(' = ')
	file_object.write(str(ZIL_N_CTO))




####################################################################
#                           CK-5
####################################################################


# w перезапись с удалением всего что было
# a дозапись с сохранением старого
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\n')
	file_object.write('\nCK-5:')

################################################    NKR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNкр')
	file_object.write(' = ')
	file_object.write(str(CK))
	file_object.write(' * ')
	file_object.write(str(CK_NKR))
	file_object.write(' = ')
	file_object.write(str(NKR_CK))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NKR_CK_d))

################################################   NTR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNтр')
	file_object.write(' = ')
	file_object.write(str(CK))
	file_object.write(' * ')
	file_object.write(str(CK_NTR))
	file_object.write(' = ')
	file_object.write(str(NTR_CK))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTR_CK_d))

################################################    NTO-2
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-2')
	file_object.write(' = ')
	file_object.write(str(CK_NTO))
	file_object.write(' * ')
	file_object.write(str(CK))
	file_object.write(' / ')
	file_object.write(str(CK_NTO_2))
	file_object.write(' - ')
	file_object.write(str(CK_NKR))
	file_object.write(' - ')
	file_object.write(str(NTR_CK))
	file_object.write(' = ')
	file_object.write(str(NTO_2_CK))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_2_CK_d))

################################################    NTO-1
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-1')
	file_object.write(' = ')
	file_object.write(str(CK_NTO))
	file_object.write(' * ')
	file_object.write(str(CK))
	file_object.write(' / ')
	file_object.write(str(CK_NTO_1))
	file_object.write(' - ')
	file_object.write(str(NKR_CK))
	file_object.write(' - ')
	file_object.write(str(NTR_CK))
	file_object.write(' - ')
	file_object.write(str(NTO_2_CK))
	file_object.write(' = ')
	file_object.write(str(NTO_1_CK))
	file_object.write('\nПринимаю = ')
	file_object.write(str(NTO_1_CK_d))

################################################    NCTO
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNсто')
	file_object.write(' = ')
	file_object.write(str(CK))
	file_object.write(' * ')
	file_object.write(str(CK_NCTO))
	file_object.write(' = ')
	file_object.write(str(NCTO_CK))



####################################################################
#                           PLN-4-35
####################################################################


# w перезапись с удалением всего что было
# a дозапись с сохранением старого
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\n')
	file_object.write('\nПЛН-4-35:')

################################################    NTR

with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNтр')
	file_object.write(' = ')
	file_object.write(str(PLN))
	file_object.write(' * ')
	file_object.write(str(NTR_PLN))
	file_object.write(' = ')
	file_object.write(str(PLN_NTR))

################################################    NCTO

with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNсто')
	file_object.write(' = ')
	file_object.write(str(PLN))
	file_object.write(' * ')
	file_object.write(str(NCTO_PLN))
	file_object.write(' = ')
	file_object.write(str(PLN_NCTO))



####################################################################
#                           SZ-3-6
####################################################################


# w перезапись с удалением всего что было
# a дозапись с сохранением старого
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\n')
	file_object.write('\nСЗ-3-6')

################################################    NTR

with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNтр')
	file_object.write(' = ')
	file_object.write(str(SZ))
	file_object.write(' * ')
	file_object.write(str(NTR_SZ))
	file_object.write(' = ')
	file_object.write(str(SZ_NTR))

################################################    NCTO

with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNсто')
	file_object.write(' = ')
	file_object.write(str(SZ))
	file_object.write(' * ')
	file_object.write(str(NCTO_SZ))
	file_object.write(' = ')
	file_object.write(str(SZ_NCTO))



####################################################################
#                           KKU-2
####################################################################


# w перезапись с удалением всего что было
# a дозапись с сохранением старого
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\n')
	file_object.write('\nККУ-2А')

################################################    NTR

with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNтр')
	file_object.write(' = ')
	file_object.write(str(KKU))
	file_object.write(' * ')
	file_object.write(str(NTR_KKU))
	file_object.write(' = ')
	file_object.write(str(KKU_NTR))

################################################    NCTO

with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNсто')
	file_object.write(' = ')
	file_object.write(str(KKU))
	file_object.write(' * ')
	file_object.write(str(NCTO_KKU))
	file_object.write(' = ')
	file_object.write(str(KKU_NCTO))



####################################################################
#                           BDT-3
####################################################################


# w перезапись с удалением всего что было
# a дозапись с сохранением старого
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\n')
	file_object.write('\nБДТ-3')

################################################    NTR

with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNтр')
	file_object.write(' = ')
	file_object.write(str(BDT))
	file_object.write(' * ')
	file_object.write(str(NTR_BDT))
	file_object.write(' = ')
	file_object.write(str(BDT_NTR))

################################################    NCTO

with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNсто')
	file_object.write(' = ')
	file_object.write(str(BDT))
	file_object.write(' * ')
	file_object.write(str(NCTO_BDT))
	file_object.write(' = ')
	file_object.write(str(BDT_NCTO))





with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\n')
	file_object.write('\nРАСЧЕТ ТРУДОЕМКОСТИ:')


####################################################################
#                           K-700
####################################################################


# w перезапись с удалением всего что было
# a дозапись с сохранением старого
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\n')
	file_object.write('\nК-700:')

################################################    TKR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTкр')
	file_object.write(' = ')
	file_object.write(str(NKR_K_700_d))
	file_object.write(' * ')
	file_object.write(str(K_T_KR))
	file_object.write(' = ')
	file_object.write(str(T_KR_K))

################################################   TTR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTтр')
	file_object.write(' = ')
	file_object.write(str(NTR_K_700_d))
	file_object.write(' * ')
	file_object.write(str(K_T_TR))
	file_object.write(' = ')
	file_object.write(str(T_TR_K))
################################################    TTO-3
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTто-3')
	file_object.write(' = ')
	file_object.write(str(NTO_3_K_700_d))
	file_object.write(' * ')
	file_object.write(str(K_T_TO_3))
	file_object.write(' = ')
	file_object.write(str(T_TO_3_K))
################################################    TTO-2
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTто-2')
	file_object.write(' = ')
	file_object.write(str(NTO_2_K_700_d))
	file_object.write(' * ')
	file_object.write(str(K_T_TO_2))
	file_object.write(' = ')
	file_object.write(str(T_TO_2_K))
################################################    TTO-1
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-1')
	file_object.write(' = ')
	file_object.write(str(NTO_1_K_700_d))
	file_object.write(' * ')
	file_object.write(str(K_T_TO_1))
	file_object.write(' = ')
	file_object.write(str(T_TO_1_K))

################################################    TCTO
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTсто')
	file_object.write(' = ')
	file_object.write(str(K_700_N_CTO))
	file_object.write(' * ')
	file_object.write(str(K_T_CTO))
	file_object.write(' = ')
	file_object.write(str(T_CTO_K))

####################################################################
#                           K-701
####################################################################


# w перезапись с удалением всего что было
# a дозапись с сохранением старого
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\n')
	file_object.write('\nК-701:')

################################################    TKR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTкр')
	file_object.write(' = ')
	file_object.write(str(NKR_K_701_d))
	file_object.write(' * ')
	file_object.write(str(K1_T_KR))
	file_object.write(' = ')
	file_object.write(str(T_KR_K1))

################################################   TTR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTтр')
	file_object.write(' = ')
	file_object.write(str(NTR_K_701_d))
	file_object.write(' * ')
	file_object.write(str(K1_T_TR))
	file_object.write(' = ')
	file_object.write(str(T_TR_K1))

################################################    TTO-3
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTто-3')
	file_object.write(' = ')
	file_object.write(str(NTO_3_K_701_d))
	file_object.write(' * ')
	file_object.write(str(K1_T_TO_3))
	file_object.write(' = ')
	file_object.write(str(T_TO_3_K1))

################################################    TTO-2
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTто-2')
	file_object.write(' = ')
	file_object.write(str(NTO_2_K_701_d))
	file_object.write(' * ')
	file_object.write(str(K1_T_TO_2))
	file_object.write(' = ')
	file_object.write(str(T_TO_2_K1))
################################################    TTO-1
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTто-1')
	file_object.write(' = ')
	file_object.write(str(NTO_1_K_701_d))
	file_object.write(' * ')
	file_object.write(str(K1_T_TO_1))
	file_object.write(' = ')
	file_object.write(str(T_TO_1_K1))

################################################    TCTO
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTсто')
	file_object.write(' = ')
	file_object.write(str(K_701_N_CTO))
	file_object.write(' * ')
	file_object.write(str(K1_T_CTO))
	file_object.write(' = ')
	file_object.write(str(T_CTO_K1))



####################################################################
#                           DT-75
####################################################################


# w перезапись с удалением всего что было
# a дозапись с сохранением старого
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\n')
	file_object.write('\nДТ-75 МВ:')

################################################    TKR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTкр')
	file_object.write(' = ')
	file_object.write(str(NKR_DT_d))
	file_object.write(' * ')
	file_object.write(str(T_KR_DT))
	file_object.write(' = ')
	file_object.write(str(DT_T_KR))

################################################   TTR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTтр')
	file_object.write(' = ')
	file_object.write(str(NTR_DT_d))
	file_object.write(' * ')
	file_object.write(str(T_TR_DT))
	file_object.write(' = ')
	file_object.write(str(DT_T_TR))

################################################    TTO-3
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTто-3')
	file_object.write(' = ')
	file_object.write(str(NTO_3_DT_d))
	file_object.write(' * ')
	file_object.write(str(T_TO_3_DT))
	file_object.write(' = ')
	file_object.write(str(DT_T_TO_3))

################################################    TTO-2
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTто-2')
	file_object.write(' = ')
	file_object.write(str(NTO_2_DT_d))
	file_object.write(' * ')
	file_object.write(str(T_TO_2_DT))
	file_object.write(' = ')
	file_object.write(str(DT_T_TO_2))

################################################    TTO-1
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTто-1')
	file_object.write(' = ')
	file_object.write(str(NTO_1_DT_d))
	file_object.write(' * ')
	file_object.write(str(T_TO_1_DT))
	file_object.write(' = ')
	file_object.write(str(DT_T_TO_1))

################################################    TCTO
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTсто')
	file_object.write(' = ')
	file_object.write(str(DT_N_CTO))
	file_object.write(' * ')
	file_object.write(str(T_CTO_DT))
	file_object.write(' = ')
	file_object.write(str(DT_T_CTO))



####################################################################
#                           MTZ2
####################################################################

# w перезапись с удалением всего что было
# a дозапись с сохранением старого
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\n')
	file_object.write('\nМТЗ-82:')

################################################    TKR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTкр')
	file_object.write(' = ')
	file_object.write(str(NKR_MTZ2_d))
	file_object.write(' * ')
	file_object.write(str(T_KR_MTZ2))
	file_object.write(' = ')
	file_object.write(str(MTZ2_T_KR))

################################################   TTR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTтр')
	file_object.write(' = ')
	file_object.write(str(NTR_MTZ2_d))
	file_object.write(' * ')
	file_object.write(str(T_TR_MTZ2))
	file_object.write(' = ')
	file_object.write(str(MTZ2_T_TR))

################################################    TTO-3
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTто-3')
	file_object.write(' = ')
	file_object.write(str(NTO_3_MTZ2_d))
	file_object.write(' * ')
	file_object.write(str(T_TO_3_MTZ2))
	file_object.write(' = ')
	file_object.write(str(MTZ2_T_TO_3))

################################################    TTO-2
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTто-2')
	file_object.write(' = ')
	file_object.write(str(NTO_2_MTZ2_d))
	file_object.write(' * ')
	file_object.write(str(T_TO_2_MTZ2))
	file_object.write(' = ')
	file_object.write(str(MTZ2_T_TO_2))

################################################    TTO-1
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTто-1')
	file_object.write(' = ')
	file_object.write(str(NTO_1_MTZ2_d))
	file_object.write(' * ')
	file_object.write(str(T_TO_1_MTZ2))
	file_object.write(' = ')
	file_object.write(str(MTZ2_T_TO_1))

################################################    TCTO
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTсто')
	file_object.write(' = ')
	file_object.write(str(MTZ2_N_CTO))
	file_object.write(' * ')
	file_object.write(str(T_CTO_MTZ2))
	file_object.write(' = ')
	file_object.write(str(MTZ2_T_CTO))

####################################################################
#                           MZT
####################################################################

# w перезапись с удалением всего что было
# a дозапись с сохранением старого
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\n')
	file_object.write('\nМТЗ-80:')

################################################    TKR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTкр')
	file_object.write(' = ')
	file_object.write(str(NKR_MZT_d))
	file_object.write(' * ')
	file_object.write(str(T_KR_MZT))
	file_object.write(' = ')
	file_object.write(str(MZT_T_KR))

################################################   TTR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTтр')
	file_object.write(' = ')
	file_object.write(str(NTR_MZT_d))
	file_object.write(' * ')
	file_object.write(str(T_TR_MZT))
	file_object.write(' = ')
	file_object.write(str(MZT_T_TR))

################################################    TTO-3
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTто-3')
	file_object.write(' = ')
	file_object.write(str(NTO_3_MZT_d))
	file_object.write(' * ')
	file_object.write(str(T_TO_3_MZT))
	file_object.write(' = ')
	file_object.write(str(MZT_T_TO_3))

################################################    TTO-2
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTто-2')
	file_object.write(' = ')
	file_object.write(str(NTO_2_MZT_d))
	file_object.write(' * ')
	file_object.write(str(T_TO_2_MZT))
	file_object.write(' = ')
	file_object.write(str(MZT_T_TO_2))

################################################    TTO-1
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTто-1')
	file_object.write(' = ')
	file_object.write(str(NTO_1_MZT_d))
	file_object.write(' * ')
	file_object.write(str(T_TO_1_MZT))
	file_object.write(' = ')
	file_object.write(str(MZT_T_TO_1))

################################################    TCTO
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTсто')
	file_object.write(' = ')
	file_object.write(str(MZT_N_CTO))
	file_object.write(' * ')
	file_object.write(str(T_CTO_MZT))
	file_object.write(' = ')
	file_object.write(str(MZT_T_CTO))


####################################################################
#                           T-40
####################################################################


# w перезапись с удалением всего что было
# a дозапись с сохранением старого
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\n')
	file_object.write('\nT-40:')

################################################    TKR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTкр')
	file_object.write(' = ')
	file_object.write(str(NKR_T40_d))
	file_object.write(' * ')
	file_object.write(str(T_KR_T40))
	file_object.write(' = ')
	file_object.write(str(T40_T_KR))

################################################   TTR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTтр')
	file_object.write(' = ')
	file_object.write(str(NTR_T40_d))
	file_object.write(' * ')
	file_object.write(str(T_TR_T40))
	file_object.write(' = ')
	file_object.write(str(T40_T_TR))

################################################    TTO-3
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTто-3')
	file_object.write(' = ')
	file_object.write(str(NTO_3_T40_d))
	file_object.write(' * ')
	file_object.write(str(T_TO_3_T40))
	file_object.write(' = ')
	file_object.write(str(T40_T_TO_3))

################################################    TTO-2
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTто-2')
	file_object.write(' = ')
	file_object.write(str(NTO_2_T40_d))
	file_object.write(' * ')
	file_object.write(str(T_TO_2_T40))
	file_object.write(' = ')
	file_object.write(str(T40_T_TO_2))

################################################    TTO-1
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTто-1')
	file_object.write(' = ')
	file_object.write(str(NTO_1_T40_d))
	file_object.write(' * ')
	file_object.write(str(T_TO_1_T40))
	file_object.write(' = ')
	file_object.write(str(T40_T_TO_1))

################################################    TCTO
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTсто')
	file_object.write(' = ')
	file_object.write(str(T40_N_CTO))
	file_object.write(' * ')
	file_object.write(str(T_CTO_T40))
	file_object.write(' = ')
	file_object.write(str(T40_T_CTO))

####################################################################
#                           T25
####################################################################


# w перезапись с удалением всего что было
# a дозапись с сохранением старого
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\n')
	file_object.write('\nT-25:')

################################################    TKR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTкр')
	file_object.write(' = ')
	file_object.write(str(NKR_T25_d))
	file_object.write(' * ')
	file_object.write(str(T_KR_T25))
	file_object.write(' = ')
	file_object.write(str(T25_T_KR))

################################################   TTR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTтр')
	file_object.write(' = ')
	file_object.write(str(NTR_T25_d))
	file_object.write(' * ')
	file_object.write(str(T_TR_T25))
	file_object.write(' = ')
	file_object.write(str(T25_T_TR))

################################################    TTO-3
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTто-3')
	file_object.write(' = ')
	file_object.write(str(NTO_3_T25_d))
	file_object.write(' * ')
	file_object.write(str(T_TO_3_T25))
	file_object.write(' = ')
	file_object.write(str(T25_T_TO_3))

################################################    TTO-2
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTто-2')
	file_object.write(' = ')
	file_object.write(str(NTO_2_T25_d))
	file_object.write(' * ')
	file_object.write(str(T_TO_2_T25))
	file_object.write(' = ')
	file_object.write(str(T25_T_TO_2))

################################################    TTO-1
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTто-1')
	file_object.write(' = ')
	file_object.write(str(NTO_1_T25_d))
	file_object.write(' * ')
	file_object.write(str(T_TO_1_T25))
	file_object.write(' = ')
	file_object.write(str(T25_T_TO_1))

################################################    TCTO
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTсто')
	file_object.write(' = ')
	file_object.write(str(T25_N_CTO))
	file_object.write(' * ')
	file_object.write(str(T_CTO_T25))
	file_object.write(' = ')
	file_object.write(str(T25_T_CTO))

####################################################################
#                           T16
####################################################################


# w перезапись с удалением всего что было
# a дозапись с сохранением старого
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\n')
	file_object.write('\nT-16:')

################################################    TKR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTкр')
	file_object.write(' = ')
	file_object.write(str(NKR_T16_d))
	file_object.write(' * ')
	file_object.write(str(T_KR_T16))
	file_object.write(' = ')
	file_object.write(str(T16_T_KR))

################################################   TTR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTтр')
	file_object.write(' = ')
	file_object.write(str(NTR_T16_d))
	file_object.write(' * ')
	file_object.write(str(T_TR_T16))
	file_object.write(' = ')
	file_object.write(str(T16_T_TR))

################################################    TTO-3
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTто-3')
	file_object.write(' = ')
	file_object.write(str(NTO_3_T16_d))
	file_object.write(' * ')
	file_object.write(str(T_TO_3_T16))
	file_object.write(' = ')
	file_object.write(str(T16_T_TO_3))

################################################    TTO-2
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTто-2')
	file_object.write(' = ')
	file_object.write(str(NTO_2_T16_d))
	file_object.write(' * ')
	file_object.write(str(T_TO_2_T16))
	file_object.write(' = ')
	file_object.write(str(T16_T_TO_2))

################################################    TTO-1
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTто-1')
	file_object.write(' = ')
	file_object.write(str(NTO_1_T16_d))
	file_object.write(' * ')
	file_object.write(str(T_TO_1_T16))
	file_object.write(' = ')
	file_object.write(str(T16_T_TO_1))

################################################    TCTO
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTсто')
	file_object.write(' = ')
	file_object.write(str(T16_N_CTO))
	file_object.write(' * ')
	file_object.write(str(T_CTO_T16))
	file_object.write(' = ')
	file_object.write(str(T16_T_CTO))



####################################################################
#                           УАЗ-469
####################################################################


# w перезапись с удалением всего что было
# a дозапись с сохранением старого
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\n')
	file_object.write('\nУАЗ-469:')

################################################    TKR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTкр')
	file_object.write(' = ')
	file_object.write(str(NKR_UAZ_d))
	file_object.write(' * ')
	file_object.write(str(UAZ_T_KR))
	file_object.write(' = ')
	file_object.write(str(T_KR_UAZ))

################################################   TTR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-1')
	file_object.write(' = ')
	file_object.write(str(UAZ_T_TR_U1))
	file_object.write(' * ')
	file_object.write(str(UAZ))
	file_object.write(' / ')
	file_object.write(str(UAZ_T_TR_D))
	file_object.write(' * ')
	file_object.write(str(UAZ_T_TR_Z))
	file_object.write(' = ')
	file_object.write(str(T_TR_UAZ))

################################################    TTO-2
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTто-2')
	file_object.write(' = ')
	file_object.write(str(NTO_2_UAZ_d))
	file_object.write(' * ')
	file_object.write(str(UAZ_T_TO_2))
	file_object.write(' = ')
	file_object.write(str(T_TO_2_UAZ))

################################################    TTO-1
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTто-1')
	file_object.write(' = ')
	file_object.write(str(NTO_1_UAZ_d))
	file_object.write(' * ')
	file_object.write(str(UAZ_T_TO_1))
	file_object.write(' = ')
	file_object.write(str(T_TO_1_UAZ))

################################################    TCTO
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTсто')
	file_object.write(' = ')
	file_object.write(str(UAZ_NCTO))
	file_object.write(' * ')
	file_object.write(str(UAZ_T_CTO))
	file_object.write(' = ')
	file_object.write(str(T_CTO_UAZ))



####################################################################
#                           КАМАЗ-5320
####################################################################


# w перезапись с удалением всего что было
# a дозапись с сохранением старого
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\n')
	file_object.write('\nКАМАЗ-5320:')

################################################    TKR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTкр')
	file_object.write(' = ')
	file_object.write(str(NKR_KAMAZ_d))
	file_object.write(' * ')
	file_object.write(str(KAMAZ_T_KR))
	file_object.write(' = ')
	file_object.write(str(T_KR_KAMAZ))

################################################   TTR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-1')
	file_object.write(' = ')
	file_object.write(str(KAMAZ_T_TR_U1))
	file_object.write(' * ')
	file_object.write(str(KAMAZ))
	file_object.write(' / ')
	file_object.write(str(KAMAZ_T_TR_D))
	file_object.write(' * ')
	file_object.write(str(KAMAZ_T_TR_Z))
	file_object.write(' = ')
	file_object.write(str(T_TR_KAMAZ))

################################################    TTO-2
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTто-2')
	file_object.write(' = ')
	file_object.write(str(NTO_2_KAMAZ_d))
	file_object.write(' * ')
	file_object.write(str(KAMAZ_T_TO_2))
	file_object.write(' = ')
	file_object.write(str(T_TO_2_KAMAZ))

################################################    TTO-1
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTто-1')
	file_object.write(' = ')
	file_object.write(str(NTO_1_KAMAZ_d))
	file_object.write(' * ')
	file_object.write(str(KAMAZ_T_TO_1))
	file_object.write(' = ')
	file_object.write(str(T_TO_1_KAMAZ))

################################################    TCTO
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTсто')
	file_object.write(' = ')
	file_object.write(str(KAMAZ_NCTO))
	file_object.write(' * ')
	file_object.write(str(KAMAZ_T_CTO))
	file_object.write(' = ')
	file_object.write(str(T_CTO_KAMAZ))

####################################################################
#                           ГАЗ-53
####################################################################


# w перезапись с удалением всего что было
# a дозапись с сохранением старого
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\n')
	file_object.write('\nГАЗ-53:')

################################################    TKR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTкр')
	file_object.write(' = ')
	file_object.write(str(NKR_GAZ_d))
	file_object.write(' * ')
	file_object.write(str(GAZ_T_KR))
	file_object.write(' = ')
	file_object.write(str(T_KR_GAZ))

################################################   TTR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-1')
	file_object.write(' = ')
	file_object.write(str(GAZ_T_TR_U1))
	file_object.write(' * ')
	file_object.write(str(GAZ))
	file_object.write(' / ')
	file_object.write(str(GAZ_T_TR_D))
	file_object.write(' * ')
	file_object.write(str(GAZ_T_TR_Z))
	file_object.write(' = ')
	file_object.write(str(T_TR_GAZ))

################################################    TTO-2
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTто-2')
	file_object.write(' = ')
	file_object.write(str(NTO_2_GAZ_d))
	file_object.write(' * ')
	file_object.write(str(GAZ_T_TO_2))
	file_object.write(' = ')
	file_object.write(str(T_TO_2_GAZ))

################################################    TTO-1
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTто-1')
	file_object.write(' = ')
	file_object.write(str(NTO_1_GAZ_d))
	file_object.write(' * ')
	file_object.write(str(GAZ_T_TO_1))
	file_object.write(' = ')
	file_object.write(str(T_TO_1_GAZ))

################################################    TCTO
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTсто')
	file_object.write(' = ')
	file_object.write(str(GAZ_NCTO))
	file_object.write(' * ')
	file_object.write(str(GAZ_T_CTO))
	file_object.write(' = ')
	file_object.write(str(T_CTO_GAZ))

####################################################################
#                           ЗИЛ-130
####################################################################


# w перезапись с удалением всего что было
# a дозапись с сохранением старого
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\n')
	file_object.write('\nЗИЛ-130:')

################################################    TKR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTкр')
	file_object.write(' = ')
	file_object.write(str(NKR_ZIL_d))
	file_object.write(' * ')
	file_object.write(str(ZIL_T_KR))
	file_object.write(' = ')
	file_object.write(str(T_KR_ZIL))

################################################   TTR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-1')
	file_object.write(' = ')
	file_object.write(str(ZIL_T_TR_U1))
	file_object.write(' * ')
	file_object.write(str(ZIL))
	file_object.write(' / ')
	file_object.write(str(ZIL_T_TR_D))
	file_object.write(' * ')
	file_object.write(str(ZIL_T_TR_Z))
	file_object.write(' = ')
	file_object.write(str(T_TR_ZIL))

################################################    TTO-2
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTто-2')
	file_object.write(' = ')
	file_object.write(str(NTO_2_ZIL_d))
	file_object.write(' * ')
	file_object.write(str(ZIL_T_TO_2))
	file_object.write(' = ')
	file_object.write(str(T_TO_2_ZIL))

################################################    TTO-1
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTто-1')
	file_object.write(' = ')
	file_object.write(str(NTO_1_ZIL_d))
	file_object.write(' * ')
	file_object.write(str(ZIL_T_TO_1))
	file_object.write(' = ')
	file_object.write(str(T_TO_1_ZIL))

################################################    TCTO
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTсто')
	file_object.write(' = ')
	file_object.write(str(ZIL_NCTO))
	file_object.write(' * ')
	file_object.write(str(ZIL_T_CTO))
	file_object.write(' = ')
	file_object.write(str(T_CTO_ZIL))


####################################################################
#                           CK-5
####################################################################


# w перезапись с удалением всего что было
# a дозапись с сохранением старого
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\n')
	file_object.write('\nCK-5:')

################################################    NKR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNкр')
	file_object.write(' = ')
	file_object.write(str(NKR_CK_d))
	file_object.write(' * ')
	file_object.write(str(CK_T_KR))
	file_object.write(' = ')
	file_object.write(str(T_KR_CK))

################################################   NTR
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNтр')
	file_object.write(' = ')
	file_object.write(str(NTR_CK_d))
	file_object.write(' * ')
	file_object.write(str(CK_T_TR))
	file_object.write(' = ')
	file_object.write(str(T_TR_CK))

################################################    NTO-2
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-2')
	file_object.write(' = ')
	file_object.write(str(NTO_2_CK_d))
	file_object.write(' * ')
	file_object.write(str(CK_T_TO_2))
	file_object.write(' = ')
	file_object.write(str(T_TO_2_CK))

################################################    NTO-1
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNто-1')
	file_object.write(' = ')
	file_object.write(str(NTO_1_CK_d))
	file_object.write(' * ')
	file_object.write(str(CK_T_TO_1))
	file_object.write(' = ')
	file_object.write(str(T_TO_1_CK))

################################################    NCTO
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNсто')
	file_object.write(' = ')
	file_object.write(str(CK_NCTO))
	file_object.write(' * ')
	file_object.write(str(CK_T_CTO))
	file_object.write(' = ')
	file_object.write(str(T_CTO_CK))




####################################################################
#                           PLN-4-35
####################################################################


# w перезапись с удалением всего что было
# a дозапись с сохранением старого
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\n')
	file_object.write('\nПЛН-4-35:')

################################################    TTR

with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTтр')
	file_object.write(' = ')
	file_object.write(str(PLN_NTR_d))
	file_object.write(' * ')
	file_object.write(str(T_TR_PLN))
	file_object.write(' = ')
	file_object.write(str(PLN_T_TR))

################################################    TCTO

with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nTпсто')
	file_object.write(' = ')
	file_object.write(str(PLN_NCTO))
	file_object.write(' * ')
	file_object.write(str(T_CTO_PLN))
	file_object.write(' = ')
	file_object.write(str(PLN_T_CTO))



####################################################################
#                           SZ-3-6
####################################################################


# w перезапись с удалением всего что было
# a дозапись с сохранением старого
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\n')
	file_object.write('\nСЗ-3-6')

################################################    ТTR

with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nТтр')
	file_object.write(' = ')
	file_object.write(str(SZ_NTR_d))
	file_object.write(' * ')
	file_object.write(str(T_TR_SZ))
	file_object.write(' = ')
	file_object.write(str(SZ_T_TR))

################################################    ТCTO

with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nТпсто')
	file_object.write(' = ')
	file_object.write(str(SZ_NCTO))
	file_object.write(' * ')
	file_object.write(str(T_CTO_SZ))
	file_object.write(' = ')
	file_object.write(str(SZ_T_CTO))



####################################################################
#                           KKU-2
####################################################################


# w перезапись с удалением всего что было
# a дозапись с сохранением старого
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\n')
	file_object.write('\nККУ-2А')

################################################    ТTR

with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nТтр')
	file_object.write(' = ')
	file_object.write(str(KKU_NTR_d))
	file_object.write(' * ')
	file_object.write(str(T_TR_KKU))
	file_object.write(' = ')
	file_object.write(str(KKU_T_TR))

################################################    ТCTO

with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nТпсто')
	file_object.write(' = ')
	file_object.write(str(KKU_NCTO))
	file_object.write(' * ')
	file_object.write(str(T_CTO_KKU))
	file_object.write(' = ')
	file_object.write(str(KKU_T_CTO))



####################################################################
#                           BDT-3
####################################################################


# w перезапись с удалением всего что было
# a дозапись с сохранением старого
with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\n')
	file_object.write('\nБДТ-3')

################################################    NTR

with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNтр')
	file_object.write(' = ')
	file_object.write(str(BDT_NTR_d))
	file_object.write(' * ')
	file_object.write(str(T_TR_BDT))
	file_object.write(' = ')
	file_object.write(str(BDT_T_TR))

################################################    NCTO

with open('KURSOVAYA_v1.txt', 'a')as file_object:
	file_object.write('\nNсто')
	file_object.write(' = ')
	file_object.write(str(BDT_NCTO))
	file_object.write(' * ')
	file_object.write(str(T_CTO_BDT))
	file_object.write(' = ')
	file_object.write(str(BDT_T_CTO))


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

