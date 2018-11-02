from Scripts.Behaviors.ComposedBehaviors.ComposedBehavior import ComposedBehavior
from Scripts.Behaviors.SimpleBehaviors.BlinkBehavior.BlinkBehaviorEaseInOut import BlinkBehaviorEaseInOut
from Scripts.Behaviors.SimpleBehaviors.MoveBehavior import *
from colour import Color
from Libs.Constants import *
import time


class AloofIdleBehavior(ComposedBehavior):
    def __init__(self, bodyRef):
        # standard behaviors
        ComposedBehavior.__init__(self, bodyRef)

        # generic variables
        self.behaviorType = ComposedBehaviors.ALOOF_IDLE
        self.behaviorList.append(BlinkBehaviorEaseInOut(bodyRef, [Color(rgb=(0.0, 0.0, 1.0))], ColorBrightness.LOW, 1, 12, Color(rgb=(0.0, 0.0, 0.0)), False))

    def applyBehavior(self):
        ComposedBehavior.applyBehavior(self)