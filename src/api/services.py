from django.core.exceptions import ValidationError


def get_path_upload_avatar(instans, file):
    """
    Построение пути к файлу, format: (media)/avatar/user_id/photo.jpg
    """
    return f'avatar/{instans}/{file}'


def validate_size_image(file_obj):
    limit = 5
    if file_obj.size > limit * 1024 * 1024:
        raise ValidationError(f'Максимальный размер файла {limit}МБ')