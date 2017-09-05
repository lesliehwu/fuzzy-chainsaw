def type_list(unknown):
    my_sum = 0
    words = ""
    what_am_i = ""
    print_me = ""
    for el in unknown:
        if(type(el) is int or type(el) is float):
            my_sum += el
        elif(type(el) is str):
            words += el
            words += " "
        
    if(words == ""):
        what_am_i = "integer"
        print_me = "Sum: " + str(my_sum)
    elif(words != "" and my_sum == 0):
        what_am_i = "string"
        print_me = "String: " + words
    elif(words != "" and my_sum != 0):
        what_am_i = "mixed"
        print_me = "String: " + words + "\nSum: " + str(my_sum)

    
    print("The list you entered is of", what_am_i,"type")
    print(print_me)

list1 = ['magical unicorns',19,'hello',98.98,'world']
list2 = [2,3,1,7,4,12]
list3 = ['magical','unicorns']


type_list(list1)
#Expected output:
#The list you entered is of mixed type
#String: magical unicorns hello world
#Sum: 117.98

type_list(list2)
#Expected output:
#The list you entered is of integer type
#Sum: 29

type_list(list3)
#Expected output:
#The list you entered is of string type
#String: magical unicorns
