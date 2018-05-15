import datetime


class CreditCard:

    def __init__(self, amount):
        self.amount = amount
    limit = 1000

    def get_credit_limit(self):
        credit_limit = CreditCard.limit - self.amount
        return credit_limit

class DebitCard(CreditCard):
    def __init__(self, amount, debit_amount):
        super(DebitCard, self).__init__(amount)
        CreditCard.amount = amount
        self.debit_amount = debit_amount

    def balance(self):
        print("Debit Card balance: {}".format(self.debit_amount))

    def pay_credit_bill(self, pay_amount):
        self.pay_amount = pay_amount
        if self.pay_amount > self.debit_amount:
            print("Not enough funds")
        else:
            self.debit_amount -= self.pay_amount
            CreditCard.amount -= self.pay_amount
            print("\nTransaction Successful at {}".format(datetime.datetime.now()))
            print("Debit Card balance: {}".format(self.debit_amount))
            my_val = CreditCard.amount + value.get_credit_limit()
            print("Remaining Credit Card Limit :", my_val)
            print("Remaining Credit Card balance to pay : ", CreditCard.amount)


val = int(input("\nYour current credit card balance is: "))
value = CreditCard(val)
print("Remaining Credit Card Limit :", value.get_credit_limit())

debit_card_amt = int(input("\nEnter your debit card amount: "))
value = DebitCard(val, debit_card_amt)

inp = int(input("\nCredit card bill to pay:  current balance = {}: ".format(val)))
value.pay_credit_bill(inp)
value.get_credit_limit()