
def convert(y):
    if y.isnumeric(): # arabska
        x = int(y)
        res = []
        if x>=4000:
            print("za duża liczba")
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
            return res
    else:   #rzymska
        dict = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
            1:"I",
            4:"IV",
            5:"V",
            9:"IX",
            10:"X",
            40:"XL",
            50:"L",
            90:"XC",
            100:"C",
            400:"CD",
            500:"D",
            900:"CM",
            1000:"M"
        }
        dict2 = {
            "I":0,
            "V":1,
            "X":2,
            "L":3,
            "C":4,
            "D":5,
            "M":6
        }
        tabCount=[0,0,0,0,0,0,0]
        result = int(0)
        temp = 0
        flag = False
        counter = 0
        for letter in y:
            if letter == "M" or letter == "D" or letter == "C" or letter == "L" or letter == "X" or letter == "V" or letter == "I":
                tabCount[dict2[letter]] +=1
                if tabCount[0] > 3 or tabCount[1] > 3 or tabCount[2] > 3 or tabCount[3] > 3 or tabCount[4] > 3 or tabCount[5] > 3 or tabCount[6] > 3:
                    flag = True
                    break
                if counter != 0 and dict[letter]>temp:
                    if temp!=0:
                        temp1 = dict[letter]
                        try:
                            if dict[temp1-temp] =="IV" in dict or dict[temp1-temp] =="IX" in dict or dict[temp1-temp] =="XL" in dict or dict[temp1-temp] =="XC" in dict or dict[temp1-temp] =="CD" in dict or dict[temp1-temp] =="CM" in dict:
                                temp2 = dict[temp1-temp]
                                temp3 = dict[temp2]
                                result += temp3-temp
                                counter +=1
                        except:
                            flag = True
                            break
                    else:
                        flag = True
                        break
                else:
                    temp = dict[letter]
                    result += temp
                    counter +=1
            else:
                flag = True
                break
            if (result >= 4000):
                flag = True
            else:
                flag = False
        if (flag == True):
            return "Zly zapis"
        else:
            return result


