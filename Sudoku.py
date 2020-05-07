# 한칸에 대한 정보 담는 Class
class point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.len = 9
        self.fin = 0
        self.valarr=list(range(1,10))
    # '가능한 값 리스트' 에서 값을 빼는 매서드    
    def delval(self, val):
        if self.fin == 0:
            try:
                self.valarr.remove(val)
                self.len -= 1
            except:
                pass
    # 이미 완성된칸은 건들지 않게 해준다.
    def setval(self, val):
        self.fin=1
        self.len=1
        self.valarr = [val]

#어떤 값이 있는 칸의 값을 그 칸에 대해 같은 가로줄, 세로줄, 3*3상자에 있는 칸들의 '가능한 값 리스트'에서 제거해줌
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

#재귀 이용
def solve(input):
    #이미 답이 나오면 빠져나온다
    if 0 not in input:
        return input

    # 각 칸에 대한 point class 를 생성     
    area = []
    for y in range(9):
        for x in range(9):
            area.append(point(x,y))

    # 각 칸의 '가능한 값 리스트'를 만든다
    for y in range(9):
        for x in range(9):
            val=input[9*y+x]
            if val == 0:
                continue

            area[9*y+x].setval(val)
            removenum(x,y,val,area)

    # 만약 어떤 값도 들어올 수 없는 칸이 있다면 이 input상황에서의 답은 없다 
    for po in range(81):
        if area[po].len == 0:
            return 0

    # 한가지의 값만 가능한 칸이 있다면 모두 입력한다(속도를 위해)
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

    # 한가지 이상의 값이 가능한 칸들을 한 값씩 대입하고 그 상황을 재귀로 solve함수에 넣어준다
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

        #어떤 칸에 대해 가능한 값들을 넣어보다가 어떤 값도 안되는 칸이 있다면 이 input상황에서의 답은 없다        
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

# 기본적 테스트를 위한 고정된 input 값을 가진 코드
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
