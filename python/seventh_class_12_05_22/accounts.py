from oop_principles import StudentImpl


class Account(StudentImpl):

    def __init__(self, name, dept, sem, credits, per_credit_fees, waiver):
        super(Account, self).__init__(name=name, dept=dept)
        self.__sem = sem
        self.__credits = credits
        self.__per_credit_fees = per_credit_fees
        self.__total_fees = 0.0
        self.__is_registered = False
        self.__have_waiver = waiver

    def total_amount(self):
        self.__total_fees = self.__credits * self.__per_credit_fees
        return self.__total_fees

    def due_amount(self):
        return self.__total_fees

    def check_waiver(self, amount=0.0):
        if self.__have_waiver == True:
            self.__total_fees = self.__total_fees - amount
            print(self.__total_fees)
        else:
            print("You have no waiver")

    def first_payble_amount(self):
        return (self.__total_fees * 40) / 100

    def get_registration(self, payment):
        if self.first_payble_amount() >= payment:
            print("Amount is Smaller then first payment {} your have to pay {}".format(payment,
                                                                                       self.first_payble_amount()))

        else:
            print("Weldone you complete your first payment {}".format(payment))
            print("You are registered for {}".format(self.__sem))
            self.__total_fees = self.__total_fees - payment
            self.__is_registered = True

    def check_registration(self):
        return self.__is_registered


# acc = Account("Shaykh Imran", "Islamic Scholar")
#
# print(acc)
# print(acc.getName())
# print(acc.getDept())
