from models import *

NAMEFILE_OUTPUT_TXT = "calculation_output.txt"


DATA_DIESEL = [
	ModelDataDiesel('K-700', 3200, 11970, 5120, 2560, 640, 160, 2, 410, 297, 43.2, 10.6, 2.5, 29.3),
	ModelDataDiesel('K-701', 3500, 19220, 6200, 3120, 780, 195, 2, 451, 297, 25.2, 11.6, 2.2, 18.3),
	ModelDataDiesel('DT-75', 1150, 5800, 2480, 1240, 310, 77, 2, 229, 268, 21.4, 6.4, 2.7, 17.1),
	ModelDataDiesel('MTZ-82', 1300, 4480, 1680, 840, 210, 52, 2, 193, 163, 19.8, 6.9, 2.7, 3.5),
	ModelDataDiesel('MTZ-80', 1200, 4480, 1680, 840, 210, 52, 2, 229, 268, 19.8, 6.9, 2.7, 3.5),
	ModelDataDiesel('T-40', 700, 2630, 1200, 600, 150, 37, 2, 156, 127, 18, 6.8, 2, 19.8),
	ModelDataDiesel('T-25', 350, 1940, 740, 370, 92, 23, 2, 132, 80, 7.7, 2.7, 0.9, 1.8),
	ModelDataDiesel('T-16', 200, 1320, 510, 255, 64, 16, 2, 114, 80, 7.7, 2.7, 0.9, 1.8),
	]

DATA_AGROMACHINE = [
	ModelDataAgromachine("PLN-4-35", 0.8, 2, 17, 3.4),
	ModelDataAgromachine("BDT", 0.78, 2, 29, 3.4),
	ModelDataAgromachine("SZ", 0.78, 2, 29, 3.4),
	ModelDataAgromachine("KKU-2A", 0.8, 2, 69, 3.4),
	]

DATA_COMBINE = [ModelDataCombine("CK", 0.15, 0.6, 220, 240, 60, 1, 330, 150, 6.6, 5.1, 15)]

DATA_CAR = [
	ModelDataCar('UAZ-469', 35_000, 140_000, 12_800, 3200, 2, 280, 11.1, 2.2, 0.25 * 7.9, 35_000, 1000, 10.3),
	ModelDataCar('KAMAZ-5250', 40_000, 250_000, 7200, 2400, 2, 380, 21.5, 4.4, 0.25 * 10.2, 40_000, 1000, 10.5),
	ModelDataCar('GAZ-130', 36_000, 160_000, 10_000, 2500, 2, 249, 11.8, 2.9, 0.25 * 4.6, 36_000, 1000, 6),
	ModelDataCar('ZIL-130', 11_000, 230_000, 10_000, 2500, 2, 302, 14, 3.5, 0.25 * 5, 44_000, 1000, 6.3)
]

DATA_MACHINES_ALL = [*DATA_DIESEL, *DATA_AGROMACHINE, *DATA_COMBINE, *DATA_CAR]