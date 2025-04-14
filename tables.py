from prettytable import PrettyTable
from calc import *

def build_header(text:str) -> str:
	return f"{'-'*30}\n{text}\n{'-'*30}"

def build_table(dict_name_count:dict):
	return tabulate(dict_name_count.items(), headers=['МАРКА', 'КОЛ-ВО'], tablefmt="grid")


'''
d = { 'K-700': K_700, 'K-701': K_701,
	 'ДТ-75 МВ': DT, 'МТЗ-82': MTZ2, 'МТЗ-80': MZT,
	 'Т-40': T40, 'Т-25': T25, 'Т-16': T16,
	  'УАЗ-469': UAZ,  'KAMAЗ-5320':KAMAZ, 'ГАЗ-53 А':GAZ,
	  'ЗИЛ-130': ZIL, 'CK-5': CK, 'KKУ-2 А': KKU,
	  'ПЛН-4-35': PLN, 'СЗ-3-6': SZ, 'БДТ-3': BDT,
	  }'
'''



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
	
class TableDateGraph():
	def __init__(self):
		pass
	def table(self, data_array_2d) -> str:
		table = PrettyTable()
		table.field_names = [
			'jan', 'feb', 'march', 
			'apr', "may", 'jun', 
			'jul', 'aug', 'sept', 
			'oct', 'nov', 'dec']

		
		max_length = max(len(row) for row in data_array_2d)
		fulled_data = [row + [0] * (max_length - len(row)) for row in data_array_2d]
		temp = [list(row) for row in zip(*fulled_data)]

		for arr in temp:
			table.add_row(arr)
		return f"{table}\n"
	
