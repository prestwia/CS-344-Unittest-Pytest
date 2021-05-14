class wordCount:
    def wordCount(self, input):
        if (type(input) is not str):
            return "Invalid type, input must be string."
        else:
            numWords = 0
            for char in input:
                if (char == ' '):
                    numWords += 1
            return numWords + 1
