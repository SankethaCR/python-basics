command =""
started = False
stopped = False
while True:
    command=input('Enter the command > ').upper()
    if command == 'START':
        if started == False:
            print('Car started !')
            started=True
        else:
            print('Car already started MAN !')
    elif command== 'STOP':
        if started and stopped == False:
            print('Car stopped !')
            stopped=True
        else:
            print('Car already stopped MAN ! and you need to START car first before STOPPING !')
    elif command == 'QUIT':
        print('Car exited !')
        break
    elif command == 'HELP':
        print(""" 
'Start' command to start the car
'Stop' command to stop the car
'Quit' command to exist/quit the car
        """)
    else:
        print("I don't undestand what you are saying")