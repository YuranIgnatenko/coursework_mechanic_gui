class ModelDataDiesel():
	def __init__(self,NAME,NKR_U,NKR_N,NTR_N,NTO_3_N,NTO_2_N,NTO_1_N,NCTO,TKR,TTR,TTO_3,TTO_2,TTO_1,TCTO):
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
		self.NAME = NAME
		self.NTR = NTR
		self.NCTO = NCTO
		self.TTR = TTR
		self.TCTO = TCTO

class ModelDataCombine():
	def __init__(self,NAME,NKR,NTR,NTO,NTO_2,NTO_1,NCTO,TKR,TTR,TTO_2,TTO_1,TCTO):
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

class DataDieselResultN():
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

class DataDieselStringN():
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
	
class DataAgromachineResultN():
	def __init__(self, NTR, NTR_d, NCTO):
		self.NTR = NTR
		self.NTR_d = NTR_d
		self.NCTO = NCTO
		
class DataAgromachineStringN():
	def __init__(self, NTR_str, NCTO_str):
		self.NTR_str = NTR_str
		self.NCTO_str = NCTO_str
	def to_str(self) -> str:
		res = "\n".join([self.NTR_str, self.NCTO_str])
		return res