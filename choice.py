from choicefunction import ChoiceFunction

class Choice:
    def __init__(self, trigger, title, choicefunction):
        self.trigger = trigger
        self.title = title
        self.choicefunction = choicefunction

    def run(self):
        self.choicefunction.run()

    def get_string(self):
        return f'[{self.trigger}] {self.title}'


if __name__ == '__main__':
    def dar_pao(nome):
        print(f'{nome} tome um pao')


    choicefunction = ChoiceFunction(dar_pao, ['hikari'])

    objeto = Choice(0, 'Dar pão para a hikari', choicefunction)
    print(objeto.get_string())
    objeto.run()