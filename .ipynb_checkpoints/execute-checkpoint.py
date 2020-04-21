from chatbotfinal import Session
session = Session()

def query():
    print ('BOT: Welcome Guest\nHi! How may I assist you?')
    print ('\nAt any instant type "res" to restart the bot\n')

    while True:

        inp = input('User: ')
        if(inp=="Bye"or inp=="bye"):
            break
        if(inp=='res'):
            query()

        print ('BOT:', session.reply(inp))
query()