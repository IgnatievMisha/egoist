try:
    print("start code")
    print(error)
    print("end")
except:
    print("no problems")
print("any code...")
'''
def checker(var):
    if type(var)!=str:
        raise TypeError(f'We dont working with {type(var)}, we need for str')
    else:
        return var
checker(1234)
'''
class BuildingError(Exception):
    def __str__(self):
        return "Something get wrong"
def check_material(amount, limit):
    if amount>limit:
        return "over"
    else:
        raise BuildingError()
print(check_material(10,354))