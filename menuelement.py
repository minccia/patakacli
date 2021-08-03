class MenuElement:
    def __init__(self, title):
        self.title = title

    def display(self):
        print(self.title)

    def get_response(self):
        chosen_option = input('Qual é a opção escolhida? \nDigite aqui: ')
        return chosen_option

    def run(self):
        self.display()
        objeto.get_response()

# Testing the class
if __name__ == '__main__':
    objeto = MenuElement('Você tem uma língua e pode fazer plu, plu plé, plu, plu, plé')
    objeto.run()
