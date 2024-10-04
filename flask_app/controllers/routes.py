# Main Import
from flask_app import app
from flask import render_template, session
from flask_app.models.info import Info
from flask_app.models.project import Project
from flask_app.models.about_point import AboutPoint  # Import AboutPoint model
from flask_app.models.certifications import Certification  # Import Certification model
from flask_app.models.connect import Connect  # Import Connect model
from flask_app.models.what_i_do import WhatIDo  # Import WhatIDo model

# Home page
@app.route('/')
def home():
    # Fetch all info data (assuming you have a single info record)
    info = Info.get_by_id({'id': 1})  # Assuming the info record has ID = 1
    
    # Fetch all About Points
    about_points = AboutPoint.get_all()

    # Fetch all Certifications
    certifications = Certification.get_all()

    # Fetch all Connect entries
    connections = Connect.get_all()

    # Fetch all What I Do entries
    what_i_do_entries = WhatIDo.get_all()

    # Fetch all projects
    projects = Project.get_all()  # Get all projects

    # If info is not found, handle the error (optional)
    if not info:
        return render_template('404.html', info=info)

    # Render the home page with the info and other data
    return render_template('index.html', info=info, about_points=about_points, certifications=certifications, connections=connections, what_i_do_entries=what_i_do_entries, projects=projects)

# Specific project page
@app.route('/portfolio/<port_id>')
def show_portfolio(port_id):
    # Fetch project by id
    project = Project.get_by_id({'id': port_id})

    project_count = Project.count_projects()  # Get number of projects

    # Fetch all info data (assuming you have a single info record)
    info = Info.get_by_id({'id': 1})

    # Fetch all About Points
    about_points = AboutPoint.get_all()

    # Fetch all Certifications
    certifications = Certification.get_all()

    # Fetch all Connect entries
    connections = Connect.get_all()

    # Fetch all What I Do entries
    what_i_do_entries = WhatIDo.get_all()

    # Store the portfolio id in session if necessary
    session['port_id'] = port_id

    project_id = int(port_id)
    has_next_project = project_id < project_count
        
    # If project is not found, handle the error (optional)
    if not project:
        return render_template('404.html', info=info)
    
    # Render the portfolio page with the project data and other data
    return render_template('portfolio-single.html', project=project, has_next_project=has_next_project, info=info, about_points=about_points, certifications=certifications, connections=connections, what_i_do_entries=what_i_do_entries)