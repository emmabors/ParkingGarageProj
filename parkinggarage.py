class Garage():
    def __init__(self, num_of_tickets):
        self.num_of_tickets = num_of_tickets
        self.tickets = []
        self.parking = []
        self.current_ticket = {}

    def space_display(self):
        print(f'\nSpaces open: {len(self.tickets)}')

    def create_garage(self):       
        self.tickets = [i for i in range(self.num_of_tickets)]
        spaces_open = len(self.tickets) - len(self.parking)
        for i in range(spaces_open):
            self.parking.append('____')
        print('              / \ ')
        print('__________----|_|_______')
        parked = ''
        for i, x in enumerate(self.parking):
            if i % 2 == 0:
                parked += f'|_{x}     |'
            elif i % 2 == 1:
                parked += f'|_{x}     |'[::-1] +  '\n'
        print(parked)

    # def take_ticket(self):
    #     bike = '.-._'
    #     truck = ':-:='
    #     car = ':-:_'
    #     vehicle = int(input('What kind of vehicle do you have? | 1: Car | 2: Truck | 3: Bike |'))
    #     parking_spot = int(input('What Spot would you like to take?'))
    #     if  self.parking[parking_spot] == '____':
    #         if vehicle == 1:
    #             #pop and splice
    #         elif vehicle == 2:
    #             #pop and splice
    #         elif vehicle == 3:
    #             #pop and splice
    #         else:
    #                 print('Please enter a valid number')
    #     else:
    #         print('Parking spot is already taken')
    #     print(f'{parking_spot} ticket has been administered - find open spot')

    def pay_for_parking(self):
        amount = input('Please pay $15(type 15 for $15)')
        if amount == 15:
            self.current_ticket['paid'] = True
        else: 
            print('Please pay the fixed amount')
        self.pay_for_parking()       
    
    # def leave_garage(self):
        #input for what parking_spot they are in
        #if  self.parking[parking_spot] != '____':
        # if self.current_ticket.values() == True:
        #     print('Thank you, have a nice day!')
        #     self.tickets.append(ticket)
        # if self.current_ticket.values() == False:
        #     self.pay_for_parking()
        #pop and splice


    def runner(self):
        self.create_garage()
        self.take_ticket()
        self.create_garage()
        self.space_display()
        print(self.tickets)


luke = Garage(20)
luke.runner()
