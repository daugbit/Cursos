def notas(* nota, sit=False):
    """
    -> Função para analisar notas e retornar a situação geral da turma.
    :param nota: notas dos alunos
    :param sit: retorna uma situação conforme a média da turma
    :return: dicionário com a quantidade de notas, a maior nota, a menor nota, a média e a situação
    """
    r = {}
    r['quantidade'] = len(nota)
    r['maior'] = max(nota)
    r['menor'] = min(nota)
    r['média'] = sum(nota) / len(nota)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


print(notas(3.0, 10, 8.4, 6, sit=True))
print(help(notas))
