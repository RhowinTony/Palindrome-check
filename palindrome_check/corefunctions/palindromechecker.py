"""
    Value = input("Enter a string ").lower()
    filtered_data =filter(Value)
    is_palindrome = palindrome(filtered_data)
"""

class Palindromecheck:
    def __init__(self, inp_val:str) -> None:
        try:
            self.givenstring = inp_val.lower()
            print(self.givenstring)
        except KeyboardInterrupt:
            print("\n Program interptd by user")            

  
    def str_filter(self):
        str_filterer = "abcdefghijklmnopqrstuvwxyz1234567890"
        filtered_data = ""
        for i in self.givenstring:
            if i in str_filterer:
                filtered_data = filtered_data + i
        print(filtered_data)
        return filtered_data

    def palindrome(self):
        i = 0
        length = len(self)
        inpu = list(self)
        output = []
        while length > 0 :
            i = i - 1
            length = length - 1
            output.append(self[i])
        return output == inpu

    def get_result(self):
        filtered_dat = self.str_filter()
        is_palindrome = self.palindrome()
        if is_palindrome:
            print("The given string is a palindrome")
        else:
            print("The given string is not a palindrome")





