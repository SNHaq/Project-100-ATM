class ATM(object):
    def __init__(self, cardNumber, pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber

    def cashWithdrawal():
        print("You have successfully withdrawed some money from your account.")

    def balanceEnquiry():
        print("You're making a balance enquiry.")

transaction = ATM(1000, 10000)
print(transaction.cashWithdrawal())
print(transaction.balanceEnquiry())