import sqlite3


def get_result(sql, param=""):
    """ Функция подключения к базе данных

    :param param:
    :param sql: параметры запроса в базу данных
    :return:  возвращает список словарей из базы данных соответствующих параметрам запроса
    """
    with sqlite3.connect("animal.db") as con:
        con.row_factory = sqlite3.Row
        result = []
        for item in con.execute(sql, param).fetchall():
            s = dict(item)

            result.append(s)
    return result

