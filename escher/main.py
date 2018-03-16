import csv

from microsoftbotframework import MsBot

from response import ResponseLogic


keypath = 'C:\\Users\\perus\\Desktop\\keyfile.csv'
with open(keypath, newline='\n') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    key = [tuple(row) for row in reader]

decider = ResponseLogic(*key[1])
bot = MsBot()
bot.add_process(decider.respond)

if __name__ == '__main__':
    bot.run()
