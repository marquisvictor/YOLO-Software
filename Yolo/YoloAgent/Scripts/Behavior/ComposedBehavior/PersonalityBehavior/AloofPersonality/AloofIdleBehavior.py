from Scripts.Behavior.ComposedBehavior.ComposedBehavior import ComposedBehavior
from Scripts.Behavior.SimpleBehavior.BlinkBehavior.BlinkBehaviorEaseInOut import BlinkBehaviorEaseInOut
from colour import Color
from Libs.Constants import *
import time


class AloofIdleBehavior(ComposedBehavior):
    def __init__(self, bodyRef):
        # standard behaviors
        ComposedBehavior.__init__(self, bodyRef)

        # generic variables
        self.behaviorType = ComposedBehaviorType.ALOOF_IDLE
        self.behaviorList.append(BlinkBehaviorEaseInOut(bodyRef, [Color(rgb=(0.0, 1.0, 0.0))], ColorBrightness.LOW, 0, 7.0, bodyRef.getColor(), False))