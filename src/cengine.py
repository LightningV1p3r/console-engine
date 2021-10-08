#Copyright (c) 2021 LightningV1p3r

####################
#Libs
####################

####################
#Argument
####################

class Argument:

    def __init__(self, name, action) -> None:
        self.name = name
        self.action = action

    def __repr__(self) -> str:
        return f"{self.name}: trigger '{self.action}'"