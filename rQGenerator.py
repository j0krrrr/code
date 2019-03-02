import random
capitals={'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for qNum in range(35):
    qFile=open('cQ%s.txt' %(qNum+1),'w')
    aKFile=open('cQA%s.txt' %(qNum+1),'w')

    qFile.write('Name:\nDate:\n\nPeriod:\n\n')
    qFile.write((' '*20)+'State Captials Quiz (Form %s)'%(qNum+1))
    qFile.write('\n\n')
    
    states=list(capitals.keys())
    random.shuffle(states)

    for questionNum in range(50):
        cAnswer=capitals[states[questionNum]]
        wAnswer=list(capitals.values())
        del wAnswer[wAnswer.index(cAnswer)]
        wAnswer=random.sample(wAnswer,3)
        aOptions=wAnswer+[cAnswer]
        random.shuffle(aOptions)
        print("%s.%s"%(questionNum+1,states[questionNum]))
        qFile.write('%s. What is the capital of %s\n' %(questionNum+1,states[questionNum]))
        for i in range(4):
            qFile.write('%s.%s\n'%('ABCD'[i],aOptions[i]))
        qFile.write('\n')

        aKFile.write('%s.%s\n'%(questionNum+1,'ABCD'[aOptions.index(cAnswer)]))
    qFile.close()
    aKFile.close()


