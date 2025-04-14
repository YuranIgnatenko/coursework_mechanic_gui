from tkinter import *
from constants import DATA_MACHINES_ALL
from manager_calc import *
from manager_output import build_header
from threading import Thread
import matplotlib.pyplot as plt

class ManagerMachines():
	def __init__(self):
		self._data = {} # {'k-700':2, 'k-701':4}

	def set(self, name_machine:str, count:int=0):
		self._data[name_machine] = count

	def get(self, name_machine:str) -> int:
		return self._data[name_machine]

	def to_dict(self) -> dict:
		return self._data

class ManagerEntries():
	def __init__(self):
		self._data = {} # {'k-700':Entry1, 'k-701':Entry2}

	def append_entry(self, name_machine:str, entry_obj:Entry):
		self._data[name_machine] = entry_obj

	def get_value(self, name_machine:str) -> int:
		temp_value = self._data[name_machine].get().strip()
		if temp_value != "":
			if str(temp_value).isdigit():
				return int(temp_value)
		return 0

	def get_etries(self) -> list[Entry]:
		return [e[1] for e in self._data.items()]

class Window():
	def __init__(self):
		self.title_window = 'KURSOVAYA TO'
		self.width_window = 285
		self.height_window = 450
		self.ui_column_label = 0
		self.ui_column_entry = 1
		self.size_padding_grid = 1
		self.size_padding_btn = 5
		self.list_machines = DATA_MACHINES_ALL
		self.manager_machines = ManagerMachines()
		self.manager_entries = ManagerEntries()
		self.list_storages_results = []


	def create_ui(self):
		self.win = Tk()
		self.win.title(self.title_window)
		self.win.config(width = self.width_window, height = self.height_window)
		
		for machine, i in zip(self.list_machines, range(len(self.list_machines))) :
			temp_label = Label(self.win, text=machine.NAME)
			temp_entry = Entry(self.win)

			temp_label.grid(row=i, column=self.ui_column_label, ipadx=self.size_padding_grid, ipady=self.size_padding_grid, padx=self.size_padding_grid, pady=self.size_padding_grid)
			temp_entry.grid(row=i, column=self.ui_column_entry, ipadx=self.size_padding_grid, ipady=self.size_padding_grid, padx=self.size_padding_grid, pady=self.size_padding_grid)

			self._managers_write(machine.NAME, temp_entry)
			
		
		self.btn_appply_machines = Button(
			self.win, 
			text="Apply & Launch", 
			command=self._command_apply, 
			background='green')
		
		self.btn_appply_machines.grid(columnspan=2, 
								ipadx=self.size_padding_btn, ipady=self.size_padding_btn, 
								padx=self.size_padding_btn, pady=self.size_padding_btn)

	def fill_entry_for_test(self):
		for e in self.manager_entries.get_etries():
			e.delete(0,END)
			e.insert(0,1)

	def _command_apply(self):
		self.btn_appply_machines['bg']='yellow'
		def launch_calc():
			for machine in self.list_machines:
				name = machine.NAME
				temp_count = self.manager_entries.get_value(name)
				self.manager_machines.set(name, temp_count)
			self.launch_calculation()
		Thread(target=launch_calc).start()


	def launch_calculation(self):
		topwin = Toplevel(self.win)
		topwin.geometry("800x600+100+100")
		textarea = Text(topwin)
		textarea.pack(fill=BOTH,expand=True)

		text_out = ""

		diesels = []
		agromachines = []
		combines = []
		cars = []

		text_out += build_header("Курсовая (обслуживание и ремонт)")
		text_out += build_header("Расчетная часть")
		
		for machine in DATA_DIESEL:
			 
			calc = CalculatorDiesel(machine,  self.manager_machines.get(machine.NAME))
			diesels.append(calc)
			temp_storage, output_str = calc.get_N()
			self.list_storages_results.append(temp_storage)
			text_out += output_str

		for machine in DATA_AGROMACHINE:
			 
			calc = CalculatorAgromachine(machine,  self.manager_machines.get(machine.NAME))
			agromachines.append(calc)
			temp_storage, output_str = calc.get_N()
			self.list_storages_results.append(temp_storage)
			text_out += output_str

		for machine in DATA_COMBINE:
			 
			calc = CalculatorCombine(machine,  self.manager_machines.get(machine.NAME))
			combines.append(calc)
			temp_storage, output_str = calc.get_N()
			self.list_storages_results.append(temp_storage)
			text_out += output_str

		for machine in DATA_CAR:
			 
			calc = CalculatorCar(machine,  self.manager_machines.get(machine.NAME))
			cars.append(calc)
			temp_storage, output_str = calc.get_N()
			self.list_storages_results.append(temp_storage)
			text_out += output_str

		text_out += build_header("РАСЧЕТ ФОРМУЛ НА ТРУДОЕМКОСТЬ")
		
		for machine in DATA_DIESEL:
			 
			calc = CalculatorDiesel(machine,  self.manager_machines.get(machine.NAME))
			temp_storage, output_str = calc.get_T()
			self.list_storages_results.append(temp_storage)
			text_out += output_str

		for machine in DATA_AGROMACHINE:
			 
			calc = CalculatorAgromachine(machine,  self.manager_machines.get(machine.NAME))
			temp_storage, output_str = calc.get_T()
			self.list_storages_results.append(temp_storage)
			text_out += output_str

		for machine in DATA_COMBINE:
			 
			calc = CalculatorCombine(machine,  self.manager_machines.get(machine.NAME))
			temp_storage, output_str = calc.get_T()
			self.list_storages_results.append(temp_storage)
			text_out += output_str

		for machine in DATA_CAR:
			 
			calc = CalculatorCar(machine,  self.manager_machines.get(machine.NAME))
			temp_storage, output_str = calc.get_T()
			self.list_storages_results.append(temp_storage)
			text_out += output_str

		table_counts_machines = TableCountsMachines(self.manager_machines.to_dict())
		table_diesel = TableDiesels(diesels)
		table_agromachine = TableAgromachines(agromachines)
		table_combine = TableCombines(combines)
		table_car = TableCars(cars)

		text_out += table_counts_machines.table()

		text_out += table_diesel.table(CONST_MODE_DATA_VAR)
		text_out += table_agromachine.table(CONST_MODE_DATA_VAR)
		text_out += table_combine.table(CONST_MODE_DATA_VAR)
		text_out += table_car.table(CONST_MODE_DATA_VAR)

		text_out += table_diesel.table(CONST_MODE_N_WORK)
		text_out += table_agromachine.table(CONST_MODE_N_WORK)
		text_out += table_combine.table(CONST_MODE_N_WORK)
		text_out += table_car.table(CONST_MODE_N_WORK)

		text_out += table_diesel.table(CONST_MODE_T_WORK)
		text_out += table_agromachine.table(CONST_MODE_T_WORK)
		text_out += table_combine.table(CONST_MODE_T_WORK)
		text_out += table_car.table(CONST_MODE_T_WORK)



		with open(NAMEFILE_OUTPUT_TXT, "w", encoding="utf-8") as file:
			file.write(text_out)

		list_season, list_mounth = self.get_all_results()
		table_graph = TableDateGraph()
		
		res = self.sorted_values(list_mounth, list_season)
		text_out += table_graph.table(res)

		textarea.insert("1.0", text_out)
		# print(text_out)
		self.btn_appply_machines['bg']='green'

		self.create_graph(list_mounth, list_season)
		



	def get_all_results(self) -> tuple:
		'''1 - list season 2 - list other mounth'''
		list_season_values = []
		list_other_mounth_values = []

		for storage in self.list_storages_results:
			dict_results = storage.__dict__
			for key in dict_results:
				value = dict_results[key]
				if str(key).find("CTO") != -1:
					list_season_values.append(value)
				else:
					list_other_mounth_values.append(value)
		return (list_other_mounth_values, list_season_values)

	def sorted_values(self, list_mounth:list[float], list_season:list[float]) -> list:
		list_mounth.sort(reverse=True)
		list_season.sort()
		new_list_mounth = [[] for _ in range(10)]
		c = 0
		for value in list_mounth:
			new_list_mounth[c].append(value)
			if c==9:c=0
			else:c+=1

		new_list_result = []
		c = 0
		for i in new_list_mounth:
			if c % 2 == 0:
				new_list_result.append(new_list_mounth.pop(c))
			c+=1
		new_list_result.reverse()
		new_list_mounth+=new_list_result
		
		num1, num2 = 0,0
		# c=0
		# for value in list_season:
		# 	if c % 2 == 0:
		# 		num1 += value
		# 	else:
		# 		num2 += value
		# 	c+=1

		result = new_list_mounth[:2]+[[0]]+new_list_mounth[2:-2]+[[0]]+new_list_mounth[-2:]
		return result

	def create_graph(self, list_mounth:list[float], list_season:list[float]):
		res = self.sorted_values(list_mounth, list_season)

		data = []
		for arr in res:
			data.append(sum(arr))

		ax = [i+1 for i in range (12)]
		plt.plot(ax, data, marker="o", color='skyblue', label='Трудоёмкость')
		plt.title("График ремонтов и обслуживания по месяцам")
		plt.xlabel("mounth")
		plt.ylabel("value")
		plt.axhline(0, color='black', linewidth=1, linestyle="--")
		plt.grid(True)
		plt.legend()
		plt.savefig("plot.png", format='png')
		plt.show()

	def _managers_write(self, name_machine:str, entry_obj:Entry):
		self.manager_entries.append_entry(name_machine, entry_obj)
		self.manager_machines.set(name_machine)

	def mainloop(self):
		self.win.mainloop()




def test():
	w = Window()
	w.create_ui()
	w.mainloop()
