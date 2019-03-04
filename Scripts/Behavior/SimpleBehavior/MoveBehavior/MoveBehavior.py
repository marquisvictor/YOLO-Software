import sys
import time

import numpy

from Libs.Constants import *
from Scripts.Behavior.SimpleBehavior.SimpleBehavior import SimpleBehavior


class MoveBehavior(SimpleBehavior, object):
    def __init__(self, bodyRef, movementSpeed, movementDirection, maxBehaviorRepetitions, duration):
        super(MoveBehavior, self).__init__(bodyRef, maxBehaviorRepetitions, duration)
        self.waypoints = numpy.array([])
        self.movementSpeed = 0
        self.animationIntervalTime = duration
        self.movementType = ShapeType.NONE
        self.initialMovementDirection = movementDirection

        if self.initialMovementDirection == MovementDirection.ALTERNATING:
            self.currentMovementDirection = MovementDirection.FORWARD
        else:
            self.currentMovementDirection = self.initialMovementDirection
            
        self.movementSpeed = numpy.clip(movementSpeed, 0, 90)
        self.initBehavior()


    def initBehavior(self):
        super(MoveBehavior, self).initBehavior()
        self.alreadyStartedSegment = False
        self.currentWaypointIndex = 0
        

    def behaviorActions(self):
        pass

    def finishBehavior(self):
        super(MoveBehavior, self).finishBehavior()
        self.bodyRef.resetWheelSetup()

    def reversePath(self, path):
        inversedPath = [-x for x in path]
        reversedPath = list(reversed(inversedPath))
        return reversedPath

    def followPath(self, pathLength, nextWaypoint):
        if not self.alreadyStartedSegment:
            self.alreadyStartedSegment = True
            self.bodyRef.setWheelMovement(nextWaypoint, self.movementSpeed)

        if self.reachedNewWaypoint(pathLength):
            self.currentWaypointIndex += 1
            self.alreadyStartedSegment = False

        if self.checkForBehaviorEnd(pathLength): 
            if self.maxBehaviorRepetitions!=0:
                if self.currentBehaviorRepetition == self.maxBehaviorRepetitions:
                    self.finishBehavior()
                    return

                if self.currentBehaviorRepetition > self.maxBehaviorRepetitions:
                    return

                self.currentBehaviorRepetition += 1

            # if this movement is alternating then change it after each repetition
            if self.initialMovementDirection == MovementDirection.ALTERNATING:
                if self.currentMovementDirection == MovementDirection.FORWARD:
                    self.currentMovementDirection = MovementDirection.REVERSE
                else:
                    self.currentMovementDirection = MovementDirection.FORWARD
        
            self.startTime = time.time()
            self.currentWaypointIndex = 0
            self.alreadyStartedSegment = False
        

    def reachedNewWaypoint(self, pathLength):
        timePerWaypoint = float(self.animationIntervalTime) / (pathLength)
        return time.time() - self.startTime >= timePerWaypoint * (self.currentWaypointIndex + 1) and self.currentWaypointIndex < (pathLength)
  
    def checkForBehaviorEnd(self, pathLength):
        return self.currentWaypointIndex > (pathLength - 1)