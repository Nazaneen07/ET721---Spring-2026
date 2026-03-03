"""
Nazaneen Baguaei,
lab 9, unit testing
feb 26, 2026
"""
import unittest
from bankaccount import *

class TestBankAccount(unittest.TestCase):
    # create a test template (instance of the class)
    def setUp(self):
        self.account1 = BankAccount("Peter")

    # test that the account is initialized with the correct balance
    def test_initial_balance(self):
        self.assertEqual(self.account1.get_balance(), 0)

    # test that a deposit operation correctly adds the specified amount to the balance
    def test_deposit(self):
        self.account1.deposit(500)
        self.assertEqual(self.account1.get_balance(), 500)

    # test that a withdrawal operation correctly subtracts the specified amount from the balance
    def test_withdraw(self):
        self.account1.deposit(1000)
        self.account1.withdraw(400)
        self.assertEqual(self.account1.get_balance(), 600)

    # test that attempting to withdraw more than the available balance raises the appropriate exception
    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account1.withdraw(2000)

    # test a sequence of deposits and withdrawals to ensure correct balance calculations
    def test_sequence(self):
        self.account1.deposit(500)
        self.assertEqual(self.account1.get_balance(), 500)
        self.account1.withdraw(200)
        self.assertEqual(self.account1.get_balance(), 300)
        self.account1.deposit(100)
        self.assertEqual(self.account1.get_balance(), 400)

if __name__ == "__main__":
    unittest.main()