
class SubstringChecker():
    def __init__(self,word):
        self.word = word
    
    def get_length_longest_substring(self):
        substrings  = self.get_distinct_substrings()
        print("all substrings- ",substrings)
        highest_number,substring = self.get_longest_substring(substrings)
        print("the longest substring is ", substring, "with a length of ",highest_number)
        return substring
    
    def get_distinct_substrings(self):
        length_of_word = len(self.word) 
        pointer = 0
        all_transversed = False
        substrings = {}
        current_word = ""
        x = 0
        length_of_transversal = length_of_word - pointer 

        while(not all_transversed):
            for i in range(length_of_transversal):
                i = i + x #updating counter based on pointer 
                
                if (i == length_of_word-1):
                    if (self.word[i] not in current_word):
                        current_word += self.word[i]
                        substrings[len(current_word)] = current_word
                    else:
                        substrings[len(self.word[i])] = self.word[i]
                    all_transversed = True
                    break
               
                if((self.word[i] != self.word[i+1]) and (self.word[i+1] not in current_word)):
                    current_word += self.word[i]
                   
                else:
                    current_word += self.word[i]
                    pointer  = i+1
                    substrings[len(current_word)] = current_word
                    length_of_transversal = length_of_word - pointer 
                    x = length_of_word - length_of_transversal
                    current_word = ""
                    break

        return substrings

    def get_longest_substring(self,substrings):
        highest_num = 0
        for key in substrings:
            if (key > highest_num):
                highest_num = key
        return highest_num,substrings[highest_num]


word = "abcabcdc"
# word = "bbbbb"
substring_checker = SubstringChecker(word)
substring_checker.get_length_longest_substring()