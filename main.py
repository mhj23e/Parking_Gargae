class ParkingGarage:
    def __init__(self):
        self.tickets = []
        self.parking_spaces = []
        self.current_ticket = {}
    
    def take_ticket(self):
        self.tickets.pop()
        self.parking_spaces.pop()
    
    def pay_for_parking(self):
        payment = input("Please enter payment amount: ")
        if payment:
            print("Thank you for your payment. You have 15 minutes to leave the garage.")
            self.current_ticket["paid"] = True
    
    def leave_garage(self):
        if self.current_ticket.get("paid", False):
            print("Thank you, have a nice day!")
        else:
            payment = input("Please enter payment amount: ")
            if payment:
                print("Thank you for your payment. Have a nice day!")
        self.parking_spaces.append(1)
        self.tickets.append(1)
