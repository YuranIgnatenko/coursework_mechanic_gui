from tkinter import *
from constants import DATA_MACHINES_ALL
from manager_calc import *
from manager_output import build_table, build_header
from threading import Thread

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
		def launch_calc():
			for machine in self.list_machines:
				name = machine.NAME
				temp_count = self.manager_entries.get_value(name)
				self.manager_machines.set(name, temp_count)
			# print("apply")
			# build_table(self.manager_machines.to_dict())
			self.launch_calculation()
		Thread(target=launch_calc).start()

	def _managers_write(self, name_machine:str, entry_obj:Entry):
		self.manager_entries.append_entry(name_machine, entry_obj)
		self.manager_machines.set(name_machine)



	def launch_calculation(self):
		print(build_header("Курсовая (обслуживание и ремонт)"))
		print(build_header("Расчетная часть"))

		for machine in DATA_DIESEL:
			print(build_header(machine.NAME))
			calc = CalculatorDiesel(machine,  self.manager_machines.get(machine.NAME))
			_, output_str = calc.get_N()
			print(output_str )

		for machine in DATA_AGROMACHINE:
			print(build_header(machine.NAME))
			calc = CalculatorAgromachine(machine,  self.manager_machines.get(machine.NAME))
			_, output_str = calc.get_N()
			print(output_str )

		for machine in DATA_COMBINE:
			print(build_header(machine.NAME))
			calc = CalculatorCombine(machine,  self.manager_machines.get(machine.NAME))
			_, output_str = calc.get_N()
			print(output_str )

		for machine in DATA_CAR:
			print(build_header(machine.NAME))
			calc = CalculatorCar(machine,  self.manager_machines.get(machine.NAME))
			_, output_str = calc.get_N()
			print(output_str )


		print(build_header("РАСЧЕТ ФОРМУЛ НА ТРУДОЕМКОСТЬ"))


		for machine in DATA_DIESEL:
			print(build_header(machine.NAME))
			calc = CalculatorDiesel(machine,  self.manager_machines.get(machine.NAME))
			_, output_str = calc.get_T()
			print(output_str )

		for machine in DATA_AGROMACHINE:
			print(build_header(machine.NAME))
			calc = CalculatorAgromachine(machine,  self.manager_machines.get(machine.NAME))
			_, output_str = calc.get_T()
			print(output_str )

		for machine in DATA_COMBINE:
			print(build_header(machine.NAME))
			calc = CalculatorCombine(machine,  self.manager_machines.get(machine.NAME))
			_, output_str = calc.get_T()
			print(output_str )

		for machine in DATA_CAR:
			print(build_header(machine.NAME))
			calc = CalculatorCar(machine,  self.manager_machines.get(machine.NAME))
			_, output_str = calc.get_T()
			print(output_str )


	def mainloop(self):
		self.win.mainloop()




def test():
	w = Window()
	w.create_ui()
	w.mainloop()
