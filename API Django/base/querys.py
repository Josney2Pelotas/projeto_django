from base.models import *


def queryvalores(filtro):
    dados_query = []

    if 'tabela1__in' in filtro:
        if not filtro['tabela1__in']:
            del filtro['tabela1__in']

    query = Tabela2.objects.values_list('tabela1__coluna2', 'valor').filter(**filtro)

    for resultado in query:
        dados_query.append(resultado)

    return dados_query


def query_id():
    query = Tabela1.objects.all()
    lista_query = [id_tabela.id for id_tabela in query]
    return lista_query
