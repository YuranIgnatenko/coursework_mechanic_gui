from constants import *
from models import *
from constants import *

CONST_MODE_N_WORK = 1
CONST_MODE_T_WORK = 2
CONST_MODE_DATA_VAR = 3

class Calculator():
	def __init__(self):
		pass

	def round(self, num:float) -> int:
		num = int(num + (0.5 if num > 0 else -0.5))
		return num

class CalculatorDiesel(Calculator):	
	def __init__(self, data:ModelDataDiesel, count:int):
		self.data = data
		self.count = count 
	
	def get_N(self) -> tuple[DataDieselResultN,str]:
		NKR  = self.data.NKR_U * self.count / self.data.NKR_N
		NTR  = self.data.NKR_U * self.count / self.data.NTR_N - self.round(NKR)
		NTO_3  = self.data.NKR_U * self.count / self.data.NTO_3_N - self.round(NKR) - self.round(NTR) 
		NTO_2  = self.data.NKR_U * self.count / self.data.NTO_2_N - self.round(NKR) - self.round(NTR) - self.round(NTO_3)
		NTO_1  = self.data.NKR_U * self.count / self.data.NTO_1_N - self.round(NKR) - self.round(NTR) - self.round(NTO_3) - self.round(NTO_2) 
		N_CTO = self.data.NCTO * self.count 

		output_string = "\n\n"
		output_string += f"Nкр = {self.data.NKR_U} * {self.count} / {self.data.NKR_N} = {NKR}\nПринимаю: {self.round(NKR)}\n"
		output_string += f"Nтр = {self.data.NKR_U} * {self.count} / {self.data.NTR_N} - {self.round(NKR)} = {NTR}\nПринимаю: {self.round(NTR)}\n"
		output_string += f"Nто-3 = {self.data.NKR_U} * {self.count} / {self.data.NTO_3_N} - {self.round(NKR)} - {self.round(NTR)} = {NTO_3}\nПринимаю: {self.round(NTO_3)}\n"
		output_string += f"Nто-2 = {self.data.NKR_U} * {self.count} / {self.data.NTO_2_N} - {self.round(NKR)} - {self.round(NTR)} - {self.round(NTO_3)} = {NTO_2}\nПринимаю: {self.round(NTO_2)}\n"
		output_string += f"Nто-1 = {self.data.NKR_U} * {self.count} / {self.data.NTO_1_N} - {self.round(NKR)} - {self.round(NTR)} - {self.round(NTO_3)} - {self.round(NTO_2)} = {NTO_1}\nПринимаю: {self.round(NTO_1)}\n"
		output_string += f"Nсто = {self.data.NCTO} * {self.count} = {N_CTO}"

		NKR = self.round(NKR)
		NTR = self.round(NTR)
		NTO_3 = self.round(NTO_3)
		NTO_2 = self.round(NTO_2)
		NTO_1 = self.round(NTO_1)
		N_CTO = self.round(N_CTO)

		storage_result_calc_n = DataDieselResultN(NKR,NTR,NTO_3,NTO_2,NTO_1,N_CTO)

		return (storage_result_calc_n, output_string)
	
	def get_T(self)-> tuple[DataDieselResultT, str]:
		output_get_n, _ = self.get_N()
		TKR = output_get_n.NKR * self.data.TKR
		TTR = output_get_n.NTR * self.data.TTR
		TTO_3 = output_get_n.NTO_3 * self.data.TTO_3
		TTO_2 = output_get_n.NTO_2 * self.data.TTO_2
		TTO_1 = output_get_n.NTO_1 * self.data.TTO_1
		TCTO = output_get_n.N_CTO * self.data.TCTO

		output_string = "\n\n"
		output_string += f"Tкр = {output_get_n.NKR} * {self.data.TKR} = {TKR}\n"
		output_string += f"Tтр = {output_get_n.NTR} * {self.data.TTR} = {TTR}\n"
		output_string += f"Tто-3 = {output_get_n.NTO_3} * {self.data.TTO_3} = {TTO_3}\n"
		output_string += f"Tто-2 = {output_get_n.NTO_2} * {self.data.TTO_2} = {TTO_2}\n"
		output_string += f"Tто-1 = {output_get_n.NTO_1} * {self.data.TTO_1} = {TTO_1}\n"
		output_string += f"Tсто = {output_get_n.N_CTO} * {self.data.TCTO} = {TCTO}\n"

		storage_result_calc_t = DataDieselResultT(TKR,TTR,TTO_3,TTO_2,TTO_1,TCTO)

		return (storage_result_calc_t, output_string)

