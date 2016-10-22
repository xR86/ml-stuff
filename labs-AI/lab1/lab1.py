
import aiml #used for chatbot
import time #used for small delays, so a response feels more natural
import json #used for serialization of data
import sys  #used for logging (stdout redirection)
import os.path #used for file check

#TODO: log all output to a logging file (streamHandler or `logging` module)
stdout = sys.stdout
logFile = open('output.log','w')
#sys.stdout = logFile

print '\n'
print '----load kernels---------'
#create kernel
kernel = aiml.Kernel()
kernel.learn('lab1-aiml-startup.xml')
kernel.respond('load aiml')

waitTime = 0.5
print '----starting chatbot-----'
print '\nHello, world !'
time.sleep(waitTime)
name = raw_input('What is your name ? >> ') 
sessionId = name.lower() #sessionId must be unique
time.sleep(waitTime)

# check if name is in database
#print os.path.isfile('data/lab1-person-' + sessionId + '.json')
#print os.path.exists('data/lab1-person-' + sessionId + '.json')

if os.path.isfile('data/lab1-person-' + sessionId + '.json'):
    existFile = open('data/lab1-person-' + sessionId + '.json')
    jsonData = json.load(existFile)
    #print jsonData
    age = jsonData['age']
    job = jsonData['job']
    #print job

else:
    age = raw_input('And your age ? >> ')
    time.sleep(waitTime)
    job = raw_input('Oh, I almost forgot, what do you do for a living ? >> ')

    time.sleep(waitTime)
    print '\nLet me think for a second ...\n'
    time.sleep(waitTime * 2)


sessionData = kernel.getSessionData(sessionId)
kernel.setPredicate('name', name, sessionId)
kernel.setPredicate('age', age, sessionId)
kernel.setPredicate('job', job, sessionId)

f = open('data/lab1-person-'+name.lower()+'.json','w+') #r,w with truncate (create new or replace)
f.write(json.dumps({'name': name, 'age': age, 'job': job}, indent=4, separators=(',', ': ') ))
f.close()

#bot predicates
kernel.setBotPredicate('hometown', 'Amazon EC2 Instance')
#bot_hometown = kernel.getBotPredicate('hometown')


#break with KeyboardInterrupt
while True:
    message = raw_input('Enter your message >> ')
    if message == 'exit' or message == 'quit':
        print '\nThanks for talking to me !\n'
        quit()
    if message == '\x1b[A': #meet up arrow
        #TODO: store each message in a variable, and recall them with up arrow
        print 'You just called up arrow'
    print kernel.respond(message, sessionId)



sys.stdout = stdout
logFile.close()



