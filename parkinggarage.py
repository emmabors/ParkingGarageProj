class Garage():
    def __init__(self, num_of_tickets):
        self.num_of_tickets = num_of_tickets
        self.tickets = []
        self.parking = []
        self.current_ticket = {}

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
                parked += f'|_{x}     |'[::-1] +  '\n'
        print(parked)

    def take_ticket(self):
        bike = '.-._'
        truck = ':-:='
        car = ':-:_'
        vehicle = int(input('What kind of vehicle do you have? | 1: Car | 2: Truck | 3: Bike |'))
        parking_spot = int(input('What Spot would you like to take?'))
        parking_spot -= 1
        if  self.parking[parking_spot] == '____':
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
                print('Please enter a valid number')
        else:
            print('Parking spot is already taken')
        print(f'{parking_spot} ticket has been administered - find open spot')

    def pay_for_parking(self):
        amount = int(input('Please pay $15(type 15 for $15)'))
        if amount == 15:
            self.current_ticket['paid'] = True
        else: 
            print('Please pay the fixed amount')
            self.pay_for_parking()       
    
    def leave_garage(self):
        parking_spot = int(input('What spot were you in?: '))
        parking_spot -= 1
        if  self.parking[parking_spot] != '____':
            if self.current_ticket['paid'] == True:
                self.parking.pop(parking_spot)
                self.parking[parking_spot:parking_spot] = ['____']
                self.tickets[parking_spot:parking_spot] = [parking_spot + 1] 
            else:
                self.pay_for_parking()
        else:
            print('space is already empty')
        print('Thank you, have a nice day!')
                   


    def runner(self):
        self.create_garage()
        print(self.tickets)
        self.display_garage()
        self.take_ticket()
        self.space_display()
        self.display_garage()
        self.pay_for_parking()
        self.leave_garage()
        print(self.tickets)
        self.display_garage()
        


luke = Garage(20)
luke.runner()
