"""
    Value = input("Enter a string ").lower()
    filtered_data =filter(Value)
    is_palindrome = palindrome(filtered_data)
"""

class Palindromecheck:
    def __init__(self, inp_val:str) -> None:
        try:
            self.givenstring = inp_val.lower()
        except KeyboardInterrupt:
            print("\n Program interruptd by user")            

  
    def str_filter(self):
        str_filters = "abcdefghijklmnopqrstuvwxyz1234567890"
        filtered_data = ""
        for i in self.givenstring:
            if i in str_filters:
                filtered_data = filtered_data + i
        return filtered_data

    def reverse_check(self,filtered_dat):
        i = 0
        length = len(filtered_dat)
        inpu = list(filtered_dat)
        output = []
        while length > 0 :
            i = i - 1
            length = length - 1
            output.append(filtered_dat[i])
        return output == inpu

    def get_result(self):
        filtered_dat = self.str_filter()
        is_palindrome = self.reverse_check(filtered_dat)
        if is_palindrome:
            print("The given string is a palindrome")
        else:
            print("The given string is not a palindrome")
        print("_*___*_"*6)






