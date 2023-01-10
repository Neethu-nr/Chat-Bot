from constants import *

import random
import re
from enum import Enum

def getTags(sentence):
	tags = re.findall('<(.+?)>', sentence)	
	return set([t.lower() for t in tags])

def lowerCaseKeys(dictionary):
	return {k.lower(): v for k, v in dictionary.items()}


class PRINT_CODES(Enum):
	ERROR = 0
	HUMAN = 1
	BOT = 2

class Cliff():
	def __init__(self):
		self.information = lowerCaseKeys(INFORMATION)
		self.errors = []
		self.display_error = False
	
	def print(self, sentence, code):
		prompt = '>'
		if code == PRINT_CODES.ERROR:
			prompt = '!#'
		elif code == PRINT_CODES.BOT:
			prompt = ' '
		print(prompt, sentence)
		return
	
	def startConversation(self):
		response = random.choice(CONVERSATION_STARTERS)
		return self.completeSentence(response)
	
	def completeSentence(self, initial_sentence=''):
		sentence = initial_sentence
		tags = getTags(sentence)
		not_found = set()
		while tags:
			tag = tags.pop()
			if tag in self.information:
				sentence = sentence.replace(f'<{tag}>', self.information[tag])
			else:
				not_found.add(tag)
		if not_found:
			error = f'Tags not found: {not_found} \n\tin sentence: {initial_sentence}, \n\tfinal_sentence: {sentence}'	
			if self.display_error:
				self.print(error, PRINT_CODES.ERROR)
			self.errors.append(error)
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
 			
