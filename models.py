from constants import *
# class models for storage 
# constants values for calculation

CATEGORY_DIESEL = 1
CATEGORY_AGROMACHINE = 2
CATEGORY_COMBINE = 3
CATEGORY_CAR = 4

class ModelDataDiesel():
	def __init__(self,NAME,NKR_U,NKR_N,NTR_N,NTO_3_N,NTO_2_N,NTO_1_N,NCTO,TKR,TTR,TTO_3,TTO_2,TTO_1,TCTO):
		self.category = CATEGORY_DIESEL
		self.NAME = NAME
		self.NKR_U = NKR_U
		self.NKR_N = NKR_N
		self.NTR_N = NTR_N
		self.NTO_3_N = NTO_3_N
		self.NTO_2_N = NTO_2_N
		self.NTO_1_N = NTO_1_N
		self.NCTO = NCTO
		self.TKR = TKR
		self.TTR = TTR
		self.TTO_3 = TTO_3
		self.TTO_2 = TTO_2
		self.TTO_1 = TTO_1
		self.TCTO = TCTO

class ModelDataAgromachine():
	def __init__(self, NAME, NTR, NCTO, TTR, TCTO):
		self.category = CATEGORY_AGROMACHINE
		self.NAME = NAME
		self.NTR = NTR
		self.NCTO = NCTO
		self.TTR = TTR
		self.TCTO = TCTO

class ModelDataCombine():
	def __init__(self,NAME,NKR,NTR,NTO,NTO_2,NTO_1,NCTO,TKR,TTR,TTO_2,TTO_1,TCTO):
		self.category = CATEGORY_COMBINE
		self.NAME = NAME
		self.NKR = NKR
		self.NTR = NTR
		self.NTO = NTO
		self.NTO_2 = NTO_2
		self.NTO_1 = NTO_1
		self.NCTO = NCTO
		self.TKR = TKR
		self.TTR = TTR
		self.TTO_2 = TTO_2
		self.TTO_1 = TTO_1
		self.TCTO = TCTO

class ModelDataCar():
	def __init__(self,NAME,NKR_U,NKR_N,NTO_2_N,NTO_1_N,NCTO,TKR,TTO_2,TTO_1,TCTO,TTR_U1,TTR_D,TTR_Z):
		self.category = CATEGORY_CAR
		self.NAME = NAME
		self.NKR_U = NKR_U
		self.NKR_N = NKR_N
		self.NTO_2_N = NTO_2_N
		self.NTO_1_N = NTO_1_N
		self.NCTO = NCTO
		self.TKR = TKR
		self.TTO_2 = TTO_2
		self.TTO_1 = TTO_1
		self.TCTO = TCTO
		self.TTR_U1 = TTR_U1
		self.TTR_D = TTR_D
		self.TTR_Z = TTR_Z

# models class for save output calculation paramets 'N'

class DataDieselResultN():
	def __init__(self,NKR,NTR,NTO_3,NTO_2,NTO_1,N_CTO):
		self.NKR = NKR
		self.NTR = NTR
		self.NTO_3 = NTO_3
		self.NTO_2 = NTO_2
		self.NTO_1 = NTO_1
		self.N_CTO = N_CTO

class DataAgromachineResultN():
	def __init__(self, NTR, NCTO):
		self.NTR = NTR
		self.NCTO = NCTO
			
class DataCombineResultN():
	def __init__(self,NKR,NTR,NTO_2,NTO_1,N_CTO):
		self.NKR = NKR
		self.NTR = NTR
		self.NTO_2 = NTO_2
		self.NTO_1 = NTO_1
		self.N_CTO = N_CTO
		
class DataCarResultN():
	def __init__(self,NKR,NTO_2,NTO_1,N_CTO):
		self.NKR = NKR
		self.NTO_2 = NTO_2
		self.NTO_1 = NTO_1
		self.N_CTO = N_CTO

# models class for save output calculation paramets 'T'

class DataDieselResultT():
	def __init__(self,TKR,TTR,TTO_3,TTO_2,TTO_1,T_CTO):
		self.TKR = TKR
		self.TTR = TTR
		self.TTO_3 = TTO_3
		self.TTO_2 = TTO_2
		self.TTO_1 = TTO_1
		self.T_CTO = T_CTO
	
class DataAgromachineResultT():
	def __init__(self, TTR, TCTO):
		self.TTR = TTR
		self.TCTO = TCTO
		
class DataCombineResultT():
	def __init__(self,TKR,TTR,TTO_2,TTO_1,T_CTO):
		self.TKR = TKR
		self.TTR = TTR
		self.TTO_2 = TTO_2
		self.TTO_1 = TTO_1
		self.T_CTO = T_CTO

class DataCarResultT():
	def __init__(self,TKR,TTR,TTO_2,TTO_1,T_CTO):
		self.TKR = TKR
		self.TTR = TTR
		self.TTO_2 = TTO_2
		self.TTO_1 = TTO_1
		self.T_CTO = T_CTO
		