import numpy as np

def calculate(list):
	if len(list) < 9:
		raise ValueError('List must contain nine numbers.')
	list_np = np.array(list).reshape(3, 3)
	calculations = {}
	calculations['mean'] = [list_np.mean(axis=0).tolist(), list_np.mean(axis=1).tolist(), list_np.mean()]
	calculations['variance'] = [list_np.var(axis=0).tolist(), list_np.var(axis=1).tolist(), list_np.var()]
	calculations['standard deviation'] = [list_np.std(axis=0).tolist(), list_np.std(axis=1).tolist(), list_np.std()]
	calculations['max'] = [list_np.max(axis=0).tolist(), list_np.max(axis=1).tolist(), list_np.max()]
	calculations['min'] = [list_np.min(axis=0).tolist(), list_np.min(axis=1).tolist(), list_np.min()]
	calculations['sum'] = [list_np.sum(axis=0).tolist(), list_np.sum(axis=1).tolist(), list_np.sum()]
	
	return calculations