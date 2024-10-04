from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Info:
    def __init__(self, data):
        self.id = data['id']
        self.bio = data['bio']
        self.recent_projects_description = data['recent_projects_description']
        self.email = data['email']
        self.phone = data['phone']
        self.contact_description = data['contact_description']
        self.all_rights_reserved = data['all_rights_reserved']
        self.profile_pic = data['profile_pic']
        self.web_pic = data['web_pic']

    # Class method to get all info
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM info;"
        results = connectToMySQL('portfolio').query_db(query)

        info_list = []
        for info in results:
            info_list.append(cls(info))
        return info_list

    # Class method to get a single info by id
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM info WHERE id = %(id)s;"
        result = connectToMySQL('portfolio').query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    # Class method to save new info
    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO info (bio, recent_projects_description, email, phone, contact_description, all_rights_reserved, profile_pic, web_pic) 
        VALUES (%(bio)s, %(recent_projects_description)s, %(email)s, %(phone)s, %(contact_description)s, %(all_rights_reserved)s, %(profile_pic)s, %(web_pic)s);
        """
        return connectToMySQL('portfolio').query_db(query, data)

    # Class method to update info by id
    @classmethod
    def update(cls, data):
        query = """
        UPDATE info 
        SET bio = %(bio)s, recent_projects_description = %(recent_projects_description)s, email = %(email)s, 
            phone = %(phone)s, contact_description = %(contact_description)s, all_rights_reserved = %(all_rights_reserved)s, 
            profile_pic = %(profile_pic)s, web_pic = %(web_pic)s
        WHERE id = %(id)s;
        """
        return connectToMySQL('portfolio').query_db(query, data)

    # Class method to delete info by id
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM info WHERE id = %(id)s;"
        return connectToMySQL('portfolio').query_db(query, data)

    # Static method to validate info data before saving or updating
    @staticmethod
    def validate_info(info):
        is_valid = True
        if len(info['bio']) < 10:
            flash("Bio must be at least 10 characters long.", "info")
            is_valid = False
        if len(info['email']) < 5:
            flash("Email must be valid.", "info")
            is_valid = False
        if len(info['phone']) < 10:
            flash("Phone number must be valid.", "info")
            is_valid = False
        if len(info['contact_description']) < 10:
            flash("Contact description must be at least 10 characters long.", "info")
            is_valid = False
        # Additional validation logic (if needed)
        return is_valid