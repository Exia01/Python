print('Hello'.__len__()) #the built property and we can customize it 
class SpecialList: #using a class
 
    def __init__(self, data):
        self.__data = data
 
    # def __len__(self):  # changing the default attribute of length
    #     return 50

    def __len__(self):  # changing the default attribute of length
        return self.__data.__len__() //2


l1 = SpecialList([1,40,30,100,30,1,2,3,4])
l2 = SpecialList([1,3,4,5]) 

#since we've done a custom
print(len(l1)) #50
print(len(l2))  #50


print(len(l1)) #4
print(len(l2)) #2


