from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Project:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.preview_description = data['preview_description']
        self.description = data['description']
        self.languages = data['languages']
        self.deployment = data['deployment']
        self.sourcecode = data['sourcecode']
        self.sourcecode_link = data['sourcecode_link']  # Updated field
        self.website = data['website']                    # Updated field
        self.website_link = data['website_link']          # Updated field
        self.prev_pic = data['prev_pic']
        self.main_pic = data['main_pic']

    # Class method to get all projects
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM projects;"
        results = connectToMySQL('portfolio').query_db(query)

        projects = []
        for project in results:
            projects.append(cls(project))
        return projects

    # Class method to save a new project
    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO projects (name, preview_description, description, languages, deployment, sourcecode, sourcecode_link, website, website_link, prev_pic, main_pic) 
        VALUES (%(name)s, %(preview_description)s, %(description)s, %(languages)s, %(deployment)s, %(sourcecode)s, %(sourcecode_link)s, %(website)s, %(website_link)s, %(prev_pic)s, %(main_pic)s);
        """
        return connectToMySQL('portfolio').query_db(query, data)

    # Class method to get a single project by id
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM projects WHERE id = %(id)s;"
        result = connectToMySQL('portfolio').query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    # Class method to update a project by id
    @classmethod
    def update(cls, data):
        query = """
        UPDATE projects 
        SET name = %(name)s, preview_description = %(preview_description)s, description = %(description)s, languages = %(languages)s, 
            deployment = %(deployment)s, sourcecode = %(sourcecode)s, sourcecode_link = %(sourcecode_link)s, website = %(website)s, 
            website_link = %(website_link)s, prev_pic = %(prev_pic)s, main_pic = %(main_pic)s
        WHERE id = %(id)s;
        """
        return connectToMySQL('portfolio').query_db(query, data)

    # Class method to delete a project by id
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM projects WHERE id = %(id)s;"
        return connectToMySQL('portfolio').query_db(query, data)

    # Static method to validate project data before saving or updating
    @staticmethod
    def validate_project(project):
        is_valid = True
        if len(project['name']) < 3:
            flash("Project name must be at least 3 characters long.", "project")
            is_valid = False
        if len(project['description']) < 10:
            flash("Description must be at least 10 characters long.", "project")
            is_valid = False
        if len(project['preview_description']) < 5:
            flash("Preview description must be at least 5 characters long.", "project")
            is_valid = False
        # Additional validation logic (if needed)
        return is_valid
    # Class method to count the number of projects
    
    @classmethod
    def count_projects(cls):
        query = "SELECT COUNT(*) as project_count FROM projects;"
        result = connectToMySQL('portfolio').query_db(query)
        if result:
            return result[0]['project_count']
        return 0