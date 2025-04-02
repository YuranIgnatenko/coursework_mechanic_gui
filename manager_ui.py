from tkinter import *
from constants import LIST_MASHINES

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
		print(name_machine)
		self._data[name_machine] = entry_obj

	def get_value(self, name_machine:str) -> int:
		temp_value = self._data[name_machine].get().strip()
		if temp_value == "":return 0
		else:return int(temp_value)

class Window():
	def __init__(self):
		self.title_window = 'KURSOVAYA TO'
		self.width_window = 285
		self.height_window = 450
		self.ui_column_label = 0
		self.ui_column_entry = 1
		self.size_padding_grid = 1
		self.size_padding_btn = 5
		self.list_machines = LIST_MASHINES
		self.manager_machines = ManagerMachines()
		self.manager_entries = ManagerEntries()

	def create_ui(self):
		self.win = Tk()
		self.win.title(self.title_window)
		self.win.config(width = self.width_window, height = self.height_window)
		
		for name, i in zip(self.list_machines, range(len(self.list_machines))) :
			temp_label = Label(self.win, text=name)
			temp_entry = Entry(self.win)

			temp_label.grid(row=i, column=self.ui_column_label, ipadx=self.size_padding_grid, ipady=self.size_padding_grid, padx=self.size_padding_grid, pady=self.size_padding_grid)
			temp_entry.grid(row=i, column=self.ui_column_entry, ipadx=self.size_padding_grid, ipady=self.size_padding_grid, padx=self.size_padding_grid, pady=self.size_padding_grid)

			self._managers_write(name, temp_entry)
			
		
		self.btn_appply_machines = Button(
			self.win, 
			text="Apply & Launch", 
			command=self._command_apply, 
			background='green')
		
		self.btn_appply_machines.grid(columnspan=2, 
								ipadx=self.size_padding_btn, ipady=self.size_padding_btn, 
								padx=self.size_padding_btn, pady=self.size_padding_btn)

	def _command_apply(self):
		for name in self.list_machines:
			temp_count = self.manager_entries.get_value(name)
			self.manager_machines.set(name, temp_count)
		print("apply")

	def _managers_write(self, name_machine:str, entry_obj:Entry):
		self.manager_entries.append_entry(name_machine, entry_obj)
		self.manager_machines.set(name_machine)

	def mainloop(self):
		self.win.mainloop()

def test():
	w = Window()
	w.create_ui()
	w.mainloop()
