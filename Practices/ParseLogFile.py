import pprint
import json
from collections import OrderedDict
def bios_log_parse(file_name=r"C:\Users\pradhana\Downloads\birchstream.uart_F2LM_CH_01_45_DDR5.log"):
	with open(file_name,"r") as file:
		lines = file.readlines()
		d = OrderedDict()
		for i in range(0,100):
			process_for_colon_equal(lines[i],d)
	#print(d)			
	print("done")
	#pprint.pprint(d)
	return d
def process_for_start_end_block()
def process_for_colon_equal(line,d):
	if "=" in line:
		temp = line.split("=")
		d[temp[0]] = temp[1].strip()
	elif":" in line:
		temp = line.split(":")	
		d[temp[0]] = temp[1].strip()
	else:
		d[line] = ""	
	

if __name__ == "__main__":
	d = bios_log_parse()
	print(d["Bios ID"])
	