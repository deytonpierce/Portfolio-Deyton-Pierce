from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Connect:
    def __init__(self, data):
        self.id = data['id']
        self.icon = data['icon']
        self.link = data['link']

    # Class method to get all connections
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM connect;"
        results = connectToMySQL('portfolio').query_db(query)

        connections = []
        for conn in results:
            connections.append(cls(conn))
        return connections

    # Class method to save a new connection
    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO connect (icon, link) 
        VALUES (%(icon)s, %(link)s);
        """
        return connectToMySQL('portfolio').query_db(query, data)

    # Class method to get a single connection by id
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM connect WHERE id = %(id)s;"
        result = connectToMySQL('portfolio').query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    # Class method to update a connection by id
    @classmethod
    def update(cls, data):
        query = """
        UPDATE connect 
        SET icon = %(icon)s, link = %(link)s 
        WHERE id = %(id)s;
        """
        return connectToMySQL('portfolio').query_db(query, data)

    # Class method to delete a connection by id
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM connect WHERE id = %(id)s;"
        return connectToMySQL('portfolio').query_db(query, data)

    # Static method to validate connection data before saving or updating
    @staticmethod
    def validate_connection(connection):
        is_valid = True
        if len(connection['icon']) < 3:
            flash("Icon must be at least 3 characters long.", "connect")
            is_valid = False
        if connection['link'] and len(connection['link']) < 5:
            flash("Link must be at least 5 characters long if provided.", "connect")
            is_valid = False
        return is_valid