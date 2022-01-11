class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        # clean
        card_num = self.card_num.replace(' ', '')
        
        if len(card_num) < 2:
            return False

        if not card_num.isdigit():
            return False
        
        digits = [int(d) for d in card_num]

        def transform(d):
            d = d*2
            if d > 9:
                d -= 9
            return d
        
        odd_sum = sum(digits[len(digits)-1:: -2])
        even_sum = sum([transform(d) for d in digits[len(digits)-2:: -2]])

        print(odd_sum, even_sum)
        
        total = odd_sum + even_sum
        
        return total%10 == 0
                
            
