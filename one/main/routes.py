from flask import render_template, request, Blueprint
from one.models import Post

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home") ## @ decorators
def home():
	page = request.args.get('page', 1, type=int) ### type int => prevents people from request float pages 1.34
	posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
	return render_template('home.html', posts=posts)

@main.route("/about")
def about():
	return render_template('about.html', title='About')

