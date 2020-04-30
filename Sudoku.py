class point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.len = 9
        self.fin = 0
        self.valarr=list(range(1,10))
    def delval(self, val):
        if self.fin == 0:
            try:
                self.valarr.remove(val)
                self.len -= 1
            except:
                pass
    def setval(self, val):
        self.fin=1
        self.len=1
        self.valarr = [val]

def removenum(x,y,val,area):
    for liney in range(9):
        area[9*liney+x].delval(val)
    for linex in range(9):
        area[9*y+linex].delval(val)
    for squarex in range(3):
        for squarey in range(3):
            tempx=int(x/3)*3+squarex
            tempy=int(y/3)*3+squarey
            area[9*tempy+tempx].delval(val)

def solve(input):
    if 0 not in input:
        return input
    area = []
    for y in range(9):
        for x in range(9):
            area.append(point(x,y))

    for y in range(9):
        for x in range(9):
            val=input[9*y+x]
            if val == 0:
                continue

            area[9*y+x].setval(val)
            removenum(x,y,val,area)


    for po in range(81):
        if area[po].len == 0:
            return 0

    for po in range(81):
        if area[po].len == 1:
            if area[po].fin==1:
                continue
            else:
                tempinput = input.copy()
                tempinput[po] = area[po].valarr[0]
                output = solve(tempinput)
                if output == 0:
                    return 0
                else:              
                    return output      

    for po in range(81):
        for i in range(area[po].len-1): 
            if area[po].fin==1:
                continue
            else:
                tempinput = input.copy()
                tempinput[po] = area[po].valarr[i]
                output = solve(tempinput)
                if output == 0:
                    continue               
                return output
        if area[po].fin==1:
            continue
        else:
            tempinput = input.copy()
            tempinput[po] = area[po].valarr[area[po].len-1]
            output = solve(tempinput)
            if output == 0:
                return 0
            else:              
                return output         

if __name__ == "__main__":
    input = [
    0,0,5,3,0,0,0,0,0,
    8,0,0,0,0,0,0,2,0,
    0,7,0,0,1,0,5,0,0,
    4,0,0,0,0,5,3,0,0,
    0,1,0,0,7,0,0,0,6,
    0,0,3,2,0,0,0,8,0,
    0,6,0,5,0,0,0,0,9,
    0,0,4,0,0,0,0,3,0,
    0,0,0,0,0,9,7,0,0]

    aws =  solve(input)
    if aws == 0:
        print("There is no answer")
    else:
        for y in range(9):
            for x in range(9):
                print(aws[9*y+x],end=' ')
            print("")
