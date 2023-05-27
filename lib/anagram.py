# # your code goes here!

class Anagram:
    def __init__(self, word):
        letters = [letter for letter in word]
        self.letters = sorted(letters)

    def match(self,words_list):
        match_list = []
        for each_word in words_list:
            # ask about iine 12 why letter for letter in each_word. why not just start with for
            element = [letter for letter in each_word]
            sorted_element = sorted(element)
            if sorted_element == self.letters:
                match_list.append(each_word)
                print("match_list,", match_list)
        return match_list

# class Anagram:
#     def __init__(self, word):
#         self.word_letters = sorted([letter for letter in word])

#     def match(self, word_list):
#         match_word_list = []

#         for word in word_list:
#             if sorted([letter for letter in word]) == self.word_letters:
#                 match_word_list.append(word)

#         return match_word_list