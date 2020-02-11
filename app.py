import os
import env
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt

app = Flask(__name__)

app.config["MONGODB_NAME"] = 'milestone-project'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')

mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def index():
    four_recipes = mongo.db.recipes.find().sort([('views', -1)]).limit(3)

    return render_template("index.html", recipes=four_recipes)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'username': request.form.get('username')})

        if login_user:
            if bcrypt.hashpw(request.form.get('password').encode('utf-8'), login_user['password']) == login_user['password']:
                session['username'] = request.form['username']
                return redirect(url_for('index'))
            
            return "Invalid password"
        return "Invalid username"
    return render_template("login.html")


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'username': request.form.get('username')})
        existing_email = users.find_one({'email': request.form.get('email')})

        if existing_user is None:
            if existing_email is None:
                hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
                users.insert_one({'username': request.form['username'],
                                  'email': request.form['email'],
                                  'password': hashpass})
                session['username'] = request.form['username']
                return redirect(url_for('index'))
            
            flash("An account with that email address already exists!")
        flash("That username already exists!")
    return render_template('register.html')


@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())


@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):

    mongo.db.recipes.find_one_and_update(
        {'_id': ObjectId(recipe_id)},
        {'$inc': {'views': 1}}
        )

    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    

    return render_template('recipe.html', recipe=the_recipe)

@app.route('/add_recipe')
def add_recipe():
    return render_template("add-recipe.html")


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one({'title': request.form.get('recipe_name').capitalize(),
                        'image_url': request.form.get('image_url'),
                        'description': request.form.get('recipe_description').capitalize(),
                        'ingredients': request.form.get('recipe_ingredients').capitalize(),
                        'method': request.form.get('recipe_ingredients').capitalize()})

    return redirect(url_for('get_recipes'))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})

    return render_template("edit-recipe.html", recipe=the_recipe)


@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update(
        {'_id': ObjectId(recipe_id)},
        {'title': request.form.get('recipe_name').capitalize(),
         'image_url': request.form.get('image_url'),
         'description': request.form.get('recipe_description').capitalize(),
         'ingredients': request.form.get('recipe_ingredients').capitalize(),
         'method': request.form.get('recipe_method').capitalize()})
    
    return redirect(url_for('get_recipes'))


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})

    return redirect(url_for('get_recipes'))

if (__name__) == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
