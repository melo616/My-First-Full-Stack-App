from flask import Flask, render_template, request, redirect
from flask_app.models.user_model import User
from flask_app import app 

@app.route("/")
def index():
    all_users = User.get_all()
    return render_template("read_all.html", all_users=all_users)

@app.route("/create")
def new_user_form():
    return render_template("create.html")

@app.route("/process/create", methods=["POST"])
def create():
    this_id = User.create(request.form) #User.create returns the id of the user just created
    return redirect(f'/users/{this_id}/show')

@app.route("/users/<int:id>/show")
def get_one(id):
    data = {
        'id':id
    }
    one_user = User.get_one(data)
    return render_template("read_one.html", one_user=one_user)

@app.route("/users/<int:id>/edit")
def edit_user(id):
    this_user = User.get_one({'id':id})
    return render_template("users_edit.html", this_user=this_user)

@app.route('/users/<int:id>/update', methods=['POST'])
def update_user(id):
    data = {
        'id': id,
        **request.form
    }
    User.update(data)
    return redirect('/')

@app.route('/users/<int:id>/delete')
def delete_user(id):
    User.delete({'id':id})
    return redirect('/')
