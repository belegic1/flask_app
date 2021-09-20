from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms import validators
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

# WTForm


class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    name = StringField("Enter your name", validators=[DataRequired()])
    email = StringField("Enter your email", validators=[DataRequired()])
    password = PasswordField("Enter your password",
                             validators=[DataRequired()])
    submit = SubmitField("Submit", validators=[DataRequired()])


class LoginForm(FlaskForm):
    email = StringField("Enter your email", validators=[DataRequired()])
    password = PasswordField("Enter your password",
                             validators=[DataRequired()])
    submit = SubmitField("Submit", validators=[DataRequired()])


class CommentForm(FlaskForm):
    body = CKEditorField("Comment....", validators=[DataRequired()])
    submit = SubmitField("Submit Post")
