import sys
import time
import numpy

from colour import Color
import pytweening as tween

from Libs.Constants import *
from Scripts.Behavior.SimpleBehavior.MoveBehavior.MoveBehavior import MoveBehavior


class MoveBehaviorStraight(MoveBehavior):
    # Body body, int repetitions, float duration
    def __init__(self, bodyRef, movementSpeed, movementDirection, transition, repetitions, duration, keepBehaviorSetting=False, startDelay = 0.0):
        MoveBehavior.__init__(self, bodyRef, movementSpeed, movementDirection, transition, repetitions, duration, keepBehaviorSetting, startDelay)
        self.movementType = ShapeType.STRAIGHT
    	self.waypoints = numpy.array([[1, 0]])
    	# Note: to do a path backwards we invert the points and their order
        if self.currentMovementDirection == MovementDirection.REVERSE:
            self.waypoints = reversePath(self, self.waypoints)
        return
    
    # Body body
    def applyBehavior(self):
        MoveBehavior.applyBehavior(self)
        self.followPath(len(waypoints), self.currentMovementWaypoint)
        return