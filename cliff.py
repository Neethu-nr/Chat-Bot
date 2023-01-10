from constants import *

import random

class Cliff():
	def __init__(self):
		self.name = 'cliff'
	
	def startConversation(self):
		response = random.choice(CONVERSATION_STARTERS)
		return self.completeSentence(response)
	
	def completeSentence(self, sentence=''):
		# TODO: replace <NAME> by self.name
		return sentence
	
	def input(self, sentence=''):
		return 
	
	def getResponse(self):
		return 'boop', False
	
	def run(self):
		print(self.startConversation())
		human_response, end = 'beep', False
		while human_response and not end:
			human_response = input('>')
			self.input(human_response)
			chat_response, end = self.getResponse()
			print(chat_response)
		return
 			