class CalculatorAgromachine(Calculator):
	def __init__(self, data:ModelDataAgromachine, count:int):
		self.data = data
		self.count = count 
	
	def get_N(self) -> tuple[DataAgromachineResultN,str]:
		NTR = self.count * self.data.NTR
		NCTO = self.count * self.data.NCTO

		output_string = "\n\n"
		output_string += f"Nтр = {self.count} * {self.data.NTR} = {NTR}\nПринимаю: {self.round(NTR)}\n"
		output_string += f"Nсто = {self.count} * {self.data.NCTO} = {NCTO}\n"

		NTR = self.round(NTR)

		storage_result_calc_n = DataAgromachineResultN(NTR, NCTO)

		return (storage_result_calc_n, output_string)
	
	def get_T(self)-> tuple[DataAgromachineResultT, str]:
		output_get_n, _ = self.get_N()
		TTR = output_get_n.NTR * self.data.TTR
		TCTO = output_get_n.NCTO * self.data.TCTO

		output_string = "\n\n"
		output_string += f"Tтр = {output_get_n.NTR} * {self.data.TTR} = {TTR}\n"
		output_string += f"Tсто = {output_get_n.NCTO} * {self.data.TCTO} = {TCTO}\n"

		storage_result_calc_t = DataAgromachineResultT(TTR,TCTO)

		return (storage_result_calc_t, output_string)
	
class CalculatorCombine(Calculator):
	def __init__(self, data:ModelDataCombine, count:int):
		self.data = data
		self.count = count 
	
	def get_N(self) -> tuple[DataCombineResultN,str]:
		NKR = self.count * self.data.NKR
		NTR = self.count * self.data.NTR
		NTO_2 = self.data.NTO * self.count / self.data.NTO_2 - NKR - NTR
		NTO_1 = self.data.NTO * self.count / self.data.NTO_1 - NKR -  NTR - NTO_2 
		NCTO = self.count * self.data.NCTO

		output_string = "\n\n"
		output_string += f"Nкр = {self.count} * {self.data.NKR} = {NKR}\nПринимаю: {self.round(NKR)}\n"
		output_string += f"Nтр = {self.count} * {self.data.NTR} = {NTR}\nПринимаю: {self.round(NTR)}\n"
		output_string += f"Nто-2 = {self.data.NTO} * {self.count} / {self.data.NTO_2} - {self.round(NKR)} - {self.round(NTR)} = {NTO_2}\nПринимаю: {NTO_2}\n"
		output_string += f"Nто-1 = {self.data.NTO} * {self.count} / {self.data.NTO_1} - {self.round(NKR)} - {self.round(NTR)} - {NTO_2} = {NTO_1}\nПринимаю: {NTO_1}\n"
		output_string += f"Nсто = {self.count} * {NCTO} = {NCTO}"

		NKR = self.round(NKR) 
		NTR = self.round(NTR)
		NTO_2 = self.round(NTO_2)
		NTO_1 = self.round(NTO_1) 

		storage_result_calc_n = DataCombineResultN(NKR,NTR,NTO_2,NTO_1,NCTO)

		return (storage_result_calc_n, output_string)
	
	def get_T(self)-> tuple[DataCombineResultT, str]:
		output_get_n, _ = self.get_N()
		TKR = output_get_n.NKR * self.data.TKR
		TTR = output_get_n.NTR * self.data.TTR
		TTO_2 = output_get_n.NTO_2 * self.data.TTO_2
		TTO_1 = output_get_n.NTO_1 * self.data.TTO_1
		TCTO = output_get_n.N_CTO * self.data.TCTO

		output_string = "\n\n"
		output_string += f"Tкр = {output_get_n.NKR} * {self.data.TKR} = {TKR}\n"
		output_string += f"Tтр = {output_get_n.NTR} * {self.data.TTR} = {TTR}\n"
		output_string += f"Tто-2 = {output_get_n.NTO_2} * {self.data.TTO_2} = {TTO_2}\n"
		output_string += f"Tто-1 = {output_get_n.NTO_1} * {self.data.TTO_1} = {TTO_1}\n"
		output_string += f"Tсто = {output_get_n.N_CTO} * {self.data.TCTO} = {TCTO}\n"

		storage_result_calc_t = DataCombineResultT(TKR,TTR,TTO_2,TTO_1,TCTO)

		return (storage_result_calc_t, output_string)

