from .choicefunction import ChoiceFunction

# Testing
def dedoNaFulana(nome):
    print(f'{nome} levou uma dedada')

objeto = ChoiceFunction(dedoNaFulana(), 'Hikari')

print(objeto)