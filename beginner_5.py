from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.beginner import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[5],0)

# your code starts here:

robotArm.moveRight()
while True:
    
    robotArm.grab()
    for x in range(8):
        robotArm.moveRight()
    robotArm.drop()
    for x in range(8):
        robotArm.moveLeft()
# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

