from constants import *
from models import *

class Calculator():
	def __init__(self):
		pass

	def round_number(self, num:float) -> int:
		num = int(num + (0.5 if num > 0 else -0.5))
		return num

class CalculatorDiesel(Calculator):	
	def __init__(self, data:ModelDataDiesel, count:int):
		self.data = data
		self.count = count 
	
	def get_N(self) -> tuple[DataDieselResultN,DataDieselStringN]:
		NKR  = self.data.NKR_U * self.count / self.data.NKR_N
		NKR_round = self.round_number (NKR )
		NTR  = self.data.NKR_U * self.count / self.data.NTR_N - NKR_round
		NTR_round = self.round_number(NTR ) 
		NTO_3  = self.data.NKR_U * self.count / self.data.NTO_3_N - NKR_round - NTR_round 
		NTO_3_round = self.round_number(NTO_3 ) 
		NTO_2  = self.data.NKR_U * self.count / self.data.NTO_2_N - NKR_round - NTR_round - NTO_3_round
		NTO_2_round = self.round_number(NTO_2 ) 
		NTO_1  = self.data.NKR_U * self.count / self.data.NTO_1_N - NKR_round - NTR_round - NTO_3_round - NTO_2_round 
		NTO_1_round = self.round_number(NTO_1 ) 
		N_CTO = self.data.NCTO * self.count 

		NKR_str = f"Nкр = {self.data.NKR_U} * {self.count} / {self.data.NKR_N} = {NKR}\nПринимаю: {NKR_round}"
		NTR_str = f"Nтр = {self.data.NKR_U} * {self.count} / {self.data.NTR_N} - {NKR_round} = {NTR}\nПринимаю: {NTR_round}"
		NTO_3_str = f"Nто-3 = {self.data.NKR_U} * {self.count} / {self.data.NTO_3_N} - {NKR_round} - {NTR_round} = {NTO_3}\nПринимаю: {NTO_3_round}"
		NTO_2_str = f"Nто-2 = {self.data.NKR_U} * {self.count} / {self.data.NTO_2_N} - {NKR_round} - {NTR_round} - {NTO_3_round} = {NTO_2}\nПринимаю: {NTO_2_round}"
		NTO_1_str = f"Nто-1 = {self.data.NKR_U} * {self.count} / {self.data.NTO_1_N} - {NKR} - {NTR} - {NTO_3} - {NTO_2} = {NTO_1}\nПринимаю: {NTO_1_round}"
		N_CTO_str = f"Nсто = {self.data.NCTO} * {self.count} = {N_CTO}"

		storage_result_calc_n = DataDieselResultN(NKR,NKR_round,NTR,NTR_round,NTO_3,NTO_3_round,NTO_2,NTO_2_round,NTO_1,NTO_1_round,N_CTO)
		storage_result_string_n = DataDieselStringN(NKR_str,NTR_str,NTO_3_str,NTO_2_str,NTO_1_str,N_CTO_str)

		return (storage_result_calc_n, storage_result_string_n)
	
	# def get_T(self)-> tuple[DataResultT, DataStringT]:
	# 	pass



class CalculatorAgromachine(Calculator):
	def __init__(self, data:ModelDataAgromachine, count:int):
		self.data = data
		self.count = count 
	
	def get_N(self) -> tuple[DataAgromachineResultN,DataAgromachineResultN]:
		NTR = self.count * self.data.NTR
		NTR_round = self.round_number(NTR)
		NCTO = self.count * self.data.NCTO

		NTR_str = f"Nтр = {self.count} * {self.data.NTR} = {NTR}\nПринимаю: {NTR_round}"
		NCTO_str = f"Nсто = {self.count} * {self.data.NCTO} = {NCTO}"

		storage_result_calc_n = DataAgromachineResultN(NTR, NTR_round, NCTO)
		storage_result_string_n = DataAgromachineStringN(NTR_str, NCTO_str)

		return (storage_result_calc_n, storage_result_string_n)
	
	# def get_T(self)-> tuple[StorageResultCalculateT,StorageResultStringT]:
		# pass
	


