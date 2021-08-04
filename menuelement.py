from .choicefunction import ChoiceFunction
from .choice import Choice

class MenuElement:
    def __init__(self, title):
        self.title = title
        self.choices = []

    def display(self):
        print(self.title)
        print('')
        
        for choice in self.choices:
            print(choice.get_string())

    def get_response(self):
        chosen_option = input('Qual é a opção escolhida? \n\nDigite aqui: ')
        return chosen_option
        
    def run(self):
        self.display()
        response = self.get_response()

        for choice in self.choices:
            if choice.trigger == response:
                choice.run()
                return

        print('Invalid, please try an accepted option.')
        self.run()

    def add_choice(self, title, function, parameters=[], trigger=None):
        if not trigger:
            trigger = str(len(self.choices)+1)

        choicefunction = ChoiceFunction(function, parameters)
        choice = Choice(trigger, title, choicefunction)
        self.choices.append(choice)

# Testing the program
if __name__ == '__main__':

    def dar_pao(nome):
        print(f'{nome} tome pao')
    
    def comer_pao(nome):
        print(f'desculpa {nome} mas eu comi seu pao')

    menu = MenuElement('Escolha uma opção:')
    menu.add_choice(dar_pao, ['hikari'], 'Dar pão')
    #menu.add_choice(comer_pao, ['hikari'], 'Comer pão')
    #menu.add_choice(comer_pao, ['luisa'], 'Comer pão da luísa')
    menu.run()