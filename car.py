command=''
started = False
while quit:
    command = input('>' ).lower()
    if command == 'help' :
        print('''
start - to start the car
stop - to stop the car
quit - to exit
''')
    elif command == 'start':
        if started:
            print("Car already started!")
        else:
            started = True
            print('Car started... Ready to go!')
    elif command == 'stop':
        if started:
            started = False
            print('Car stopped.')
        else:
            print("Car already stopped!")
    elif command == 'quit':
        quit = False
    else:
        print("I don't understand that.")