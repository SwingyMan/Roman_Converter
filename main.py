import sys
import re
regex = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
def validate_roman(string: str):
    result = re.match(regex, string)
    return result is not None

def convert(y):
    if y.isnumeric(): # arabska
        x = int(y)
        res = []
        if x>=4000:
            print("")
        else:
            while x != 0:
                if x >= 1000:
                    x -= 1000
                    res.append("M")
                elif x >= 900:
                    x -= 900
                    res.append("CM")
                elif x >= 500:
                    x -= 500
                    res.append("D")
                elif x >= 400:
                    x -= 400
                    res.append("CD")
                elif x >= 100:
                    x -= 100
                    res.append("C")
                elif x >= 90:
                    x -= 90
                    res.append("XC")
                elif x >= 50:
                    x -= 50
                    res.append("L")
                elif x >= 40:
                    x -= 40
                    res.append("XL")
                elif x >= 10:
                    x -= 10
                    res.append("X")
                elif x >= 9:
                    x -= 9
                    res.append("IX")
                elif x >= 5:
                    x -= 5
                    res.append("V")
                elif x == 4:
                    x -= 4
                    res.append("IV")
                else:
                    x -= 1
                    res.append("I")
            res = "".join(res)
            print(res)
    else:   #rzymska
    	if not validate_roman(y):
        	raise IOError("Zla cyfra rzymska")
    	translations = {
        	"I": 1,
        	"V": 5,
        	"X": 10,
        	"L": 50,
        	"C": 100,
        	"D": 500,
        	"M": 1000,
        	}
    	first_value = translations[y[0]]
    	if len(y) == 1:
        	print(first_value)
    	result = first_value if translations[y[1]] <= first_value else -first_value
    	for idx, letter in [x for x in enumerate(y)][2:]:
        	previous = y[idx-1]
        	if translations[letter] > translations[previous]:
            		result -= translations[previous]
            #  assuming it was added once already
        	else:
            		result += translations[previous]
    	result += translations[y[-1]]
    	print(result)
if __name__ == "__main__":
    convert(sys.argv[1])

