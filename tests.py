import unittest
from cliff import Cliff

class BasicTest(unittest.TestCase):
	def setUp(self):
		self.bot = Cliff()
	
	def test_hi(self):
		start = self.bot.startConversation()
		self.assertIsNotNone(start)
		self.bot.input('hi there')
		response, end = self.bot.getResponse()
		self.assertIsNotNone(response)
		self.assertFalse(end)
	
if __name__ == '__main__':
    unittest.main()	
