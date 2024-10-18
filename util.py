def linear_regression(n, x, y):
	
	sum_x = sum(x)
	sum_y = sum(y)
	sum_xy = sum(x_i * y_i for x_i, y_i in zip(x, y))
	sum_x_squared = sum(x_i ** 2 for x_i in x)
	
	m = (n * sum_xy - sum_x * sum_y)/(n * sum_x_squared - sum_x ** 2)
	n = (sum_y - m * sum_x) / n
	return m, n

