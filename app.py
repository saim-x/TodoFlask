from flask import Flask, redirect, render_template, request

app = Flask(__name__)

tasks = []
projects = ["Project A", "Project B", "Project C"]

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add_task", methods=["POST"])
def add_task():
    new_task = request.form.get("task")
    if new_task:
        tasks.append(new_task)
    return redirect("/")

@app.route("/projects/")
def projects_page():
    return render_template("projects.html", projects=projects)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
