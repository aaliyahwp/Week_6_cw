from account import Account
# from the module (file) import the class
# create some object instances
# instantiation




lisa_account = Account(500)
bart_account = Account(100)
# We are calling a special method called the constructor
# I can now use that file to create an account for Lisa
# Python when we use brackets to call a function or a method and we can take arguments in there

# Once we have printed this is the object reference- where the memory is

# object.field
# object.method()

lisa_account.deposit(100)
bart_account.deposit(20)
# both calling the deposit method- we need a way of saying whose bank account is calling deposit

lisa_account.withdrawal(40)
bart_account.withdrawal(-40)

# print(lisa_account.get_balance())
# print(bart_account.get_balance())
# adding a second lot of open brackets close brackets as it's a method

# bart_account.get_firstname('Bart')
# lisa_account.get_firstname('Lisa')

lisa_account.transfer(bart_account, 40)
# created a balance tranfer by first inputting self(lisa here, then the account I wish to transfer the money to,
# then the amount I want to transfer within brackets
bart_account.transfer(lisa_account, 20)

lisa_account.dollartopound_deposit(20)
# deposited $20 into Lisa's account which using the function is then created converted into pounds
bart_account.dollartopound_withdrawal(40)
# Withdrew $40 from Bart's account which was then converted into pounds using the function
print(lisa_account.get_balance())
print(bart_account.get_balance())

