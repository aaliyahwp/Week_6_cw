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

print(lisa_account.get_balance())
print(bart_account.get_balance())
# adding a second lot of open brackets close brackets as it's a method

