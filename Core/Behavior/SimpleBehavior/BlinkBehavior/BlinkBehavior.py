import time
import numpy
from colour import Color
from Core.Enumerations import *
from Core.Behavior.SimpleBehavior.SimpleBehavior import SimpleBehavior


class BlinkBehavior(SimpleBehavior, object):
    def __init__(self, controlRef, blinkColor, brightness, maxBehaviorRepetitions, duration, defaultColor):
        super(BlinkBehavior, self).__init__(controlRef, maxBehaviorRepetitions, duration)
        self.controlRef = controlRef
        self.controlColorAtStart = controlRef.getColor()
        self.controlBrightnessAtStart = controlRef.getBrightness()
        self.blinkColor = blinkColor
        self.brightness = brightness
        self.defaultColor = defaultColor
        

    def behaviorActions(self):
        #to be overriden
        super(BlinkBehavior, self).behaviorActions()
        

    def finishBehavior(self):
        super(BlinkBehavior, self).finishBehavior()
        self.controlRef.setColor(self.defaultColor)

    def checkForBehaviorEnd(self): 
        return time.time() - self.startTime > self.duration  
              
    def lerpColor(self, percentage, currentColor, newColor):
        rLerp = newColor.red * percentage + currentColor.red * (1 - percentage)
        gLerp = newColor.green * percentage + currentColor.green * (1 - percentage)
        bLerp = newColor.blue * percentage + currentColor.blue * (1 - percentage)

        #cleaning up any imprecision
        rLerp = numpy.clip(rLerp, 0, 1)
        gLerp = numpy.clip(gLerp, 0, 1)
        bLerp = numpy.clip(bLerp, 0, 1)

        lerpColor = Color(rgb=(rLerp, gLerp, bLerp))
        return lerpColor
