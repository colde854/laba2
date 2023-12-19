

import wikipedia


# Извлечение резюме
def getSummary(name, sent):
    if sent:
        return wikipedia.summary(name, sentences=sent)
    else:
        return wikipedia.summary(name)

# Получение статьи как объекта
def getPage(name):
    return wikipedia.page(name)

# Получение названия статьи
def getTitle(name):
    return getPage(name).title

# Получение содержания статьи
def getContent(name):
    return getPage(name).content

# Получение ссылки на статью
def getUrl(name):
    return getPage(name).url


