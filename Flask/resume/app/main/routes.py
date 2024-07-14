import os
from flask import render_template, flash, redirect, url_for, request, send_from_directory, abort, current_app
from flask_login import current_user, login_required
from app import db
from app.main import bp
from app.main.forms import ResumeForm, CertificateForm
from app.models import Resume, Certificate, User
from werkzeug.utils import secure_filename

@bp.route('/')
@bp.route('/index')
def index():
    resumes = Resume.query.all()
    return render_template('index.html', title='Главная', resumes=resumes)

@bp.route('/resume/<username>')
def view_resume(username):
    user = User.query.filter_by(username=username).first_or_404()
    resume = Resume.query.filter_by(user_id=user.id).first_or_404()
    return render_template('view_resume.html', title=f'Резюме {username}', resume=resume, user=user)

@bp.route('/my_resume', methods=['GET', 'POST'])
@login_required
def my_resume():
    form = ResumeForm()
    cert_form = CertificateForm()
    resume = Resume.query.filter_by(user_id=current_user.id).first()
    
    if form.validate_on_submit():
        if resume is None:
            resume = Resume(user_id=current_user.id)
        
        resume.about = form.about.data
        resume.education = form.education.data
        resume.experience = form.experience.data
        resume.desired_position = form.desired_position.data
        resume.additional_info = form.additional_info.data
        resume.contacts = form.contacts.data
        
        if form.photo.data:
            filename = secure_filename(form.photo.data.filename)
            photo_path = os.path.join(current_app.root_path, 'static', 'uploads', filename)
            form.photo.data.save(photo_path)
            resume.photo = filename
        
        db.session.add(resume)
        db.session.commit()
        flash('Ваше резюме обновлено!')
        return redirect(url_for('main.my_resume'))
    
    elif request.method == 'GET' and resume:
        form.about.data = resume.about
        form.education.data = resume.education
        form.experience.data = resume.experience
        form.desired_position.data = resume.desired_position
        form.additional_info.data = resume.additional_info
        form.contacts.data = resume.contacts
    
    return render_template('my_resume.html', title='Мое резюме', form=form, cert_form=cert_form, resume=resume)

@bp.route('/upload_certificate', methods=['POST'])
@login_required
def upload_certificate():
    form = CertificateForm()
    if form.validate_on_submit():
        resume = Resume.query.filter_by(user_id=current_user.id).first()
        if resume:
            filename = secure_filename(form.certificate.data.filename)
            cert_path = os.path.join(current_app.root_path, 'static', 'uploads', filename)
            form.certificate.data.save(cert_path)
            certificate = Certificate(filename=filename, resume_id=resume.id)
            db.session.add(certificate)
            db.session.commit()
            flash('Сертификат загружен!')
        else:
            flash('Сначала создайте резюме!')
    return redirect(url_for('main.my_resume'))

@bp.route('/download_certificate/<filename>')
def download_certificate(filename):
    return send_from_directory(os.path.join(current_app.root_path, 'static', 'uploads'), filename, as_attachment=True)

@bp.route('/delete_certificate/<int:id>')
@login_required
def delete_certificate(id):
    certificate = Certificate.query.get_or_404(id)
    resume = Resume.query.filter_by(user_id=current_user.id).first()
    if resume and certificate in resume.certificates:
        file_path = os.path.join(current_app.root_path, 'static', 'uploads', certificate.filename)
        if os.path.exists(file_path):
            os.remove(file_path)
        db.session.delete(certificate)
        db.session.commit()
        flash('Сертификат удален!')
    else:
        flash('Ошибка при удалении сертификата.')
    return redirect(url_for('main.my_resume'))