from choicefunction import ChoiceFunction

def dedoNaFulana(nome):
    print(f'{nome} levou uma dedada')

objeto = ChoiceFunction(dedoNaFulana(), 'Hikari')

print(objeto)