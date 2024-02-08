from flask import Flask
from flask import render_template
from post import Post
import requests


app = Flask(__name__)
url = "https://api.npoint.io/8dc5244d07e4f67f1686"
post_data = requests.get(url).json()
post_object = [Post(post['id'], post['title'], post['subtitle'], post['body'], post['image_url'], post['author'], post['date']) for post in post_data]

@app.route("/")
def home():
    return render_template("index.html", data=post_object)


@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/post.html/<int:post_num>")
def read_more(post_num):
    requested_post = None
    for pst in post_object:
        if pst.id == post_num:
            requested_post = pst

    return render_template("post.html", post = requested_post)

if __name__ == "__main__":
    app.run(debug=True)