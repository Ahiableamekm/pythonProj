from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collections.db"

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Book(db.Model):
    bid : Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author : Mapped[str] = mapped_column(String(250), nullable=False)
    rating : Mapped[float] = mapped_column(Float, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    all_books = db.session.execute(db.select(Book)).scalars()
    return render_template('index.html', books=list(all_books))


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        with app.app_context():
            new_record = Book(
                title = request.form["title"],
                author = request.form["author"],
                rating = request.form["rating"]
            )
            db.session.add(new_record)
            db.session.commit()
        return redirect(url_for('home'))
    
    return render_template("add.html")

@app.route('/edit/<int:bid>', methods=["POST", "GET"])
def edit(bid):
    with app.app_context():
        rating_to_edit = db.session.execute(db.select(Book).where(Book.bid==bid)).scalar()
        if request.method == "POST":
            rating_to_edit.rating = request.form["edit"]
            db.session.commit()
            
            return redirect(url_for('home'))
    return render_template('edit.html', book=rating_to_edit)


@app.route('/<int:bid>')
def delete(bid):
    with app.app_context():
        record_to_delete = db.session.execute(db.select(Book).where(Book.bid==bid)).scalar()
        db.session.delete(record_to_delete)
        db.session.commit()

    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

