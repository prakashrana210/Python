



# class Mobile:
#     def __init__(self, m, p):
#         self.model = m
#         self.price = p
#
#     def show_model(self, MF):
#         self.MF = MF
#         print("model :" self.model, "price :" self.price, "MF :", self.MF)
#
# x = mobile("realme,", "16000,")
# x.show_model ("2806")

class Mobile:
    def __init__(self, m, p):
        self.model = m
        self.price = p

    def show_model(self, MF):
        self.MF = MF
        print("model :", self.model, "price :", self.price, "MF :", self.MF )

x = Mobile("realme,", "16000,")
x.show_model("7.november")