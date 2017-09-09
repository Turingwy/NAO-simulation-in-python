from TCPConnection import *
from Command import *
init_command = "(scene rsg/agent/nao/nao_hetero.rsg 0)"

class Robot:

    def __init__(self):
        pass

    def init(self):
        connect()
        putMessage(init_command)
        msg = getMessage()
        print(msg)

    def simpleThink(self):
        for _ in range(80):
            putMessage("say ComeOn!")
            getMessage()
        self.sitdown()
        while True:
            self.swingNeck()

    def swingNeck(self):
        command = Command()
        command.appendHJEffector(HingeJointEffector("he1", 1))
        for _ in range(50):
            command.submit()
            getMessage()
        command = Command()
        command.appendHJEffector(HingeJointEffector("he1", -1))
        for _ in range(50):
            command.submit()
            getMessage()

    def sitdown(self):
        command = Command()
        command.appendHJEffector(HingeJointEffector("lae1", -1.5))
        command.appendHJEffector(HingeJointEffector("rae1", -1.5))
        command.appendHJEffector(HingeJointEffector("lae2", 0.9))
        command.appendHJEffector(HingeJointEffector("rae2", -0.9))
        command.appendHJEffector(HingeJointEffector("lae3", 0))
        command.appendHJEffector(HingeJointEffector("rae3", 0))
        command.appendHJEffector(HingeJointEffector("lae4", -0.8))
        command.appendHJEffector(HingeJointEffector("rae4", 0.8))
        command.appendHJEffector(HingeJointEffector("lle3", 1))
        command.appendHJEffector(HingeJointEffector("rle3", 1))
        command.appendHJEffector(HingeJointEffector("lle4", -2))
        command.appendHJEffector(HingeJointEffector("rle4", -2))
        command.appendHJEffector(HingeJointEffector("lle5", 1))
        command.appendHJEffector(HingeJointEffector("rle5", 1))
        command.appendHJEffector(HingeJointEffector("lle6", 0))
        command.appendHJEffector(HingeJointEffector("rle6", 0))
        for _ in range(40): 
            command.submit()
            getMessage()
        command = Command()
        command.appendHJEffector(HingeJointEffector("lae1", 0))
        command.appendHJEffector(HingeJointEffector("rae1", 0))
        command.appendHJEffector(HingeJointEffector("lae2", 0))
        command.appendHJEffector(HingeJointEffector("rae2", 0))
        command.appendHJEffector(HingeJointEffector("lae3", 0))
        command.appendHJEffector(HingeJointEffector("rae3", 0))
        command.appendHJEffector(HingeJointEffector("lae4", 0))
        command.appendHJEffector(HingeJointEffector("rae4", 0))
        command.appendHJEffector(HingeJointEffector("lle3", 0))
        command.appendHJEffector(HingeJointEffector("rle3", 0))
        command.appendHJEffector(HingeJointEffector("lle4", 0))
        command.appendHJEffector(HingeJointEffector("rle4", 0))
        command.appendHJEffector(HingeJointEffector("lle5", 0))
        command.appendHJEffector(HingeJointEffector("rle5", 0))
        command.appendHJEffector(HingeJointEffector("lle6", 0))
        command.appendHJEffector(HingeJointEffector("rle6", 0))
        command.submit()
