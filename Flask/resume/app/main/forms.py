from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class ResumeForm(FlaskForm):
    photo = FileField('Фото', validators=[FileAllowed(['jpg', 'png'])])
    about = TextAreaField('О себе', validators=[DataRequired()])
    education = TextAreaField('Образование', validators=[DataRequired()])
    experience = TextAreaField('Опыт работы', validators=[DataRequired()])
    desired_position = StringField('Желаемая должность', validators=[DataRequired()])
    additional_info = TextAreaField('Дополнительная информация')
    contacts = TextAreaField('Контакты', validators=[DataRequired()])
    submit = SubmitField('Сохранить')

class CertificateForm(FlaskForm):
    certificate = FileField('Сертификат', validators=[FileAllowed(['pdf'])])
    submit = SubmitField('Загрузить')