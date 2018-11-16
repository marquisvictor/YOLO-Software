from Scripts.Behavior.ComposedBehavior.ComposedBehavior import ComposedBehavior
from Scripts.Behavior.SimpleBehavior.BlinkBehavior.BlinkBehaviorEaseInOut import BlinkBehaviorEaseInOut
from Scripts.Behavior.SimpleBehavior.MoveBehavior.MoveBehaviorSpikes import MoveBehaviorSpikes
from colour import Color
from Libs.Constants import *
import time


class PunkAttentionCallBehavior(ComposedBehavior):
    def __init__(self, bodyRef):
        # standard behaviors
        ComposedBehavior.__init__(self, bodyRef)

        # generic variables
        self.behaviorType = ComposedBehaviorType.PUNK_ATTENTION_CALL

        self.behaviorList.append(BlinkBehaviorEaseInOut(bodyRef, [Color(rgb=(1.0, 0.0, 0.0))], ColorBrightness.HIGH, 1, 3.0, Color(rgb=(0.0, 0.0, 0.0)), False))
        self.behaviorList.append(MoveBehaviorSpikes(bodyRef, 90, MovementDirection.ALTERNATING, 2, 1.5, False))