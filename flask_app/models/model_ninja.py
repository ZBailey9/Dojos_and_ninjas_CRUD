from flask_app.config.mysqlconnection import connectToMySQL


DATABASE = 'dojos_ninjas'

class Ninja:
    def __init__(self, data: dict) -> None:
        self.id         = data['id']
        self.first_name = data['first_name']
        self.last_name  = data['last_name']
        self.age        = data['age']
        self.created_at = data['updated_at']
        self.updated_at = data['updated_at']
        self.dojo_id    = data['dojo_id']

    @classmethod
    def get_all_ninjas(cls) -> list:
        query = 'SELECT * FROM ninjas;'
        results = connectToMySQL(DATABASE).query_db(query)
        all_ninjas = []
        for row in results:
            all_ninjas.append(cls(row))
        return all_ninjas


    @classmethod
    def create_ninja(cls, data: list[dict]) -> int:
        query = 'INSERT INTO ninjas (first_name, last_name, age, dojo_id) \
            VALUES(%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);'
        new_ninja_id = connectToMySQL(DATABASE).query_db(query, data)
        return new_ninja_id

    @classmethod
    def update_ninja(cls, data: list[dict]) -> None:
        query = 'UPDATE ninjas \
            SET first_name = %(first_name)s,\
            last_name = %(last_name)s, \
            age = %(age)s \
            WHERE id = %(id)s'
        connectToMySQL(DATABASE).query_db(query, data)
        return None
    
    @classmethod
    def delete_ninja(cls, id: str) -> None:
        data = { 'id': int(id) }
        query = 'DELETE FROM ninjas \
            WHERE id = %(id)s'
        connectToMySQL(DATABASE).query_db(query, data)
        return None