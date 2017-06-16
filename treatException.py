class treatException(object):
	"""docstring for treatException"""
	def __init__(self, arg):
		super(treatException, self).__init__()
		self.arg = arg
	
	def badException():
		number = int(input('What`s your favorite number? \n'))
		print(2 * number)

	def goodException():
		while True:
			try:
				number = int(input('What`s your favorite number? \n'))
				print(2 / number)
				break
			except ValueError:
				print("Make sure you enter a number")
			except ZeroDivisionError:
				print ("Don't pick zero")
			except Exception as e:
				print(e+'\n')


erro = treatException
erro.goodException()

