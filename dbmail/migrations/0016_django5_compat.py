# Replace index_together with Index for Django 5.2 compatibility.
# index_together in 0001_initial created an auto-named index; we
# drop it and re-create with an explicit name.

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbmail', '0015_auto_20180926_1206'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='signaldeferreddispatch',
            index_together=set(),
        ),
        migrations.AddIndex(
            model_name='signaldeferreddispatch',
            index=models.Index(fields=['eta', 'done'], name='dbmail_sign_eta_bd53d1_idx'),
        ),
        migrations.AlterField(
            model_name='signaldeferreddispatch',
            name='done',
            field=models.BooleanField(default=None, null=True),
        ),
    ]
