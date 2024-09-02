class Hello:

	def __init__(self, name):
		self.name = name

	def greet(self):
		print("Hello,",self.name)


class KoreanHello(Hello):
	def __init__(self, name):
		super().__init__(name)

	#overides greet of Hello
	def greet(self):
		print("안녕하세요,",self.name)


name = input("Enter name: ")
hi = Hello(name)
koreaname = KoreanHello(name)
hi.greet()
koreaname.greet()