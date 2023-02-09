from multiprocessing import Process, current_process, Value, Array

N=8
def task(common, tid, turn):
	a=0
	for i in range(100):
		print(f'{tid}-{i}:Non-critical Section')

