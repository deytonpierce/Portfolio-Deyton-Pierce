from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class AboutPoint:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']

    # Class method to get all about points
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM about_point;"
        results = connectToMySQL('portfolio').query_db(query)

        about_points = []
        for point in results:
            about_points.append(cls(point))
        return about_points

    # Class method to save a new about point
    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO about_point (title, description) 
        VALUES (%(title)s, %(description)s);
        """
        return connectToMySQL('portfolio').query_db(query, data)

    # Class method to get a single about point by id
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM about_point WHERE id = %(id)s;"
        result = connectToMySQL('portfolio').query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    # Class method to update an about point by id
    @classmethod
    def update(cls, data):
        query = """
        UPDATE about_point 
        SET title = %(title)s, description = %(description)s 
        WHERE id = %(id)s;
        """
        return connectToMySQL('portfolio').query_db(query, data)

    # Class method to delete an about point by id
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM about_point WHERE id = %(id)s;"
        return connectToMySQL('portfolio').query_db(query, data)

    # Static method to validate about point data before saving or updating
    @staticmethod
    def validate_about_point(point):
        is_valid = True
        if len(point['title']) < 3:
            flash("Title must be at least 3 characters long.", "about_point")
            is_valid = False
        if len(point['description']) < 10:
            flash("Description must be at least 10 characters long.", "about_point")
            is_valid = False
        # Additional validation logic (if needed)
        return is_valid