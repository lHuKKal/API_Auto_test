import psycopg2

# Подключение к базе данных
connect_bd_postgresql_card_id_schema = psycopg2.connect(
    dbname="card_id_dev",
    user="dev_testing",
    password="dev_testing",
    host="172.16.10.135",
    port="5432",
    # Можно указать путь к таблице, если имеется дополнительная таблица с помощью Option
    options="-c search_path=public"

)


class PostgresqlConnect:

    @staticmethod
    def take_value_from_card_id_table():
        # Создание курсора
        cur = connect_bd_postgresql_card_id_schema.cursor()

        # Выполнение SQL-запроса
        cur.execute("SELECT * FROM clients_cards where payment_system = 'HUMO' and branch = '00394' and cbs_id = '63943152'")

        # Получение описания столбцов
        column_names = [desc[0] for desc in cur.description]
        print(column_names)

        # Извлечение результата запроса в переменную
        result = cur.fetchone()  # Извлечение только первой строки их БД
        # result2 = cur.fetchall()  # fetchall() для извлечения всех строк результата.
        cbs_id = result[1]  # выбрать значение cbs_id под 1 индексом
        card_numer = result[4]
        expiry_date = result[7]
        reversed_expire_date = expiry_date[:2] + expiry_date[2:]  # Сохраняем дату наоборот, иначе не проходит проверку
        print("Одна строка - " + str(result))
        # print("Все строки - " + str(result2))
        response = f"{cbs_id} {card_numer} {expiry_date}"  # Отобразить выбранные переменные в одну строку (только для проверки функции)
        print(response)

        # Закрытие курсора и соединения
        cur.close()
        connect_bd_postgresql_card_id_schema.close()

        return cbs_id, card_numer, reversed_expire_date  # Возвращаем все переменные
