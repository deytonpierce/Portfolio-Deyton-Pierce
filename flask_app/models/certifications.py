from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Certification:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.year = data['year']
        self.pic = data['pic']

    # Class method to get all certifications
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM certifications;"
        results = connectToMySQL('portfolio').query_db(query)

        certifications = []
        for cert in results:
            certifications.append(cls(cert))
        return certifications

    # Class method to save a new certification
    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO certifications (title, description, year, pic) 
        VALUES (%(title)s, %(description)s, %(year)s, %(pic)s);
        """
        return connectToMySQL('portfolio').query_db(query, data)

    # Class method to get a single certification by id
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM certifications WHERE id = %(id)s;"
        result = connectToMySQL('portfolio').query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    # Class method to update a certification by id
    @classmethod
    def update(cls, data):
        query = """
        UPDATE certifications 
        SET title = %(title)s, description = %(description)s, year = %(year)s, pic = %(pic)s 
        WHERE id = %(id)s;
        """
        return connectToMySQL('portfolio').query_db(query, data)

    # Class method to delete a certification by id
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM certifications WHERE id = %(id)s;"
        return connectToMySQL('portfolio').query_db(query, data)

    # Static method to validate certification data before saving or updating
    @staticmethod
    def validate_certification(certification):
        is_valid = True
        if len(certification['title']) < 3:
            flash("Title must be at least 3 characters long.", "certification")
            is_valid = False
        if len(certification['description']) < 10:
            flash("Description must be at least 10 characters long.", "certification")
            is_valid = False
        if len(certification['year']) < 4 or not certification['year'].isdigit():
            flash("Year must be a valid year (e.g., 2020).", "certification")
            is_valid = False
        if len(certification['pic']) < 5:
            flash("Picture URL must be at least 5 characters long.", "certification")
            is_valid = False
        return is_valid