import psycopg2

class PostgresqlConnect:

    @staticmethod
    def Take_Value_From_Card_Id_Table():

        # Подключение к базе данных
        connect_bd_postgresql = psycopg2.connect(
            dbname="card_id_dev",
            user="dev_testing",
            password="dev_testing",
            host="172.16.10.135",
            port="5432",
            options="-c search_path=public"  # Можно указать путь к таблице, если имеется дополнительная таблица с помощью Option
        )

        # Создание курсора
        cur = connect_bd_postgresql.cursor()

        # Выполнение SQL-запроса
        cur.execute("SELECT * FROM clients_cards where payment_system = 'HUMO' and branch = '00394'")

        # Получение описания столбцов
        column_names = [desc[0] for desc in cur.description]
        print(column_names)

        # Извлечение результата запроса в переменную
        result = cur.fetchone()
        cbs_id = result[1]  # выбрать значение cbs_id под 1 индексом
        card_numer = result[4]
        expiry_date = result[7]
        print(result)
        response = f"{cbs_id} {card_numer} {expiry_date}"  # Отобразить выбранные переменные в одну строку (только для проверки функции)
        print(response)

        # Закрытие курсора и соединения
        cur.close()
        connect_bd_postgresql.close()

        return cbs_id, card_numer, expiry_date  # Возвращаем все переменные
