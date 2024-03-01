from goods.models import Products
from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline

def q_search(query):
    #поиск по id
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    #добавляем релевантность в векторный поиск
    #создаем вектор по полям поиска
    vector = SearchVector("name", "description")
    #преобразуем поисковый запрос в векторное представление
    query = SearchQuery(query)
    #возвращаем аннторированный queryset из обработанного методом SearchRank вектора и запроса с сортировки по наиболее подходящему варианту
    result = (Products.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank"))
    result = result.annotate(headline=SearchHeadline("name", query, start_sel='<span style="background-color: yellow;">', stop_sel="</span",))
    result = result.annotate(bodyline=SearchHeadline("description", query, start_sel='<span style="background-color: yellow;">', stop_sel="</span",))
    return result
    #векторный поиск django для postres в котором запрос поиска разбивается на токены и векторизируется и ищет по совпадениям
    #return Products.objects.annotate(search=SearchVector("name", "description")).filter(search=query)

#Вариант текстового поиска в sqlite3
    # #для полнотекстового поиска входные данные разбиваем на составляющие и формируем из них список из токенов запроса
    # keywords = [word for word in query.split() if len(word) > 2]
    # #создаем переменную как пустой Q объект для полнотекстового поиска
    # q_objects = Q()

    # for token in keywords:
    #     #знак |= означает или равно и добавит Q объект в коллекцию в суммарное выражение Q объектов
    #     q_objects |= Q(description__icontains=token)
    #     #добавляем поиск по иммени
    #     q_objects |= Q(name__icontains=token)
    #     #применяем фильтр из Q объектов на методе object для формирования SQL запроса
    # return Products.objects.filter(q_objects)