from constants import *
from models import *
from manager_output import *
from constants import *
from prettytable import PrettyTable

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
	

class TableDiesels():
	def __init__(self, list_calc_diesel:list[CalculatorDiesel]):
		self.diesels = list_calc_diesel
		
	def table(self, mode:str) -> str:
		'''mode: 'N' for calc_N, 'T' for calc_T'''
		td = []
		if mode == CONST_MODE_N_WORK:
			th = ['МАРКА', 'КОЛ-ВО', 'NКР', 'NТР', 'NТО-3', 'NTO-2', 'NTO-1', 'NCTO']
			for diesel in self.diesels:
				out = diesel.get_N()[0]
				td.extend([diesel.data.NAME, diesel.count, out.NKR, 
					out.NTR, out.NTO_3, out.NTO_2,
					out.NTO_1, out.N_CTO])
		elif mode == CONST_MODE_T_WORK:
			th = ['МАРКА', 'КОЛ-ВО', 'TКР', 'TТР', 'TТО-3', 'TTO-2', 'TTO-1', 'TCTO']
			for diesel in self.diesels:
				out = diesel.get_T()[0]
				td.extend([diesel.data.NAME, diesel.count, out.TKR, 
					out.TTR, out.TTO_3, out.TTO_2,
					out.TTO_1, out.T_CTO])
		elif mode == CONST_MODE_DATA_VAR:
			th = ['МАРКА', 'КОЛ-ВО', 
		 			'NKR_N', 'NKR_U', 'NТО-1', 'NTO-2', 'NTO-3', 'NCTO',
		 			'TKR', 'TTR', 'TТО-1', 'TTO-2', 'TTO-3', 'TCTO']
			for diesel in self.diesels:
				d = diesel.data
				td.extend([
					d.NAME, diesel.count, 
					d.NKR_N, d.NKR_U, d.NTO_1_N, d.NTO_2_N, d.NTO_3_N, d.NCTO,  
					d.TKR, d.TTR, d.TTO_1, d.TTO_2, d.TTO_3, d.TCTO])
		else:
			return "error mode"
		
		columns = len(th)
		table = PrettyTable(th)
		td_data = td[:]
		while td_data:
			table.add_row(td_data[:columns])
			td_data = td_data[columns:]
		return f"{table}\n"

class TableAgromachines():
	def __init__(self, list_calc_agromachine:list[CalculatorAgromachine]):
		self.agromachines = list_calc_agromachine
	def table(self, mode:str) -> str:
		td = []
		if mode == CONST_MODE_N_WORK:
			th = ['МАРКА', 'КОЛ-ВО', 'NTR', 'NCTO']
			for agromachine in self.agromachines:
				out = agromachine.get_N()[0]
				td.extend([agromachine.data.NAME, agromachine.count, 
				agromachine.data.NTR, agromachine.data.NCTO])
		elif mode == CONST_MODE_T_WORK:
			th = ['МАРКА', 'КОЛ-ВО', 'TTR', 'TCTO']
			for agromachine in self.agromachines:
				out = agromachine.get_T()[0]
				td.extend([agromachine.data.NAME, agromachine.count, 
				out.TTR, out.TCTO])	
		elif mode == CONST_MODE_DATA_VAR:
			th = ['МАРКА', 'КОЛ-ВО', 'NTR', 'NCTO', 'TTR', 'TCTO']
			for agromachine in self.agromachines:
				d = agromachine.data
				td.extend([d.NAME, agromachine.count, 
				d.NTR, d.NCTO, d.TTR, d.TCTO])	
		else:
			return "error mode"
						
		columns = len(th)
		table = PrettyTable(th)
		td_data = td[:]
		while td_data:
			table.add_row(td_data[:columns])
			td_data = td_data[columns:]
		return f"{table}\n"
	

class TableCombines():
	def __init__(self, list_calc_combine:list[CalculatorCombine]):
		self.combines = list_calc_combine
	def table(self, mode:str) -> str:
		td = []
		if mode == CONST_MODE_N_WORK:
			th = ['МАРКА', 'КОЛ-ВО', 'NTR', 'NCTO']
			for combine in self.combines:
				out = combine.get_N()[0]
				td.extend([combine.data.NAME, combine.count, 
				combine.data.NTR, combine.data.NCTO])
		elif mode == CONST_MODE_T_WORK:
			th = ['МАРКА', 'КОЛ-ВО', 'TTR', 'TCTO']
			for combine in self.combines:
				out = combine.get_T()[0]
				td.extend([combine.data.NAME, combine.count, 
				out.TTR, out.T_CTO])	
		elif mode == CONST_MODE_DATA_VAR:
			th = ['МАРКА', 'КОЛ-ВО', 'NTR', 'NTO1', 'NTO2', 'NCTO', 'TTR', 'TTO1', 'TTO2', 'TCTO']
			for combine in self.combines:
				d = combine.data
				td.extend([d.NAME, combine.count, 
				d.NTR, d.NTO_1, d.NTO_2, d.NCTO, 
				d.TTR, d.TTO_1, d.TTO_2, d.TCTO])	
		else:
			return "error mode"

		columns = len(th)
		table = PrettyTable(th)
		td_data = td[:]
		while td_data:
			table.add_row(td_data[:columns])
			td_data = td_data[columns:]
		return f"{table}\n"
	

class TableCars():
	def __init__(self, list_calc_car:list[CalculatorCar]):
		self.cars = list_calc_car
	def table(self, mode:str) -> str:
		td = []
		if mode == CONST_MODE_N_WORK:
			th = ['NAME', 'COUNT', 'NKR', 'NTO1', 'NTO2', 'NCTO']
			for car in self.cars:
				out = car.get_N()[0]
				td.extend([car.data.NAME, car.count, 
				out.NKR, out.NTO_1, out.NTO_2, out.N_CTO])
		elif mode == CONST_MODE_T_WORK:
			th = ['NAME', 'COUNT', 'TKR', 'TTO1', 'TTO2', 'TCTO']
			for car in self.cars:
				out = car.get_T()[0]
				td.extend([car.data.NAME, car.count, 
				out.TKR, out.TTO_1, out.TTO_2, out.T_CTO])
		elif mode == CONST_MODE_DATA_VAR:
			th = ['NAME', 'COUNT', 'NKR_U', 'NKR_N', 'NTO1', 'NTO2', 'NCTO',
		 			'TKR', 'TTR_U1', 'TTR_D', 'TTR_Z', 'TTO1', 'TTO2', 'TCTO']
			for car in self.cars:
				d = car.data
				td.extend([d.NAME, car.count, 
				d.NKR_U, d.NKR_N, d.NTO_1_N, d.NTO_2_N, d.NCTO,
				d.TKR, d.TTR_U1, d.TTR_D, d.TTR_Z, d.TTO_1, d.TTO_2, d.TCTO])
			
		columns = len(th)
		table = PrettyTable(th)
		td_data = td[:]
		while td_data:
			table.add_row(td_data[:columns])
			td_data = td_data[columns:]
		return f"{table}\n"
	
class TableCountsMachines():
	def __init__(self, manager_machines_dict:dict):
		self.manager_machines = manager_machines_dict
	def table(self) -> str:
		th = ['МАРКА', 'КОЛ-ВО']

		td = []
		for key in self.manager_machines.keys():
			td.extend([key, self.manager_machines[key]])
			
		columns = len(th)
		table = PrettyTable(th)
		td_data = td[:]
		while td_data:
			table.add_row(td_data[:columns])
			td_data = td_data[columns:]
		return f"{table}\n"