# from abc import ABC, abstractmethod   # this importation is first and foremost requirement in abstraction code.
#
# NOTE : User can never create obj of main class or abstracted class, For us, Bank is main class.
#      : abstraction can be used for hide implementation code.
#      : both code(commented and uncommented) are almost same. Here I just try to show how can we hide code, through Bank example.
#      : You can practice abstraction code by deriving area value of all geometric-shapes.
#
# class Bank(ABC): 
#
#     def strings(self):
#         print('This is calling from abstract class to provide string')
#
#     @abstractmethod
#     def total_AMt(self):
#         pass
#
#     @abstractmethod
#     def deposite(self, deposite_amt):
#         pass
#
#     @abstractmethod
#     def withdraw(self, withdraw_amt):
#         pass
#
#
#
# #
# class Candidate_name(Bank):
#
#     def __init__(self, name, start_amt):
#         self.name = name
#         self.start_amt = start_amt
#         self.total_Amt = start_amt
#         self.trans_list = []
#
#     def total_AMt(self):
#         # self.total_Amt = self.start_amt
#         return self.total_Amt
#
#     def deposite(self, deposite_amt):
#         self.deposite_amt = deposite_amt
#         if deposite_amt > 0:
#             self.total_Amt = self.total_Amt + self.deposite_amt
#             self.trans_list.append(('deposited', self.deposite_amt))
#             return self.total_Amt
#         else:
#             return 'Please provide proper digit'
#
#     def withdraw(self, withdraw_amt):
#         # self.withdraw = withdraw_amt
#         if withdraw_amt < self.total_Amt:
#             self.withdraw_amt = withdraw_amt
#             self.total_Amt = self.total_Amt - self.withdraw_amt
#             self.trans_list.append(('withdrew', self.withdraw_amt))
#             return self.total_Amt
#
#         else:
#             return 'this is out of bound'
#
#
#
#
#
# lists = [Candidate_name('Bhavik', 1000), Candidate_name('Vishal', 2000), Candidate_name('Jaydeep', 3000), Candidate_name('Haresh', 5000)]
# Bank_amt = 0
#
# lists[0].deposite(100)
# lists[0].withdraw(200)
# lists[1].withdraw(200)
# lists[2].withdraw(400)
#
#
# for candidate in lists:
#     Bank_amt = Bank_amt + candidate.total_AMt()
#     if len(candidate.trans_list) != 0:
#         print(f'Candidate {candidate.name} has done transaction {candidate.trans_list} and total balance left is {candidate.total_AMt()}')
#     else:
#         print(f'Candidate {candidate.name} has well maintained account and total balance left is {candidate.total_AMt()}')
#
# print(Bank_amt)

# ----------------------------------------------------------------------------------------------------------------------------------------------

from abc import ABC, abstractmethod


class Bank(ABC):

    def __init__(self, name, start_amt):
        self.name = name
        self.start_amt = start_amt
        self.total_Amt = start_amt
        self.trans_list = []

    def strings(self):
        print('This is calling from abstract class to provide string')

    @abstractmethod
    def total_AMt(self):
        pass

    @abstractmethod
    def deposite(self, deposite_amt):
        pass

    @abstractmethod
    def withdraw(self, withdraw_amt):
        pass



#
class Candidate_name(Bank):


    def total_AMt(self):
        # self.total_Amt = self.start_amt
        return self.total_Amt

    def deposite(self, deposite_amt):
        self.deposite_amt = deposite_amt
        if deposite_amt > 0:
            self.total_Amt = self.total_Amt + self.deposite_amt
            self.trans_list.append(('deposited', self.deposite_amt))
            return self.total_Amt
        else:
            return 'Please provide proper digit'

    def withdraw(self, withdraw_amt):
        # self.withdraw = withdraw_amt
        if withdraw_amt < self.total_Amt:
            self.withdraw_amt = withdraw_amt
            self.total_Amt = self.total_Amt - self.withdraw_amt
            self.trans_list.append(('withdrew', self.withdraw_amt))
            return self.total_Amt

        else:
            return 'this is out of bound'




lists = [Candidate_name('Bhavik', 1000), Candidate_name('Vishal', 2000), Candidate_name('Jaydeep', 3000), Candidate_name('Haresh', 5000)]
Bank_amt = 0

lists[0].deposite(100)
lists[0].withdraw(200)
lists[1].withdraw(200)
lists[2].withdraw(400)


for candidate in lists:
    Bank_amt = Bank_amt + candidate.total_AMt()
    if len(candidate.trans_list) != 0:
        print(f'Candidate {candidate.name} has done transaction {candidate.trans_list} and total balance left is {candidate.total_AMt()}')
    else:
        print(f'Candidate {candidate.name} has well maintained account and total balance left is {candidate.total_AMt()}')

print(Bank_amt)
