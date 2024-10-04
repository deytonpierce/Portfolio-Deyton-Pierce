from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class WhatIDo:
    def __init__(self, data):
        self.id = data['id']
        self.order_by = data['order_by']
        self.icon = data['icon']
        self.title = data['title']
        self.description = data['description']

    # Class method to get all "What I Do" entries
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM what_i_do ORDER BY order_by;"
        results = connectToMySQL('portfolio').query_db(query)

        what_i_do_entries = []
        for entry in results:
            what_i_do_entries.append(cls(entry))
        return what_i_do_entries

    # Class method to save a new entry
    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO what_i_do (order_by, icon, title, description) 
        VALUES (%(order_by)s, %(icon)s, %(title)s, %(description)s);
        """
        return connectToMySQL('portfolio').query_db(query, data)

    # Class method to get a single entry by id
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM what_i_do WHERE id = %(id)s;"
        result = connectToMySQL('portfolio').query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    # Class method to update an entry by id
    @classmethod
    def update(cls, data):
        query = """
        UPDATE what_i_do 
        SET order_by = %(order_by)s, icon = %(icon)s, title = %(title)s, description = %(description)s 
        WHERE id = %(id)s;
        """
        return connectToMySQL('portfolio').query_db(query, data)

    # Class method to delete an entry by id
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM what_i_do WHERE id = %(id)s;"
        return connectToMySQL('portfolio').query_db(query, data)

    # Static method to validate "What I Do" data before saving or updating
    @staticmethod
    def validate_entry(entry):
        is_valid = True
        if len(entry['order_by']) < 1:
            flash("Order By field cannot be empty.", "what_i_do")
            is_valid = False
        if len(entry['icon']) < 3:
            flash("Icon must be at least 3 characters long.", "what_i_do")
            is_valid = False
        if len(entry['title']) < 3:
            flash("Title must be at least 3 characters long.", "what_i_do")
            is_valid = False
        if len(entry['description']) < 10:
            flash("Description must be at least 10 characters long.", "what_i_do")
            is_valid = False
        return is_valid