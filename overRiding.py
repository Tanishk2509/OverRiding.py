class A: #parent
    def Disp(self):
        print("This is parent class method")
    
class B(A): #child
    def Disp(self):
        print("This is child class method")

obj=B()
obj.Disp()

# class A:   #parent
#     def Disp(self):
#         print("This is parent class method")

# class B(A):   #child
#     def Disp(self):
#       super().Disp()
#       print("This is child class method")

# obj=B()
# obj.Disp()