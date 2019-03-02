from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required


# class ReviewForm(FlaskForm):

#  title = StringField('Review title', validators=[Required()])

#  review = TextAreaField('Pitch review')
 

#  submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):

    submit = SubmitField('Submit')


# class CreatePitchs(FlaskForm):
#     pitch = TextAreaField('describe your business', validators=[Required()])
#     submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    comment = TextAreaField('leave The The Comment', validators=[Required()])
    submit = SubmitField('add your comment')


class PitchForm(FlaskForm):

    title = StringField('Pitch title', validators=[Required()])
    text = TextAreaField('Text', validators=[Required()])
    category = SelectField(
        'Type',
        choices=[('Busines pitch', 'General pitch'),
                 ('General pitch', 'Busines pitch')],
        validators=[Required()])
    submit = SubmitField('Submit')
