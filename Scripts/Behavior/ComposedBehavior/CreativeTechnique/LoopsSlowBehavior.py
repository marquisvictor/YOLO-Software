from colour import Color
from Libs.Constants import *
from Scripts.Behavior.ComposedBehavior.ComposedBehavior import ComposedBehavior
from Scripts.Behavior.SimpleBehavior.MoveBehavior.MoveBehaviorLoops import MoveBehaviorLoops
from Scripts.Behavior.SimpleBehavior.BlinkBehavior.BlinkBehaviorEaseInOut import BlinkBehaviorEaseInOut

class LoopsSlowBehavior(ComposedBehavior):
    def __init__(self, bodyRef):
        # standard behaviors
        ComposedBehavior.__init__(self, bodyRef)

        # generic variables
        self.behaviorType = ComposedBehaviorType.LOOPS_SLOW
        self.behaviorList.append(MoveBehaviorLoops(bodyRef, 30, MovementDirection.FORWARD, 2, 3.5, True))
        self.behaviorList.append(BlinkBehaviorEaseInOut(bodyRef, [bodyRef.getStimulusColor()], ColorBrightness.HIGH, 1, 7.0, Color(rgb=(0.0, 0.0, 0.0)), False))