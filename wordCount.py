class wordCount:
    def wordCount(self, input):
        if (type(input) is not str):
            raise TypeError("Only Strings are allowed")
        else:
            numWords = 0
            for char in input:
                if (char == ' '):
                    numWords += 1
            return numWords + 1
