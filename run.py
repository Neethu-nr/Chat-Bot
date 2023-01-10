from cliff import Cliff

if __name__ == "__main__":
	bot = Cliff()
	bot.run()
	if bot.errors:
		print('\n\n# --------------ERRRORS----------------')
		print(bot.errors)