class CalculatorCombine(Calculator):
	def __init__(self, data:ModelDataCombine, count:int):
		self.data = data
		self.count = count 
	
	def get_N(self) -> tuple[DataCombineResultN,DataCombineResultN]:

		NKR = self.count * self.data.NKR
		NKR_round = self.round_number(NKR) 

		NTR = self.count * self.data.NTR
		NTR_round = self.round_number(NTR)

		NTO_2 = self.data.NTO * self.count / self.data.NTO_2 - NKR - NTR
		NTO_2_round = self.round_number(NTO_2)

		NTO_1 = self.data.NTO * self.count / self.data.NTO_1 - NKR -  NTR - NTO_2 
		NTO_1_round = self.round_number(NTO_1) 

		NCTO = self.count * self.data.NCTO

		NKR_str = f"Nкр = {self.count} * {self.data.NKR} = {NKR}\nПринимаю: {NKR_round}"
		NTR_str = f"Nтр = {self.count} * {self.data.NTR} = {NTR}\nПринимаю: {NTR_round}"
		NTO_2_str = f"Nто-2 = {self.data.NTO} * {self.count} / {self.data.NTO_2} - {NKR_round} - {NTR_round} = {NTO_2}\nПринимаю: {NTO_2}"
		NTO_1_str = f"Nто-1 = {self.data.NTO} * {self.count} / {self.data.NTO_1} - {NKR_round} - {NTR_round} - {NTO_2} = {NTO_1}\nПринимаю: {NTO_1}"
		NCTO_str = f"Nсто = {self.count} * {NCTO} = {NCTO}"

		storage_result_calc_n = DataCombineResultN(NKR,NKR_round,NTR,NTR_round,NTO_2,NTO_2_round,NTO_1,NTO_1_round,NCTO)
		storage_result_string_n = DataCombineStringN(NKR_str,NTR_str,NTO_2_str,NTO_1_str,NCTO_str)

		return (storage_result_calc_n, storage_result_string_n)
	
	# def get_T(self)-> tuple[StorageResultCalculateT,StorageResultStringT]:
		# pass



class CalculatorCar(Calculator):
	def __init__(self, data:ModelDataCar, count:int):
		self.data = data
		self.count = count 
	
	def get_N(self) -> tuple[DataCarResultN,DataCarResultN]:
		NKR = int (self.data.NKR_U) * self.count / self.data.NKR_N 
		NKR_round = self.round_number(NKR) 

		NTO_2 = self.data.NKR_U * self.count / self.data.NTO_2_N - NKR_round
		NTO_2_round = self.round_number(NTO_2) 

		NTO_1 = self.data.NKR_U * self.count / self.data.NTO_1_N - NKR_round - NTO_2_round
		NTO_1_round = self.round_number(NTO_1)

		N_CTO = self.data.NCTO * self.count


		NKR_str = f"Nкр = {self.data.NKR_U} * {self.count} / {self.data.NKR_N} = {NKR}\nПринимаю: {NKR}"
		# NKR = NKR_round
		NTO_2_str = f"Nто-2 = {self.data.NKR_U} * {self.count} / {self.data.NTO_2_N} - {NKR} = {NTO_2}\nПринимаю: {NTO_2}"
		# NTO_2_ZIL = NTO_2_ZIL_d
		NTO_1_str = f"Nто-1 = {self.data.NKR_U} * {self.count} / {self.data.NTO_1_N} - {NKR} - {NTO_2} = {NTO_1}\nПринимаю: {NTO_1}"
		# NTO_1_ZIL = NTO_1_ZIL_d
		N_CTO_str = f"Nсто = {self.data.NCTO} * {self.count} = {N_CTO}"

		storage_result_calc_n = DataCarResultN(NKR,NKR_round,NTO_2,NTO_2_round,NTO_1,NTO_1_round,N_CTO)
		storage_result_string_n = DataCarStringN(NKR_str,NTO_2_str,NTO_1_str,N_CTO_str)
		
		return (storage_result_calc_n, storage_result_string_n)
	
	# def get_T(self)-> tuple[StorageResultCalculateT,StorageResultStringT]:
		# pass