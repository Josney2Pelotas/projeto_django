from base.models import *


def QueryTeste(filtro):
    dados_query = []

    if 'tabela1__in' in filtro:
        if not filtro['tabela1__in']:
            del filtro['tabela1__in']

    query = Tabela2.objects.values_list('tabela1__coluna2', 'valor').filter(**filtro)

    for resultado in query:
        dados_query.append(resultado)

    return dados_query