class CalculatorCar(Calculator):
	def __init__(self, data:ModelDataCar, count:int):
		self.data = data
		self.count = count 
	
	def get_N(self) -> tuple[DataCarResultN,str]:
		NKR = int (self.data.NKR_U) * self.count / self.data.NKR_N 
		NTO_2 = self.data.NKR_U * self.count / self.data.NTO_2_N - self.round(NKR)
		NTO_1 = self.data.NKR_U * self.count / self.data.NTO_1_N - self.round(NKR) - self.round(NTO_2)
		N_CTO = self.data.NCTO * self.count

		output_string = "\n\n"
		output_string += f"Nкр = {self.data.NKR_U} * {self.count} / {self.data.NKR_N} = {NKR}\nПринимаю: {self.round(NKR)}\n"
		output_string += f"Nто-2 = {self.data.NKR_U} * {self.count} / {self.data.NTO_2_N} - {NKR} = {NTO_2}\nПринимаю: {self.round(NTO_2)}\n"
		output_string += f"Nто-1 = {self.data.NKR_U} * {self.count} / {self.data.NTO_1_N} - {NKR} - {NTO_2} = {NTO_1}\nПринимаю: {self.round(NTO_1)}\n"
		output_string += f"Nсто = {self.data.NCTO} * {self.count} = {N_CTO}\n"
		
		NKR = self.round(NKR)
		NTO_2 = self.round(NTO_2) 
		NTO_1 = self.round(NTO_1)

		storage_result_calc_n = DataCarResultN(NKR,NTO_2,NTO_1,N_CTO)
		
		return (storage_result_calc_n, output_string)
	
	def get_T(self)-> tuple[DataCarResultT, str]:
		output_get_n, _ = self.get_N()

		TKR = output_get_n.NKR * self.data.TKR
		TTR = self.data.TTR_U1 * self.count / self.data.TTR_D * self.data.TTR_Z
		TTO_2 = output_get_n.NTO_2 * self.data.TTO_2
		TTO_1 = output_get_n.NTO_1 * self.data.TTO_1
		TCTO = output_get_n.N_CTO * self.data.TCTO

		output_string = "\n\n"
		output_string += f"Tкр = {output_get_n.NKR} * {self.data.TKR} = {TKR}\n"
		output_string += f"Tтр = {self.data.TTR_U1} * {self.count} / {self.data.TTR_D} = {TTR}\n"
		output_string += f"Tто-2 = {output_get_n.NTO_2} * {self.data.TTO_2} = {TTO_2}\n"
		output_string += f"Tто-1 = {output_get_n.NTO_1} * {self.data.TTO_1} = {TTO_1}\n"
		output_string += f"Tсто = {self.data.NCTO} * {self.data.TCTO} = {TCTO}\n"

		storage_result_calc_t = DataCarResultT(TKR,TTR,TTO_2,TTO_1,TCTO)

		return (storage_result_calc_t, output_string)
	
