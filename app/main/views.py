from flask import render_template,request,redirect,url_for
from . import main


from flask import render_template, request, redirect, url_for, abort
from ..models import User,Role,Pitch,Comment
from .forms import UpdateProfile,CommentForm, PitchForm
from .. import db
from flask_login import login_required, current_user
import markdown2



@main.route('/')
def index():
    business = Pitch.get_pitchs('business')
    general = Pitch.get_pitchs('general')

    title = 'pitch'
    pitch = Pitch.query.all()
    return render_template('index.html', title=title, pitch=pitch,business=business, general=general)


@main.route('/pitchs/business')
def business():
    pitchs = Pitch.get_pitchs('business')

    return render_template('business.html', pitchs=pitchs)


@main.route('/pitchs/general')
def general():
    pitchs = Pitch.get_pitchs('general')

    return render_template('general.html', pitchs=pitchs)


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()


    return render_template('profile/update.html', form=form)


@main.route('/pitch/new', methods=['GET', 'POST'])
@login_required
def new_pitch():
    pitch_form = PitchForm()
    if pitch_form.validate_on_submit():
        title = pitch_form.title.data
        pitch = pitch_form.text.data
        category = pitch_form.category.data

        # Updated pitch instance
        new_pitch = Pitch(
            pitch_title=title,
            pitch_content=pitch,
            category=category,
            user=current_user)

        # Save pitch method
        new_pitch.save_pitch()
        return redirect(url_for('.index'))

        title = 'New pitch'
    return render_template('newpitch.html', pitchForm=pitch_form)



@main.route('/pitch', methods=['GET', 'POST'])
def create_pitchs():
    form = CreatePitchs()
    print(current_user.id)
    if form.validate_on_submit():
        pitch = form.text.data
        category = form.category.data

        new_pitch = Pitch(pitch=pitch, user_id=current_user.id,
                          category=category, likes=0, dislikes=0)
        new_pitch.save_pitch()
        return redirect(url_for('main.index'))

        title = 'New Pitch'
    return render_template('pitch.html', form=form, user=current_user)




    #     new_pitch = Pitch(pitch=pitch, user_id=current_user.id)

    #     db.session.add(new_pitch)
    #     db.session.commit()

    #     return redirect(url_for('main.index'))

    # return render_template('pitch.html', form=form, user=current_user)


@main.route('/pitch/comment/<int:id>', methods=['GET', 'POST'])
@login_required
def create_comments(id):
    form = CommentForm()
   
    if form.validate_on_submit():
        comment = form.text.data

    #     comment = form.comment.data

    #     new_comment = Comment(comment=comment, pitch_id=id,user_id=current_user.id)
    #     db.session.add(new_comment)
    #     db.session.commit()

    # comment = Comment.query.filter_by(pitch_id=id).all()

    # return render_template('comment.html', comment=comment, form=form)


        new_comment = Comment(comment = comment, user = current_user, pitch_id = pitch)

        new_comment.save_comment()

        comments = Comment.get_comments(pitch)

    return render_template('pitch.html', pitch = pitch, comment_form = form,comment = comment, date = posted_date)

