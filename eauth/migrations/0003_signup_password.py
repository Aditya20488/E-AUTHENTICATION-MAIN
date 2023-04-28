

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eauth', '0002_remove_signup_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='password',
            field=models.CharField(default='', max_length=100),
        ),
    ]
