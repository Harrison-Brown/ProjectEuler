'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

exceptions={
	10:"ten",
	11:"eleven",
	12:"twelve",
	13:"thirteen",
	15:"fifteen",
	18:"eighteen",
	1000:"onethousand"}
	
numbers = {
	"ones":["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"],
	"tens":["teen", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
}
	
def get_digit(n, p): #returns the p digit of n; 0 -> ones, 1 -> tens
    place = 10 ** p
    digit = int((n // place)) % 10
    return digit

def word(n):
	word = ""
	if n in exceptions:
		return exceptions[n]
	if n%1000>=100: #finds word of hundreds place
		digit = get_digit(n, 2)
		word = word + numbers["ones"][digit-1] + "hundred"
		if n%100>=1:
			word = word + "and" #fixes issue with one hundred and one, etc
	if n%100>=10: #finds word of tens place
		if n%100 in exceptions:
			word = word + exceptions[n%100]
		else:
			digit = get_digit(n, 1)
			word = word + numbers["tens"][digit-1]
	if n%10>=1 and n%100 not in exceptions: 
		digit = get_digit(n, 0)
		word = word + numbers["ones"][digit-1]
	return word
		
total = 0
for i in range(1, 1001):
	str = word(i)
	total = total + len(str)
print(total)

#ANSWER: 21124