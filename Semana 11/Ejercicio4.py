class Head:
    def __init__ (self, mouth, eyes, ears, nose):
        self.mouth = mouth
        self.eyes = eyes
        self.ears = ears
        self.nose = nose

class Torso:
    def __init__ (self, head, right_arm, left_arm, right_leg, left_leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg

class Arm:
    def __init__ (self, hand):
        self.hand = hand

class Hand:
    def __init__ (self, fingers):
        self.fingers = fingers

class Leg:
    def __init__ (self, feet):
        self.feet = feet

class Feet:
    def __init__ (self, fingers):
        self.fingers = fingers

class Human:
    def __init__ (self, torso):
        self.torso = torso

head = Head (1,2,2,1)
right_hand = Hand (5) 
left_hand = Hand (5)
right_feet = Feet (5)
left_feet = Feet (5)
right_arm = Arm (right_hand)
left_arm = Arm (left_hand)
right_leg = Leg (right_feet)
left_leg = Leg (left_feet)
torso = Torso (head, right_arm, left_arm, right_leg, left_leg)

human = Human (torso)

