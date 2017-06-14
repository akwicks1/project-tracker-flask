"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    title, grade = hackbright.get_grades_by_github(github)

    html = render_template("student_info.html",
                            first=first,
                            last=last, 
                            github=github,
                            title=title,
                            grade=grade)

    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    html = render_template("student_search.html")

    return html

@app.route("/student-add")
def student_add():
    """Add a student."""


    return render_template("student_add.html")


@app.route("/added-student", methods=['POST'])
def added_student():
    """Successfully added student."""

    first = request.form.get('first')
    last = request.form.get('last')
    github = request.form.get('github')

    hackbright.make_new_student(first, last, github)


    html = render_template("successful_add.html",
                            first=first,
                            last=last,
                            github=github)


    return html





if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)

