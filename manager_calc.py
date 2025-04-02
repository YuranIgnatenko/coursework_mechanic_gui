from constants import *

class StorageResultCalculateN():
	def __init__(self,NKR,NKR_round,NTR,NTR_round,NTO_3,NTO_3_round,NTO_2,NTO_2_round,NTO_1,NTO_1_round,N_CTO):
		self.NKR = NKR
		self.NKR_round = NKR_round
		self.NTR = NTR
		self.NTR_round = NTR_round
		self.NTO_3 = NTO_3
		self.NTO_3_round = NTO_3_round
		self.NTO_2 = NTO_2
		self.NTO_2_round = NTO_2_round
		self.NTO_1 = NTO_1
		self.NTO_1_round = NTO_1_round
		self.N_CTO = N_CTO

class StorageResultStringN():
	def __init__(self,NKR_str,NTR_str,NTO_3_str,NTO_2_str,NTO_1_str,N_CTO_str):
		self.NKR_str = NKR_str
		self.NTR_str = NTR_str
		self.NTO_3_str = NTO_3_str
		self.NTO_2_str = NTO_2_str
		self.NTO_1_str = NTO_1_str
		self.N_CTO_str = N_CTO_str
	def to_str(self) -> str:
		res = "\n".join([self.NKR_str,self.NTR_str,self.NTO_3_str,self.NTO_2_str,self.NTO_1_str,self.N_CTO_str])
		return res

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
	
	def get_N(self) -> tuple[StorageResultCalculateN,StorageResultStringN]:
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

		storage_result_calc_n = StorageResultCalculateN(NKR,NKR_round,NTR,NTR_round,NTO_3,NTO_3_round,NTO_2,NTO_2_round,NTO_1,NTO_1_round,N_CTO)
		storage_result_string_n = StorageResultStringN(NKR_str,NTR_str,NTO_3_str,NTO_2_str,NTO_1_str,N_CTO_str)

		return (storage_result_calc_n, storage_result_string_n)
	
