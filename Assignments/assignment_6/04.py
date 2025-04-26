class Bank:
    bank_name = "SONERI BANK"
    def Change_BankName( cls ,new_name ,bank_name = "SONERI BANK"):
        cls.bank_name = new_name
        print(f"Bank Name Changed {bank_name}  to {cls.bank_name}")


user1 = Bank()
user2 = Bank()
user1.Change_BankName("HBL")
print(user1.bank_name)