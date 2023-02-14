# ---------------------------------------------------Luke

class Garage():
    def __init__(self, num_of_tickets):
        self.num_of_tickets = num_of_tickets
        self.tickets = []
        self.parking = []
        self.current_ticket = {'paid': False}

    def create_garage(self):
        self.tickets = [i + 1 for i in range(self.num_of_tickets)]
        spaces_open = len(self.tickets) - len(self.parking)
        for i in range(spaces_open):
            self.parking.append('____')

    def space_display(self):
        print(f'\nSpaces open: {len(self.tickets)}')

    def display_garage(self):
        print('              / \ ')
        print('__________----|_|_______')
        parked = ''
        for i, x in enumerate(self.parking):
            if i % 2 == 0:
                parked += f'|_{x}     |'
            elif i % 2 == 1:
                parked += f'|_{x}     |'[::-1] + '\n'
        print(parked)

    def display_garage_spots(self):
        print('              / \ ')
        print('__________----|_|_______')
        parked = ''
        for i, x in enumerate(self.parking):
            if i % 2 == 0:
                parked += str(i+1) + f'|_{x}     |'
            elif i % 2 == 1:
                parked += f'|_{x}     |'[::-1] + str(i+1) + '\n'
        print(parked)

# -----------------------------------------------Emma

    def take_ticket(self):
        bike = '.-._'
        truck = ':-:='
        car = ':-:_'
        print('\n')
        vehicle = int(
            input('What kind of vehicle do you have? | 1: Car | 2: Truck | 3: Bike | :'))
        print('\n')
        parking_spot = int(input('What Spot would you like to take?'))
        print('\n')
        parking_spot -= 1
        if self.parking[parking_spot] == '____':
            if vehicle == 1:
                self.tickets.pop(parking_spot)
                self.parking.pop(parking_spot)
                self.parking[parking_spot:parking_spot] = [car]
            elif vehicle == 2:
                self.tickets.pop(parking_spot)
                self.parking.pop(parking_spot)
                self.parking[parking_spot:parking_spot] = [truck]
            elif vehicle == 3:
                self.tickets.pop(parking_spot)
                self.parking.pop(parking_spot)
                self.parking[parking_spot:parking_spot] = [bike]
            else:
                print('\t' + 'Please enter a valid number')
        else:
            print('Parking spot is already taken')
        print(f'Spot {parking_spot + 1} has been administered - Find your spot')

    def pay_for_parking(self):
        print('\n')
        amount = int(input('Please pay $15(type 15 for $15)'))
        if amount == 15:
            self.current_ticket['paid'] = True
            print('\n' + 'Thank you - You have 15 minutes to leave')
        else:
            print('\t' + 'Please pay the fixed amount')
            self.pay_for_parking()

    def leave_garage(self):
        parking_spot = int(input('What spot were you in?: '))
        parking_spot -= 1
        if self.parking[parking_spot] != '____':
            if self.current_ticket['paid'] == True:
                self.parking.pop(parking_spot)
                self.parking[parking_spot:parking_spot] = ['____']
                self.tickets[parking_spot:parking_spot] = [parking_spot + 1]
                self.current_ticket['paid'] = False
            else:
                print('Please pay for ticket')
                self.pay_for_parking()
        else:
            print('space is already empty')

# -------------------------------------------Luke

    def runner(self):
        self.space_display()
        self.display_garage()
        option = int(input(
            'Enter number to choose | 1: Take Ticket | 2: Pay | 3: Leave Garage | 4: Select Floor | :'))
        if option == 1:
            self.display_garage_spots()
            self.take_ticket()
            self.runner()
        elif option == 2:
            self.pay_for_parking()
        elif option == 3:
            self.display_garage_spots()
            self.leave_garage()
            print('\n' + 'Thank you, have a nice day!')
            self.runner()
        elif option == 4:
            main()
        else:
            self.runner()
        self.runner()

# -----------------------------------MAIN----------------------------------------------


print('\n\n----------------Welcome to our 2 floor garage!-------------------\n\n')
var = int(input('How many parking spaces are on each floor? :'))
print('\n')

floor1 = Garage(var)
floor2 = Garage(var)
floor1.create_garage()
floor2.create_garage()


def main():
    while True:
        var2 = int(input('\n\n\tSelect Floor 1 or 2 (4 to Exit) :'))
        if var2 == 1:
            print('\n\t--FLOOR 1--')
            floor1.runner()
        elif var2 == 2:
            print('\n\t--FLOOR 2--')
            floor2.runner()
        elif var2 == 4:
            exit()
        else:
            print('Error! Please type a valid number.')


main()
