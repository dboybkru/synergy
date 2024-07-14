from flask import current_app as app, render_template, redirect, url_for, flash, request, abort, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from app import db
from app.models import User, Resume, Skill, Project, SocialLink, Tag, Notification
from app.forms import LoginForm, ResumeForm, SkillForm, ProjectForm, SocialLinkForm
import os
import json

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('resumes'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('resumes'))
        flash('Неверное имя пользователя или пароль', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
@app.route('/resumes')
@login_required
def resumes():
    return render_template('resumes.html', resumes=current_user.resumes)

@app.route('/create_resume', methods=['GET', 'POST'])
@login_required
def create_resume():
    form = ResumeForm()
    if form.validate_on_submit():
        resume = Resume(title=form.title.data, user=current_user)
        db.session.add(resume)
        db.session.commit()
        flash('Новое резюме создано', 'success')
        return redirect(url_for('edit_resume', resume_id=resume.id))
    return render_template('create_resume.html', form=form)

@app.route('/edit_resume/<int:resume_id>', methods=['GET', 'POST'])
@login_required
def edit_resume(resume_id):
    resume = Resume.query.get_or_404(resume_id)
    if resume.user != current_user:
        abort(403)
    form = ResumeForm(obj=resume)
    skill_form = SkillForm()
    project_form = ProjectForm()
    social_link_form = SocialLinkForm()
    
    if form.validate_on_submit():
        form.populate_obj(resume)
        if form.photo.data:
            filename = secure_filename(form.photo.data.filename)
            form.photo.data.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            resume.photo = filename
        db.session.commit()
        flash('Резюме обновлено', 'success')
        return redirect(url_for('edit_resume', resume_id=resume.id))
    
    return render_template('edit_resume.html', form=form, resume=resume, 
                           skill_form=skill_form, project_form=project_form, 
                           social_link_form=social_link_form)

@app.route('/delete_resume/<int:resume_id>', methods=['POST'])
@login_required
def delete_resume(resume_id):
    resume = Resume.query.get_or_404(resume_id)
    if resume.user != current_user:
        abort(403)
    db.session.delete(resume)
    db.session.commit()
    flash('Резюме удалено', 'success')
    return redirect(url_for('resumes'))

@app.route('/resume/<int:resume_id>')
def view_resume(resume_id):
    resume = Resume.query.get_or_404(resume_id)
    if not resume.is_public and (not current_user.is_authenticated or resume.user != current_user):
        abort(404)
    return render_template('view_resume.html', resume=resume)

@app.route('/add_skill/<int:resume_id>', methods=['POST'])
@login_required
def add_skill(resume_id):
    resume = Resume.query.get_or_404(resume_id)
    if resume.user != current_user:
        abort(403)
    form = SkillForm()
    if form.validate_on_submit():
        skill = Skill(name=form.name.data, level=form.level.data, resume=resume)
        db.session.add(skill)
        db.session.commit()
        flash('Навык добавлен', 'success')
    return redirect(url_for('edit_resume', resume_id=resume.id))

@app.route('/delete_skill/<int:resume_id>/<int:skill_id>')
@login_required
def delete_skill(resume_id, skill_id):
    resume = Resume.query.get_or_404(resume_id)
    if resume.user != current_user:
        abort(403)
    skill = Skill.query.get_or_404(skill_id)
    db.session.delete(skill)
    db.session.commit()
    flash('Навык удален', 'success')
    return redirect(url_for('edit_resume', resume_id=resume.id))

@app.route('/add_project/<int:resume_id>', methods=['POST'])
@login_required
def add_project(resume_id):
    resume = Resume.query.get_or_404(resume_id)
    if resume.user != current_user:
        abort(403)
    form = ProjectForm()
    if form.validate_on_submit():
        filename = ''
        if form.image.data:
            filename = secure_filename(form.image.data.filename)
            form.image.data.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        project = Project(title=form.title.data, description=form.description.data,
                          image=filename, link=form.link.data, resume=resume)
        
        tag_names = [tag.strip() for tag in form.tags.data.split(',') if tag.strip()]
        for tag_name in tag_names:
            tag = Tag.query.filter_by(name=tag_name).first()
            if not tag:
                tag = Tag(name=tag_name)
                db.session.add(tag)
            project.tags.append(tag)
        
        db.session.add(project)
        db.session.commit()
        flash('Проект добавлен', 'success')
    return redirect(url_for('edit_resume', resume_id=resume.id))

@app.route('/delete_project/<int:resume_id>/<int:project_id>')
@login_required
def delete_project(resume_id, project_id):
    resume = Resume.query.get_or_404(resume_id)
    if resume.user != current_user:
        abort(403)
    project = Project.query.get_or_404(project_id)
    if project.image:
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], project.image))
    db.session.delete(project)
    db.session.commit()
    flash('Проект удален', 'success')
    return redirect(url_for('edit_resume', resume_id=resume.id))

