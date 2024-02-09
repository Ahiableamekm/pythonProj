from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, desc
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange
from dotenv import dotenv_values
import requests

cred = dotenv_values('.env')

TOKEN = cred["TOKEN"]
SEARCH_ENDPOINT = "https://api.themoviedb.org/3/search/movie"
DETAIL_ENDPOINT = f"https://api.themoviedb.org/3/movie"
HEADERS = {
    "accept": "application/json",
    "Authorization": f"Bearer {TOKEN}"
}

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"

# CREATE DB
class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()

class EditRating(FlaskForm):
    updated_rating = FloatField(label="Your Rating Out of 10. e.g, 7.5", validators=[DataRequired(), NumberRange(min=0, max=10)])
    updated_review = StringField(label="Your Review", validators=[DataRequired()])
    submit_update = SubmitField(label="Done")

class AddMovie(FlaskForm):
    movie_search = StringField(label="Movie Title", validators=[DataRequired()])
    search_button = SubmitField(label="Add Movie")


@app.route("/")
def home():
    all_movies = db.session.execute(db.select(Movie).order_by(desc(Movie.rating))).scalars()
    for rank, movie in enumerate(all_movies, 1):
        movie.ranking = rank
        db.session.commit()
    all_movies = db.session.execute(db.select(Movie).order_by(desc(Movie.rating))).scalars()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["POST", "GET"])
def edit():
    movie_id = request.args.get("id")
    update_form = EditRating()
    record_to_be_update = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
    if update_form.validate_on_submit():
        record_to_be_update.rating = float(update_form.updated_rating.data)
        record_to_be_update.review = update_form.updated_review.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", form=update_form, title=record_to_be_update.title)

@app.route("/delete")
def delete():
    id = request.args.get("id")
    with app.app_context():
        record_to_delete = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()
        db.session.delete(record_to_delete)
        db.session.commit()
        return redirect(url_for('home'))






@app.route("/add", methods=["POST", "GET"])
def add():
    addmovie_form = AddMovie()
    if addmovie_form.validate_on_submit():
        movie_params ={
            "query":addmovie_form.movie_search.data
        }
        response = requests.get(SEARCH_ENDPOINT, params=movie_params, headers=HEADERS).json()
        movie_list = response["results"]
        return render_template("select.html", data=movie_list)
    return render_template ("add.html", form=addmovie_form)


@app.route("/fetch")
def fetch():
    movie_id = request.args.get("id")
    if movie_id:   
        responds = requests.get(f"{DETAIL_ENDPOINT}/{movie_id}", headers=HEADERS)
        data = responds.json()
        new_record = Movie(
            title = data["title"],
            year = int(data["release_date"].split("-")[0]),
            img_url = f"https://image.tmdb.org/t/p/w500{data['poster_path']}",
            description=data["overview"]

        )
        db.session.add(new_record)
        db.session.commit()
    return redirect(url_for('edit', id=new_record.id))

if __name__ == '__main__':
    app.run(debug=True)
























# first movie
# with app.app_context():
#     new_record = Movie(
#         title = "Phone Booth",
#         year = 2002,
#         description = "Publicist Stuart Shepard finds himself trapped in a phone booth," \
#                       "pinned down by an extortionist's sniper rifle. Unable to leave or " \
#                       "receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax",
#         rating = 7.3,
#         ranking = 10,
#         review = "My favorite charater wast the caller",
#         image_url = "https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg",
#     )
#     db.session.add(new_record)
#     db.session.commit()

# Second Movie
# with app.app_context():
#     another_record = Movie(
#         title = "Avata The way of Water",
#         year = 2022,
#         description = "Set more than a decade after the events of the first film, learn the story of the Sully family" \
#                       "(Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe," \
#                         "the battles they fight to stay alive, and the tragedies they endure." ,
#         rating = 7.3,
#         ranking = 9,
#         review = 'I liked the water',
#         image_url = "https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
#     )
#     db.session.add(another_record)
#     db.session.commit()