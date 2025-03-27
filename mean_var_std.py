#!/bin/python3.11

import numpy as np

def calculate(list):
	if len(list) < 9:
		raise ValueError('List must contain nine numbers.')
	list_np = np.array(list).reshape(3, 3)
	result = {}
	result['mean'] = [list_np.mean(axis=0).tolist(), list_np.mean(axis=1).tolist(), list_np.mean()]
	result['variance'] = [list_np.var(axis=0).tolist(), list_np.var(axis=1).tolist(), list_np.var()]
	result['standard deviation'] = [list_np.std(axis=0).tolist(), list_np.std(axis=1).tolist(), list_np.std()]
	result['max'] = [list_np.max(axis=0).tolist(), list_np.max(axis=1).tolist(), list_np.max()]
	result['min'] = [list_np.min(axis=0).tolist(), list_np.min(axis=1).tolist(), list_np.min()]
	result['sum'] = [list_np.sum(axis=0).tolist(), list_np.sum(axis=1).tolist(), list_np.sum()]
	return result

if __name__ == '__main__':
	print(calculate([0,1,2,3,4,5,6,7,8]))