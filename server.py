from flask import Flask, render_template
from post import Post

app = Flask(__name__)

blog_posts = Post()

@app.route('/')
def home():
    return render_template("index.html", blog_posts = blog_posts.get_all_blog_posts())

@app.route('/post/<int:post_id>')
def get_post(post_id):
    post = blog_posts.get_post_by_id(post_id)
    return render_template("post.html", post = post[0])

if __name__ == "__main__":
    app.run(debug=True)
