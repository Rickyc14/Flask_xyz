from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired()])
	content = TextAreaField('content', validators=[DataRequired()])
	gem_file = FileField('Share gem', validators=[FileRequired(), FileAllowed(['jpg', 'png'])]) #file required!!
	submit = SubmitField('Post')

