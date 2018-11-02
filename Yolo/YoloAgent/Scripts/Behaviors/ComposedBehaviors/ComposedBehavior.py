from ..SimpleBehaviors.BlinkBehavior import *
from ..SimpleBehaviors.FeelerBehavior import *
from ..SimpleBehaviors.MoveBehavior import *
from Libs.Constants import *
import time


class ComposedBehavior:
    def __init__(self):
        # standard behaviors
        self.behaviorList = []
        self.behaviorList.append(BlinkBehavior())
        #self.behaviorList.append(FeelerBehavior())
        self.behaviorList.append(MoveBehavior())

        # generic variables
        self._behaviorDuration = 0.0
        self._startTime = 0.0
        self.isOver = True
        self.behaviorHalted = False
        self.behaviorType = ComposedBehaviors.BASE

        return

    def startBehavior(self):
        self._startTime = time.time()
        self.isOver = False


        for behavior in self.behaviorList:
            behavior.startBehavior()

        print("Starting " + self.behaviorType.name)

        return

    def applyBehavior(self, agentBody):
        self.isOver = True
        behaviorsToApply = []

        #print ("Applying " + str(self.behaviorType))
        behaviorsToApply = self.behaviorList

        for behavior in behaviorsToApply:
            if not behavior.isOver:
                behavior.applyBehavior(agentBody)

            if self.isOver and not behavior.isOver:
                self.isOver = False

        #if self.isOver : print("Composed behavior is over")

        return

    def prepareBehavior(self, body):
        raise NotImplementedError("Please Implement and Use Inheriting Class' Method")

    def updateStartTimeAfterHalt(self, totalTimeDelay):

        for behavior in self.behaviorList:
            behavior.updateStartTimeAfterHalt(totalTimeDelay)

        return

    def haltAndFinishBehavior(self, body):

        for behavior in self.behaviorList:
            behavior.finalizeEffects(body)

        return