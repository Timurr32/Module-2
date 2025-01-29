from RobotArm import *

# Import the challenges (in this case challenges/example.py)
from challenges.basic import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[5],0)

# your code starts here:
robotArm.moveRight()
scan = robotArm.scan()
robotArm.grab()
if robotArm.scan() == "red":
    robotArm.moveLeft()
    robotArm.drop()
elif robotArm.scan() == "yellow":
    robotArm.moveRight()
    robotArm.drop()

# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

