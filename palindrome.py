class Palindrome:
    def palindrome(self, input):
        if (type(input) is not str):
            return "Invalid type, input must be string."
        else:
            if (len(input) % 2 == 0):
                for i in range(int(len(input) / 2)):
                    if (input[i] == input[len(input) - 1 - i]):
                        continue
                    else:
                        return False
            else:
                for i in range(len(input) // 2):
                    if (input[i] == input[len(input) - 1 - i]):
                        continue
                    else:
                        return False
            return True
