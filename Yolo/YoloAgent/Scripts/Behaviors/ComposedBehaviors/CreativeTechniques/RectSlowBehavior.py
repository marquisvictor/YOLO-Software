from Scripts.Behaviors.ComposedBehaviors.ComposedBehavior import ComposedBehavior
from Scripts.Behaviors.SimpleBehaviors.MoveBehavior import *
from Libs.Constants import *
import time


class RectSlowBehavior(ComposedBehavior):
    def __init__(self, bodyRef):
        # standard behaviors
        ComposedBehavior.__init__(self, bodyRef)

        # generic variables
        self.behaviorType = ComposedBehaviors.RECT_SLOW
        self.behaviorList.append(MoveBehavior(bodyRef, Shapes.RECT, 45, MovementDirection.STANDARD, Transitions.LINEAR, 1, 10, True))

    def applyBehavior(self):
        ComposedBehavior.applyBehavior(self)