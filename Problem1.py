#Time Complexity :- O(1)
#Space Complexity :- O(1)

class Solution:
    def numberToWords(self, num: int) -> str:
        
        higherPlaces = ['','Thousand','Million', 'Billion']

        if num==0:
            return 'Zero'
        result = ''
        i=0
        while num > 0:
            if num%1000!= 0:
                result = self.helper(num%1000)+higherPlaces[i]+' '+ result
            num = num//1000
            i+=1
        return result.strip()
    

    def helper(self, num):
        below20 = {0:'',1:'One', 2:'Two', 3:'Three',4:'Four', 5:'Five',6:'Six', 7:'Seven', 8:'Eight', 9:'Nine',10:'Ten', 11:'Eleven',12:'Twelve', 13:'Thirteen',14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen', 19:'Nineteen'}
        tensPlace= {0:'',2:'Twenty', 3:'Thirty', 4:'Forty', 5:'Fifty', 6:'Sixty', 7:'Seventy', 8:'Eighty',9:'Ninety'}
        if num==0:
            return ''
        if num < 20:
            return below20[num]+' '
        elif num<100:
            return tensPlace[num//10]+' '+self.helper(num%10)
        else:
            return below20[num//100]+' '+'Hundred '+self.helper(num%100)
        