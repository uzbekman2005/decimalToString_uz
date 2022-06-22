class IntToStr:
    def __init__(self, num):
        self.num = num
        self.birlik = {
            1:"bir",
            2: "ikki",
            3: "uch",
            4: "to'rt",
            5: "besh",
            6: "olti",
            7: "yetti",
            8: "sakkiz",
            9: "to'qqiz",
            0: ""
        }
        self.onlik = {
            1:"o'n",
            2: "yigirma",
            3: "o'ttiz",
            4: "qirq",
            5: "ellik",
            6: "oltmish",
            7: "yetmish",
            8: "sakson",
            9: "to'qson",
            0: ""
        }
        self.yuz = "yuz"
        self.ming = "ming"
        self.million ="million"

        self.milliard ="milliard"

    def converter(self):
        temp = str(self.num)
        birlikk=unlik=yuzlik=minglik=unminglik=yuzminglik=millionlik=onmillionlik=yuzmillionlik=milliardlik=0
        for i in range(len(temp)-1,-1, -1):
            if i == len(temp)-1:
                birlikk = int(temp[i])
            elif i == len(temp)-2:
                unlik = int(temp[i])
            elif i == len(temp)-3:
                yuzlik = int(temp[i])
            elif i == len(temp)-4:
                minglik = int(temp[i])
            elif i == len(temp)-5:
                unminglik = int(temp[i])
            elif i == len(temp)-6:
                yuzminglik = int(temp[i])
            elif i == len(temp)-7:
                millionlik = int(temp[i])
            elif i == len(temp)-8:
                onmillionlik = int(temp[i])
            elif i == len(temp)-9:
                yuzmillionlik = int(temp[i])
            elif i == len(temp)-10:
                milliardlik = int(temp[i])

        bil = f"{self.birlik[milliardlik]} {self.milliard}" if milliardlik != 0 else ""
        yuzMil = f"{self.birlik[yuzmillionlik]} {self.yuz}" if yuzmillionlik != 0 else ""
        unMil = f"{self.onlik[onmillionlik]}" if onmillionlik != 0 else ''
        mil = f"{self.birlik[millionlik]}" if millionlik != 0 else ""
        yuzmin = f"{self.birlik[yuzminglik]} {self.yuz}" if yuzminglik != 0 else ""
        unmin = f"{self.onlik[unminglik]}" if unminglik != 0 else ""
        ming = f"{self.birlik[minglik]}\n" if minglik != 0 else ""
        yu = f"{self.birlik[yuzlik]} {self.yuz}" if yuzlik != 0 else ""
        unl = f"{self.onlik[unlik]}" if unlik != 0 else ""
        birl = f"{self.birlik[birlikk]}" if birlikk != 0 else ""
        result = bil + " " + yuzMil + " " + unMil + " " + mil + " "
        result = result + self.million if yuzmillionlik != 0 or onmillionlik != 0 or millionlik != 0 else result
        result += " " +yuzmin + " " + unmin + " " + ming + " "
        result += self.ming if minglik != 0 or yuzminglik != 0 or unminglik != 0 else ""
        result += " " +yu + " " + unl + " " + birl
        result = result.replace("  ", " ")
        result = result.replace("  ", " ")
        result = result.replace("  ", " ")
        result = result.replace("  ", " ")
        result = result.replace("  ", " ")
        result = result.replace("  ", " ")
        result = result.strip()
        return result[0].title() + result[1:]


