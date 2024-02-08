from flask import Flask, render_template, request
from dotenv import dotenv_values
from post import Post
import requests
import smtplib

cred = dotenv_values(".env")
EMAIL = cred["EMAIL"]
PASSWORD = cred["PASS"]

app = Flask(__name__)
url = "https://api.npoint.io/8dc5244d07e4f67f1686"
post_data = requests.get(url).json()
post_object = [Post(post['id'], post['title'], post['subtitle'], post['body'], post['image_url'], post['author'], post['date']) for post in post_data]

@app.route("/")
def home():
    return render_template("index.html", data=post_object)


@app.route("/about")
def about():
    
        return render_template("about.html")

@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method =="POST":
        username = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg=f"Subject: New connection from {username} \n\nUsername: {username} \nEmail: {email} \nPhone number: {phone} \nMessage: {message}"
            )
        return render_template("contact.html", status="Sucessfully sent message")
    else:
        
        return render_template("contact.html", status="Contact me")

@app.route("/post/<int:post_num>")
def read_more(post_num):
    requested_post = None
    for pst in post_object:
        if pst.id == post_num:
            requested_post = pst

    return render_template("post.html", post = requested_post)


# @app.route("/entry-form", methods=["POST"])
# def receive_data():
#     if request.method =="POST":
#         username = request.form["name"]
#         email = request.form["email"]
#         phone = request.form["phone"]
#         message = request.form["message"]
#         print(username)
#         print(email)
#         print(phone)
#         print(message)

#         return f"<h1>Successfully sent your message</h1>"

if __name__ == "__main__":
    app.run(debug=True)