from constants import *

def int_round(num):
	num = int(num + (0.5 if num > 0 else -0.5))
	return num

def calculate_N(
		 NKR_U:int,  NKR_N:int, 
		 NTR_N:int,  NTO_3_N:int,
		 NTO_2_N:int,  NTO_1_N:int, 
		 NCTO:int, count :int):

	NKR  = NKR_U * count / NKR_N # Nкр
	NKR_d = int_round (NKR )
	NTR  = NKR_U * count / NTR_N - NKR_d # Nтр
	NTR_d = int_round(NTR ) 
	NTO_3  = NKR_U * count / NTO_3_N - NKR_d - NTR_d # Nто-3
	NTO_3_d = int_round(NTO_3 ) 
	NTO_2  = NKR_U * count / NTO_2_N - NKR_d - NTR_d - NTO_3_d # Nто-2
	NTO_2_d = int_round(NTO_2 ) 
	NTO_1  = NKR_U * count / NTO_1_N - NKR_d - NTR_d - NTO_3_d - NTO_2_d # Nто-1
	NTO_1_d = int_round(NTO_1 ) 
	N_CTO = NCTO * count # Nсто


	NKR_str = f"Nкр = {NKR_U} * {count} / {NKR_N} = {NKR}\nПринимаю: {NKR_d}"
	NTR_str = f"Nтр = {NKR_U} * {count} / {NTR_N} - {NKR_d} = {NTR}\nПринимаю: {NTR_d}"
	NTO_3_str = f"Nто-3 = {NKR_U} * {count} / {NTO_3_N} - {NKR_d} - {NTR_d} = {NTO_3}\nПринимаю: {NTO_3_d}"
	NTO_2_str = f"Nто-2 = {NKR_U} * {count} / {NTO_2_N} - {NKR_d} - {NTR_d} - {NTO_3_d} = {NTO_2}\nПринимаю: {NTO_2_d}"
	NTO_1_str = f"Nто-1 = {NKR_U} * {count} / {NTO_1_N} - {NKR} - {NTR} - {NTO_3} - {NTO_2} = {NTO_1}\nПринимаю: {NTO_1_d}"
	N_CTO_str = f"Nсто = {NCTO} * {count} = {N_CTO}"