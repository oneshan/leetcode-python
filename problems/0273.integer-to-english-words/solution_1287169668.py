# 0273 - Integer to English Words
# Date: 2024-06-13
# Runtime: 36 ms, Memory: 16.9 MB
# Submission Id: 1287169668


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'

        to19 = (',One,Two,Three,Four,Five,Six,Seven,Eight,Nine,Ten,'
                'Eleven,Twelve,Thirteen,Fourteen,Fifteen,Sixteen,'
                'Seventeen,Eighteen,Nineteen').split(',')
        tens = (',Ten,Twenty,Thirty,Forty,Fifty,Sixty,Seventy,Eighty,Ninety').split(',')

        def get_word(num):
            res = []
            if num >= 1_000_000_000:
                prev, num = divmod(num, 1_000_000_000)
                res.append(get_word(prev))
                res.append('Billion')
            if num >= 1_000_000:
                prev, num = divmod(num, 1_000_000)
                res.append(get_word(prev))
                res.append('Million')
            if num >= 1_000:
                prev, num = divmod(num, 1_000)
                res.append(get_word(prev))
                res.append('Thousand')
            if num >= 100:
                prev, num = divmod(num, 100)
                res.append(get_word(prev))
                res.append('Hundred')
            if num >= 20:
                prev, num = divmod(num, 10)
                res.append(tens[prev])
            if num > 0:         
                res.append(to19[num])
            return ' '.join(res)

        return get_word(num)