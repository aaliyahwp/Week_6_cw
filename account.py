# class - classification of a type
# a class is a blueprint
# DATA + BEHAVIOUR
# fields + methods
# a method is a function in a class
# a class is a code template for creating objects
# objects

class Account:



    def __init__(self, opening_amount):
        self.balance = opening_amount

    # it's a special method that the computer understands- it's a constructore
    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance

    #     A getter - a method that lets us get at out data
    # There are two things in classes - data and behaviour
    # Pass doesn't do anything
    # += is a way to add a variable to an existing variable

    def withdrawal(self, amount):
        amount = abs(amount)
        # once you have made it into an absolute number you now have the correct number that will be withdrawn
        if self.balance > amount:
            self.balance -= amount
        else:
            return self.balance

    # getter

    def get_firstname(self):
        return self.get_firstname
        #     A getter is what we want to use to read code encapsulated inside the class
        # a setter is used to write something that is hidden inside the class
        self.get_firstname = firstname

    def transfer(self, to_account, amount):
        self.withdrawal(amount)
        to_account.deposit(amount)

    def dollartopound_deposit(self, foreign_currency):
        self.deposit(0.84 * (foreign_currency))

    def dollartopound_withdrawal(self, foreign_currency):
        self.withdrawal(0.84 * (foreign_currency))
# Created the above two funtions to convert US dollars into pounds

# Created a function to transfer an amount, first I have inputted the self (the person from which the money is coming), then the count the money is going to and then finally the amount I wish to transfer
# I have then used the functions I already created to ensure that money is withdrawn from the account that made the transfer and deposited to the account that will receieve the money





# encapsulation - mapping something up inside of a capsule - in python this means hiding stuff
# The person that creates the internals of something can completely change how it works- doesn't change how the car looks - this remains the same


# When we put _ at the start of something it conveys meaning to a colleague
# When we add a single underscore or double underscore this means something to me as a python developer
# When you see a single/ double __ in the front of a field in python- steer clear
# single underscore- private, double underscore is double private


#  absolute number is also always pos
# We are allowed to use capital letters with accounts
# with class apart from 'class everything will be indented
