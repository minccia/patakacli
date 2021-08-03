class ChoiceFunction:
    def __init__(self, function, parameters=[]):
        self.function = function
        self.parameters = parameters
        
    def run(self):
        self.function(*self.parameters)


