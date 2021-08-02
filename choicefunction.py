class ChoiceFunction:
    def __init__(self, function, parameters=[]):
        self.function = function
        self.parameters = parameters
        
    def run(self):
        self.function(*self.parameters)

if __name__ == "__main__":
    class Dedada():
        def dedoNaFulana(self, nome):
            print(f'{nome} levou uma dedada')

    hikari = Dedada()
    choicefunction = ChoiceFunction(hikari.dedoNaFulana, ['paola'])
    choicefunction.run()