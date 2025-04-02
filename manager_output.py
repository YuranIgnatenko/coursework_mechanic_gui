from tabulate import tabulate

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


