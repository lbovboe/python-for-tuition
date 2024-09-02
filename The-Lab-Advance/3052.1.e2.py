
class Messaging:

	#stores name
	def __init__(self):
		self.name = ""

	#display message
	def message(self):
		print("No messaging service yet")


class SocialMedia(Messaging):

	def __init__(self, name):
		Messaging.__init__(self)
		self.name = name

	#overrides parents message
	def message(self):
		print("Using messaging of",self.name)

	@staticmethod
	def main():
		message = Messaging()
		message.message()
		name = input("Enter social media: ")
		name = SocialMedia(name)
		name.message()

#main
SocialMedia.main()