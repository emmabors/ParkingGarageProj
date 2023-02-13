class Garage(): 
   
    def __init__(self):
        self.tickets = tickets [1,2,3,4,5,6,7,8,9,10]
        self.parking_spots = parking_spots [1,2,3,4,5,6,7,8,9,10]
        self.current_ticket = {}
    
    def take_ticket(self):
        if self.tickets >= 1:
            print(f'{ticket} ticket has been administered - find open spot')
            tickets.pop()
            parking_spots.pop()
    
    def pay_for_parking(self):
        amount = input('Please pay $15(type 15 for $15)')
        if amount == 15:
            current_ticket['paid'] = True
    
    def current_tickets(self):
        for key, value in self.current_ticket():
            print(key, value)
        
    
    def leave_garage(self):
        if current_ticket.values() == True:
            print('Thank you, have a nice day!')
            self.tickets.append(ticket)
        if current_ticket.values() == False:
            self.pay_for_parking()