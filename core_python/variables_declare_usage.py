def variables():
    var1: str = "ashok"  # varible var1 declared type is string and value is "ashok"
    var2: str = "kumar"  # varible var2 declared type is string and value is "kumar"
    print("My first name is {} and last name is {}".format(var1, var2))
    print(id(var1))
    var1, var2 = var2, var1
    print(var1, var2)
    print(id(var1))
    name = 'ashok'
    print(id(name))

    _new = "variable "  # Private Variable
    print(id(_new))
    return var1
