import math

class BiSearch:
    @staticmethod
    def search(word_dict, target):
        result = target in word_dict.values()            
        return result
