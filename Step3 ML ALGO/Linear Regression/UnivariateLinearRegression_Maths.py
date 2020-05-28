#Linear Regresion in univariate 

import numpy as np
class LinearRegressor:
	def __init__(self, x, y, alpha = 0.01, b0 = 0, b1 = 0):

		self.i = 0
		self.x = x
		self.y = y
		self.alpha = alpha
		self.b0 = b0
		self.b1 = b1
		if len(x) != len(y):
			raise TypeError("X and Y should have same number of rows.")

	#here we are using model as 'self'

	#prediction funciton
	def predict(model, x):
		# y = b0 + b1 * x
		return model.b0 + model.b1 * x

	def costDerivative(model, i):
		x, y, b0, b1 = model.x, model.y, model.b0, model.b1
		predict = model.predict

		return sum([
			2 * (predict(xi) - yi) *1
			if i == 0
			else (predict(xi) - yi) * xi
			for xi, yi in zip(x,y)
			]) / len(x)

	#function to update the coefficient
	def updateCoeff(model, i):
		costDerivative = model.costDerivative
		if i == 0:
			model.b0 -= model.alpha * costDerivative(i)
		elif i == 1:
			model.b1 -= model.alpha * costDerivative(i)

	#sotp iteration
	def stopIteration(model, max_epochs = 1000):
		model.i +=1
		if model.i == max_epochs:
			return True
		else:
			return False


	#function to fit the model
	def fit(model):
		updateCoeff = model.updateCoeff
		model.i = 0
		while True:
			if model.stopIteration():
				break
			else:
				updateCoeff(0)
				updateCoeff(1)


#main funciton
if __name__ == '__main__':
	x = [i for i in range(12)]
	y = [2* i + 3 for i in range(12)]
	print("x\t\ty\n")
	for i in range(12):
		print("{}\t\t{}".format(x[i], y[i]))
	linearRegressor = LinearRegressor(x,y, alpha=0.03)

	print("Model is traiing ........\n")
	linearRegressor.fit()
	print("Predicted Value is: {}".format(linearRegressor.predict(11)))
