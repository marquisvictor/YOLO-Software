from Scripts.Behavior.ComposedBehavior.ComposedBehavior import ComposedBehavior
from Scripts.Behavior.SimpleBehavior.MoveBehavior.MoveBehaviorRect import MoveBehaviorRect
from Libs.Constants import *
import time


class RectSlowBehavior(ComposedBehavior):
    def __init__(self, bodyRef):
        # standard behaviors
        ComposedBehavior.__init__(self, bodyRef)

        # generic variables
        self.behaviorType = ComposedBehaviorType.RECT_SLOW
        self.behaviorList.append(MoveBehaviorRect(bodyRef, 30, MovementDirection.FORWARD, 2, 3.5, True))