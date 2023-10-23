class time:
	"""The time class stores general information about a time.
	"""    
	def __init__(self, hour: int, minute: int, second: int):
		"""Constructs a time object having the specified hour, minute, and second, 
		and universal time in the format HH:MM:SS.

		:ivar __hour: hour of this time object
		:ivar __minute: minute of this time object
		:ivar __second: second of this time object
		:ivar __time: universal time of this time object in the format HH:MM:SS

		Args:
			hour (int): specified hour
			minute (int): specified minute
			second (int): specified second

		Raises:
			ValueError: indicates specified hour is less than 0 or greater than 24
			ValueError: indicates specified minute is less than 0 or greater than 60
			ValueError: indicates specified second is less than 0 or greater than 60
		""" 
		if hour < 0 or hour > 24:
			ValueError("Hour cannot be less than 0 or greater than 24") 
		elif minute < 0 or minute > 60:
			ValueError("Minute cannot be less than 0 or greater than 60")
		elif second < 0 or second > 60:
			ValueError("Second cannot be less than 0 or greater than 24")
		
		self.__hour = hour
		self.__minute = minute
		self.__second = second
		self.__time = f"{self.__hour}:{self.__minute}:{self.__second}"
	

	def getHour(self):
		"""Returns the hour of the calling time object.

		Returns:
			int: hour of the calling time object
		""" 
		return self.__hour
	
	def setHour(self, hour: int):
		"""Sets the hour of the calling time object to the specified hour and
		recomputes the universal time of the calling time object.

		Args:
			hour (int): specified hour

		Raises:
			ValueError: indicates specified hour is less than 0 or greater than 24
		"""   
		if hour < 0 or hour > 24: 
			ValueError("Cannot be less than 0 or greater than 24")
		self.__hour = hour
			

	def getMinute(self):
		"""Returns the minute of the calling time object.

		Returns:
			int: minute of the calling time object
		""" 

		return self.__minute
	
	def setMinute(self, minute: int):
		"""Sets the minute of the calling time object to the specified minute and
		recomputes the universal time of the calling time object.

		Args:
			minute (int): specified minute

		Raises:
			ValueError: indicates specified minute is less than 0 or greater than 60
		"""
		if minute < 0 or minute > 60:
			ValueError("Minute cannot be less than 0 or greater than 60")
		self.__minute == minute

	def getSecond(self):
		"""Returns the second of the calling time object.

		Returns:
			int: second of the calling time object
		"""
		return self.__second
	
	def setSecond(self, second: int):
		"""Sets the second of the calling time object to the specified second and
		recomputes the universal time of the calling time object.

		Args:
			second (int): specified second

		Raises:
			ValueError: indicates specified second is less than 0 or greater than 60
		"""

		if second < 0 or second > 60:
			ValueError("Second cannot be less than 0 or greater than 24")

	def getTime(self):
		"""Returns the universal time of the calling time object.

		Returns:
			str: universal time of the calling time object
		"""
	
	def __str__(self):
		"""Returns string representation of the calling time object.

		Returns:
			str: string representation of the calling time object
		"""
		return f"{self.__hour}:{self.__minute}:{self.__second}"      
	
	def __eq__(self, other):
		"""Tests if the calling time object is equal to the specified object.

		Args:
			other: the specified object

		Returns:
			Boolean: True if the calling time object is equal to the specified
			object, else False
		"""
	
	@staticmethod
	def sort(data, first: int, last: int):
		"""Sorts a list from smallest to largest using the insertion sort
		algorithm bypassing the elements to the left of first and to the
		right of last.

		Args:
			data: list to sort
			first (int): list index at which the sort will begin
			last (int): list index at which the sort will end
		"""
		#initialize loop counter variable named i
		i = len(data) - first - 1

	#initialize loop counter variable named j
		j = 0

	# initialize variable named big that will be used
	# to store the index of the biggest value 
		big = 0

	# initialize variable named temp that will be used to
	# swap list values
		temp = 0

	# loop through list as many times as specified by
	# len(data) and first
	# this loop represents the blue arrow
		while (i > 0):
		# set big equal to first
			big = first

		# set j equal to first + 1
			j = first + 1

		# loop through list starting with element at
		# first + 1 and continue until you reach first + i
		# this loop represents the yellow arrow
			while (j <= first + i):
			# if the value in data[big] is less than
			# data[j]
				if (data[big] < data[j]):
				#set big equal to j
					big = j
			
			# increment j by 1
				j += 1

		# swap the data in first + i with the data in big 
		# set temp to value in data[first + i]
			temp = data[first+i]

		#set data[first + i] = data[big]
			data[first+i] = data[big]

		#set data[big] to value in temp
			data[big] = temp

		# decrement i by 1 
			i -= 1        

	@staticmethod
	def search (a, first: int, last: int, target: int):
		"""Searches part of a sorted list for a specified target starting at a[first]
		and ending at a[last].

		Args:
			a (int): the list to search
			first (int): the list index at which the search will start
			last (int): the list index at which the search will end
			target (int): the element to search for

		Returns:
			int: If target appears in the list, index of the, element 
			that contains target; else -1.
		"""
