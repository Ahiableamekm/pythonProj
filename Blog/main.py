from flask import Flask, render_template
from post import Post
import requests

post_data = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_objects =[Post(post['id'], post["title"], post["subtitle"], post["body"]) for post in post_data]

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", data=post_objects)

@app.route("/<int:id>")
def read_more(id):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == id:
            requested_post = blog_post
    return render_template("post.html", data=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
