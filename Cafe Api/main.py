import random
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean


app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


    def to_dict(self):
        return {column.name:getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record

# random cafe endpoint
@app.route("/random")
def get_random():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    random_cafe = random.choice(all_cafes)

    return jsonify({
        "cafe":random_cafe.to_dict()}
        )

# all cafe endpoint
@app.route("/all")
def all_cafes():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    return jsonify({
        "cafes":[cafe.to_dict() for cafe in all_cafes]
    })

# search cafe endpoint
@app.route("/search")
def search():
    loc = request.args.get("loc")
    query = db.session.execute(db.select(Cafe).where(Cafe.location==loc)).scalar()
    if query:
        return jsonify({
            "result":query.to_dict()
        }), 200
    return jsonify({
        "error":{
            "Not Found":"Sorry, we don't have a cafe at that locations."
        }
    }), 404


# HTTP POST - Create Record

# new cafe endpoint
@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
        name = request.form.get("name"),
        map_url = request.form.get("map"),
        img_url = request.form.get("image"),
        location = request.form.get("location"),
        seats = request.form.get("seats"),
        has_toilet = bool(request.form.get("toilet")),
        has_wifi = bool(request.form.get("wifi")),
        has_sockets = bool(request.form.get("sockets")),
        can_take_calls = bool(request.form.get("calls")),
        coffee_price = request.form.get("price")
    )

    db.session.add(new_cafe)
    db.session.commit()
    return jsonify({
        "response":{
            "success":"Successfully added a new cafe."
        }
    }), 200

# HTTP PUT/PATCH - Update Record

# price update endpoint
@app.route("/update-price/<id>", methods=["PATCH"])
def update(id):
    cafe_to_update = db.session.execute(db.select(Cafe).where(Cafe.id==id)).scalar()
    if cafe_to_update:
        cafe_to_update.coffee_price = request.args.get("new_price")
        db.session.commit()
        return jsonify({
            "response":{
                "success":"Successfully updated the price of the cafe."
            }
        }), 200
    return jsonify({
        "response":{
            "Not Found":"Sorry, there's no cafe by that id."
        }
        }), 404

# HTTP DELETE - Delete Record

# record deletion endpoint
@app.route("/report-closed/<id>", methods=["DELETE"])
def delete(id):
    cafe_to_delete = db.session.execute(db.select(Cafe).where(Cafe.id == id)).scalar()
    if cafe_to_delete:
        if request.args.get("api_key") == "TopSecretAPIKey":
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify({
                "response":{
                    "success":"Successfully deleted the cafe."
                }
            }), 200
        return jsonify({
            "response":{
                "Forbidden":"Sorry, you are not allowed. Make sure to get the correct api_key."
            }
        }), 403
    
    return jsonify({
        "response":{
            "NOt Found":"sorry, there's no cafe by that id."
        }
    })


if __name__ == '__main__':
    app.run(debug=True)
