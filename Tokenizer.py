from Token import Token

class HingeJointPerceptor:
    def __init__(self, name=None, ax = 0):
        self.name = name
        self.ax = ax

    def fillForm(self, tokenStream):
        next(tokenStream)
        self.name = next(tokenStream).value
        next(tokenStream)
        self.ax = next(tokenStream).value
        return True

class ForcePerceptor:
    def __init__(self, name=None, center=None, force=None):
        self.name = name
        self.center = center
        self.force = force

    def fillForm(self, tokenStream):
        next(tokenStream)
        self.name = next(tokenStream).value
        next(tokenStream)
        self.center = []
        for _ in range(3):
            self.center.append(next(tokenStream).value)

        next(tokenStream)
        self.force = []
        for _ in range(3):
            self.force.append(next(tokenStream).value)

class ACCPerceptor:
    def __init__(self, name=None, a=None):
        self.name = name
        self.a = a

    def fillForm(self, tokenStream):
        next(tokenStream)
        self.name = next(tokenStream).value
        next(tokenStream)
        self.a = []
        for _ in range(3):
            self.a.append(next(tokenStream).value)

def splitMessage2Token(msg):
    msgList = msg.split()
    msgList2 = []
    for s in msgList:
        msgList2[len(msgList2):len(msgList2)] = s.split('(')
    msgList3 = []
    for s in msgList2:
        msgList3[len(msgList3):len(msgList3)] = s.split(')')
    msgList3 = [s for s in msgList3 if s != '']
    return [Token(s) for s in msgList3] 
    

def fillPerceptor(tokenList):
    tokenStream = iter(tokenList)
    token = next(tokenStream)
    HJList, ACCList, forceList = [], [], []
    try:
        while True:
            if token.type == 0:
                HJ = HingeJointPerceptor()
                HJ.fillForm(tokenStream)
                HJList.append(HJ)
            elif token.type == 1:
                ACC = ACCPerceptor(tokenStream)
                ACC.fillForm(tokenStream)
                ACCList.append(ACC)
            elif token.type == 2:
                force = ForcePerceptor(tokenStream)
                force.fillForm(tokenStream)
                forceList.append(force)

            token = next(tokenStream)
    except:
        pass
    return HJList, ACCList, forceList

# msg = '(time (now 5887.28))(GS (sl 0) (sr 0) (t 0.00) (pm BeforeKickOff))(GYR (n torso) (rt -42.04 -0.00 -0.00))(ACC (n torso) (a 0.00 -1.34 2.83))(HJ (n hj1) (ax -0.00))(HJ (n hj2) (ax 0.00))(HJ (n raj1) (ax -104.84))(HJ (n raj2) (ax -62.91))(HJ (n raj3) (ax 0.00))(HJ (n raj4) (ax 55.92))(HJ (n laj1) (ax -104.84))(HJ (n laj2) (ax 62.91))(HJ (n laj3) (ax -0.00))(HJ (n laj4) (ax -55.92))(HJ (n rlj1) (ax -0.00))(HJ (n rlj2) (ax -0.00))(HJ (n rlj3) (ax 69.90))(HJ (n rlj4) (ax -130.63))(HJ (n rlj5) (ax 69.90))(FRP (n rf) (c -0.00 -0.08 -0.01) (f -0.00 6.47 26.02))(HJ (n rlj6) (ax 0.00))(HJ (n llj1) (ax -0.00))(HJ (n llj2) (ax 0.00))(HJ (n llj3) (ax 69.90))(HJ (n llj4) (ax -130.63))(HJ (n llj5) (ax 69.90))(FRP (n lf) (c 0.00 -0.08 -0.01) (f 0.00 6.47 26.02))(HJ (n llj6) (ax -0.00))'
# a, b, c = fillPerceptor(splitMessage2Token(msg))

# for cc in a:
#     print(cc.ax)



