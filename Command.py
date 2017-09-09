from TCPConnection import *
HJ_LIST = (
        'he1',
        'he2',
        'lae1',
        'lae2',
        'lae3',
        'lae4',
        'lle1',
        'lle2',
        'lle3',
        'lle4',
        'lle5',
        'lle6',
        'rle1',
        'rle2',
        'rle3',
        'rle4',
        'rle5',
        'rle6',
        'rae1',
        'rae2',
        'rae3',
        'rae4'
        )


class HingeJointEffector:
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate


class Command:
    def __init__(self):
        self.hjList = []

    def appendHJEffector(self, hjOrLoc, rate=None):
        hj = None
        if not isinstance(hjOrLoc, HingeJointEffector):
            hj = HingeJointEffector(HJ_LIST[hjOrLoc], rate)
        else:
            hj = hjOrLoc
            if hj.name not in HJ_LIST:
                raise Exception('Effector name not valid.')

        self.hjList.append(hj)

    def submit(self):
        msg = ""
        for hj in self.hjList:
            msg += '(' + hj.name + ' ' + str(hj.rate) + ')'

        print(msg)
        putMessage(msg)

