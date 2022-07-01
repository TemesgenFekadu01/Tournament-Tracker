slotlist = []

print('Welcome to Tournaments R Us')
print('============================')
num_of_slots = int(input('Enter the number of participants: '))

for a in range(num_of_slots):
    slotlist.append(None)

def signup():
    print('\nParticipant Sign Up')
    print('============================')
    name = str(input('Participant Name: '))
    slotnum = int(input('Desired Starting Slot #: '))
    if slotnum > num_of_slots:
        print('\nError:\nSlot number is out of range.')
    elif slotlist[(slotnum-1)] is None:
        slotlist[(slotnum-1)] = str(slotnum) + '|' + name
        print('\nSuccess:\n' + name + ' is signed up in starting slot #' + str(slotnum))
    else:
        print('\nError:\nSlot #' + str(slotnum) + ' is filled. Please try again.')
    print('\n1. Sign up another participant\n2. Return to main menu')
    menu_item = int(input('Select: '))
    if menu_item == 1:
        signup()
    elif menu_item == 2:
        menu()

def cancel():
    print('\nParticipant Cancellation')
    print('============================')
    slotnum = int(input('Desired Starting Slot #: '))
    name = str(input('Participant Name: '))
    slotentry = slotlist[(slotnum-1)]
    slotname = slotentry.split('|')[1]
    if slotname == name:
       slotlist[(slotnum-1)] = None
       print('\nSuccess:\n' + name + ' has been cancelled from starting slot #' + str(slotnum))
    else:
        print('\nError:\n' + name + ' is not in that starting slot.')
    print('\n1. Cancel another participant\n2. Return to main menu')
    menu_item = int(input('Select: '))
    if menu_item == 1:
        cancel()
    elif menu_item == 2:
        menu()

def view():
    print('\nView Participants')
    print('============================')
    slotnum = int(input('Starting slot #: '))
    slotstart = slotnum - 6
    slotend = slotnum + 5
    if slotstart < 0:
        slotstart = 0
    if slotend > num_of_slots:
        slotend = num_of_slots
    displaylist = slotlist[slotstart:slotend]
    for a in displaylist:
        print(a)
    print('\n1. View another participant\n2. Return to main menu')
    menu_item = int(input('Select: '))
    if menu_item == 1:
        view()
    elif menu_item == 2:
        menu()

def save():
    print('\nSave Changes')
    print('============================')
    print('Save your changes to CSV? [y/n]')
    saveornaw = str(input('Select: '))
    if saveornaw == 'y':
        file = open('Tournament_Tracker.csv','w')
        file.write(str(slotlist))
        file.close()    
        print('\n1. Save again \n2. Return to main menu')
    elif saveornaw == 'n':
        print('\n1. Save again \n2. Return to main menu')
    menu_item = int(input('Select: '))
    if menu_item == 1:
        save()
    elif menu_item == 2:
        menu()

def exit():
    print('\nExit')
    print('============================')
    print('\nAny unsaved changes will be lost.\nAre you sure you want to exit? [y/n]')
    menu_item = str(input('Select: '))
    if menu_item == 'y':
        print('\nGoodbye')
    elif menu_item == 'n':
        menu()

def select():
    menu_item = int(input('Select: '))
    if menu_item == 1:
        signup()
    elif menu_item == 2:
        cancel()
    elif menu_item == 3:
        view()
    elif menu_item == 4:
        save()
    elif menu_item == 5:
        exit()

def menu():
    print('\nParticipant Menu')
    print('============================')
    print('1. Sign Up\n2. Cancel Sign Up\n3. View Participants\n4. Save Changes\n5. Exit\n')
    select()

menu()
