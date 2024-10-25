class Car:
    def __init__ (self,**kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]


my_car = Car(make="Nissan",model="gtr")
# print(my_car.model)
# print(my_car.make)
print(my_car["model"])
print(my_car["make"])


# def calculate(n,**kwargs):
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)

# calculate(2,add=3,multiply=5)



# # total = 0
# # def add(*args):
# #     global total
# #     for n in args:
# #         total+=n


# # add(2,3,4,1)
# # print(total)