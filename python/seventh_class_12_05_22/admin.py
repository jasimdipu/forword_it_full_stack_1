from accounts import Account

account = Account("Rahim", "Marketing", "6th", 20, 5000, True)

print(account.total_amount())
print(account.check_waiver(20000))
print(account.check_registration())
print(account.first_payble_amount())
print(account.get_registration(33000))
print(account.check_registration())