@app.route('/add_social_link/<int:resume_id>', methods=['POST'])
@login_required
def add_social_link(resume_id):
    resume = Resume.query.get_or_404(resume_id)
    if resume.user != current_user:
        abort(403)
    form = SocialLinkForm()
    if form.validate_on_submit():
        social_link = SocialLink(platform=form.platform.data, url=form.url.data, resume=resume)
        db.session.add(social_link)
        db.session.commit()
        flash('Ссылка на соцсеть добавлена', 'success')
    return redirect(url_for('edit_resume', resume_id=resume.id))

@app.route('/delete_social_link/<int:resume_id>/<int:link_id>')
@login_required
def delete_social_link(resume_id, link_id):
    resume = Resume.query.get_or_404(resume_id)
    if resume.user != current_user:
        abort(403)
    link = SocialLink.query.get_or_404(link_id)
    db.session.delete(link)
    db.session.commit()
    flash('Ссылка на соцсеть удалена', 'success')
    return redirect(url_for('edit_resume', resume_id=resume.id))

@app.route('/export_resume/<int:resume_id>')
@login_required
def export_resume(resume_id):
    resume = Resume.query.get_or_404(resume_id)
    if resume.user != current_user:
        abort(403)
    
    resume_data = {
        'title': resume.title,
        'about': resume.about,
        'education': resume.education,
        'experience': resume.experience,
        'desired_position': resume.desired_position,
        'additional_info': resume.additional_info,
        'contacts': resume.contacts,
        'skills': [{'name': skill.name, 'level': skill.level} for skill in resume.skills],
        'projects': [{
            'title': project.title,
            'description': project.description,
            'link': project.link,
            'tags': [tag.name for tag in project.tags]
        } for project in resume.projects],
        'social_links': [{'platform': link.platform, 'url': link.url} for link in resume.social_links]
    }
    
    return jsonify(resume_data)

@app.route('/notifications')
@login_required
def notifications():
    notifications = current_user.notifications.order_by(Notification.timestamp.desc()).all()
    return render_template('notifications.html', notifications=notifications)

@app.route('/mark_notification_read/<int:notification_id>')
@login_required
def mark_notification_read(notification_id):
    notification = Notification.query.get_or_404(notification_id)
    if notification.user != current_user:
        abort(403)
    notification.is_read = True
    db.session.commit()
    return redirect(url_for('notifications'))

@app.route('/projects')
def projects():
    resume = Resume.query.filter_by(is_public=True).first()
    if not resume:
        abort(404)
    tag = request.args.get('tag')
    sort = request.args.get('sort', 'newest')
    
    projects = resume.projects
    if tag:
        projects = projects.filter(Project.tags.any(name=tag))
    
    if sort == 'oldest':
        projects = projects.order_by(Project.id.asc())
    else:
        projects = projects.order_by(Project.id.desc())
    
    tags = Tag.query.all()
    return render_template('projects.html', projects=projects, tags=tags, current_tag=tag, sort=sort)

# def create_admin_user():
#     admin = User.query.filter_by(username='admin').first()
#     if not admin:
#         admin = User(username='admin', password=generate_password_hash('admin'))
#         db.session.add(admin)
#         db.session.commit()
#         print('Admin user created')
#     else:
#         print('Admin user already exists')

# @app.before_first_request
# def initialize_app():
#     create_admin_user()