class requestor:
	
	Id = 0
	reqCount = 0
	reqTime = datetime.now()

	def __init__(self, Id, reqCount, reqTime):
		self.Id = Id
		self.reqTime = reqTime
		self.reqCount = reqCount
	

	@staticmethod
	def add(Id, count):
		#saves requestor's info on json if doesnot exist already'
		if (search(Id)):
			#new line in file with new client
			return "added new client"+ Id						
		
	
	@staticmethod
	def incrementReq(Id):
		#increments request count in json each time request is made for spesific client
		print("success")

	@staticmethod
	def clearCount(Id,time):
		#clears the reqCount if 1 min has been passed
		if (datetime.now() - time >= 60 ):
			setReqCount(Id, 0)
			

	@staticmethod
	def getReqCount(Id):
		#to get count of Id from json
		return count

	@staticmethod
	def setReqCount(Id, count):
		# set a count val for Id in json
		print("success")

	@staticmethod
	def getReqTime(Id):
		#to get Request time of Id from json
		return time
	
	@staticmethod
	def setReqTime(Id, time):
		#set Request time of Id in json
		print("success")

	@staticmethod
	def search(Id):
		#search Id the json, returns bool
		return true
