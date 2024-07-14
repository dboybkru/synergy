from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, PasswordField, SubmitField, SelectField, IntegerField, BooleanField
from wtforms.validators import DataRequired, URL, NumberRange

class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')

class ResumeForm(FlaskForm):
    title = StringField('Название резюме', validators=[DataRequired()])
    photo = FileField('Фото', validators=[FileAllowed(['jpg', 'png'], 'Только изображения!')])
    about = TextAreaField('О себе')
    education = TextAreaField('Образование')
    experience = TextAreaField('Опыт работы')
    desired_position = StringField('Желаемая должность')
    additional_info = TextAreaField('Дополнительная информация')
    contacts = TextAreaField('Контакты')
    block_order = StringField('Порядок блоков')
    color_scheme = SelectField('Цветовая схема', choices=[('light', 'Светлая'), ('dark', 'Темная')])
    is_public = BooleanField('Опубликовать резюме')
    submit = SubmitField('Сохранить')

class SkillForm(FlaskForm):
    name = StringField('Название навыка', validators=[DataRequired()])
    level = IntegerField('Уровень (1-100)', validators=[DataRequired(), NumberRange(min=1, max=100)])
    submit = SubmitField('Добавить навык')

class ProjectForm(FlaskForm):
    title = StringField('Название проекта', validators=[DataRequired()])
    description = TextAreaField('Описание')
    image = FileField('Изображение', validators=[FileAllowed(['jpg', 'png'], 'Только изображения!')])
    link = StringField('Ссылка на проект', validators=[URL()])
    tags = StringField('Теги (через запятую)')
    submit = SubmitField('Добавить проект')

class SocialLinkForm(FlaskForm):
    platform = StringField('Платформа', validators=[DataRequired()])
    url = StringField('URL', validators=[DataRequired(), URL()])
    submit = SubmitField('Добавить ссылку')