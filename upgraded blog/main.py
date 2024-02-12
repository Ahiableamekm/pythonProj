from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


class BlogForm(FlaskForm):
    title = StringField(label="Blog Post Title", validators=[DataRequired()])
    subtitle = StringField(label="Subtitle", validators=[DataRequired()])
    author = StringField(label="Your Name", validators=[DataRequired()])
    image = URLField(label="Blog Image URL", validators=[DataRequired(), URL()])
    content = CKEditorField(label="Blog Content", validators=[DataRequired()])
    submit = SubmitField(label="Submit Post")


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = db.session.execute(db.select(BlogPost)).scalars().all()
    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/post/<post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.session.execute(db.select(BlogPost).where(BlogPost.id==post_id)).scalar()
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route("/add-new-post", methods=["POST", "GET"])
def add_new_post():
    blogform = BlogForm()
    if blogform.validate_on_submit():
        blogbost = BlogPost(
            title = blogform.title.data,
            subtitle = blogform.subtitle.data,
            date = date.today().strftime("%B %d, %Y"),
            body = blogform.content.data,
            author = blogform.author.data,
            img_url = blogform.image.data
        )
        db.session.add(blogbost)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=blogform)
 

# TODO: edit_post() to change an existing blog post
@app.route("/edit-post/<id>", methods=["POST", "GET"])
def edit_post(id):
    blogpost_to_edit = db.session.execute(db.select(BlogPost).where(BlogPost.id==id)).scalar()
    editpost = BlogForm(
        title = blogpost_to_edit.title,
        subtitle = blogpost_to_edit.subtitle,
        author = blogpost_to_edit.author,
        content = blogpost_to_edit.body,
        image = blogpost_to_edit.img_url,
    )
    if editpost.validate_on_submit():
        blogpost_to_edit.title = editpost.title.data
        blogpost_to_edit.subtitle = editpost.subtitle.data
        blogpost_to_edit.author = editpost.author.data
        blogpost_to_edit.img_url = editpost.image.data
        blogpost_to_edit.body = editpost.content.data
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template('make-post.html', form=editpost, id=id)


# TODO: delete_post() to remove a blog post from the database

@app.route("/delete/<post_id>")
def delete_post(post_id):
    post_to_delete = db.session.execute(db.select(BlogPost).where(BlogPost.id==post_id)).scalar()
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for("get_all_posts"))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
