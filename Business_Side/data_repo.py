import sqlite3


class DataRepo:

    def __init__(self, filename):
        self.connection = sqlite3.connect(filename)

    def clear_database(self):
        self.connection.execute('''drop table if exists winemag''')

    def is_database_empty(self):
        return not bool(self.connection.execute("SELECT count(*) FROM (select 0 from winemag limit 1);").fetchone()[0])

    def create_database(self):
        self.connection.execute('''CREATE TABLE IF NOT EXISTS winemag
                 (points INT,
                 title           CHAR(50),
                 description     TEXT,
                 taster_name     CHAR(20),
                 taster_twitter_handle CHAR(20),
                 price INT,
                 designation CHAR(50),
                 variety CHAR(20),
                 region_1 CHAR(20),
                 region_2 CHAR(20),
                 province CHAR(20),
                 country CHAR(20),
                 winery CHAR(20));''')

    def get_data_from_database(self, criteria={'points', 'title'}):
        variables_string = ','.join(criteria)
        cursor = self.connection.execute(f"SELECT {variables_string} from winemag")
        rows = []
        for row in cursor:
            rows.append(row)
        return rows

    def insert_data(self, json_data, criteria):
        variables_string = ','.join(criteria)
        insert_query = f"INSERT INTO winemag ({variables_string}) \
            VALUES ({', '.join('?' for i in range(len(criteria)))})"
        for row in json_data:
            values = [row[criterium] for criterium in criteria]
            self.connection.execute(insert_query, values)

    def avg_price(self):
        return self.connection.execute('''SELECT avg(price) from winemag''').fetchone()[0]

    def avg_points(self):
        return self.connection.execute('''SELECT avg(points) from winemag''').fetchone()[0]

    def table_exists(self):
        return bool(self.connection.execute('SELECT EXISTS(SELECT 1 FROM sqlite_master '
                                            'WHERE type="table" AND name="winemag")').fetchone()[0])

    def get_list_of_countries(self):
        cursor = self.connection.execute('''SELECT country from winemag''')
        countries_list = []
        for country in cursor:
            countries_list.append(country[0])
        return countries_list

    def get_counts_by_country(self, data):
        counts_by_country = {}
        for country in data:
            if country not in counts_by_country.keys():
                counts_by_country[country] = 1
            else:
                counts_by_country[country] = counts_by_country[country] + 1
        return counts_by_country
