# Register modeltranslation fields in migration state.
# Columns already exist in DB (created by sync_translation_fields).
# SeparateDatabaseAndState ensures no SQL is emitted for AddField.

from django.db import migrations, models


def _add_field_state_only(model_name, name, field):
    """AddField that only updates Django state, skips DB."""
    return migrations.SeparateDatabaseAndState(
        state_operations=[
            migrations.AddField(model_name=model_name, name=name, field=field),
        ],
        database_operations=[],
    )


class Migration(migrations.Migration):

    dependencies = [
        ("dbmail", "0016_django5_compat"),
    ]

    operations = [
        # mailbasetemplate translation fields
        _add_field_state_only("mailbasetemplate", "message_el", models.TextField(
            help_text="Basic template for mail messages. {{content}} tag for msg.", null=True, verbose_name="Body")),
        _add_field_state_only("mailbasetemplate", "message_en", models.TextField(
            help_text="Basic template for mail messages. {{content}} tag for msg.", null=True, verbose_name="Body")),
        _add_field_state_only("mailbasetemplate", "message_mn", models.TextField(
            help_text="Basic template for mail messages. {{content}} tag for msg.", null=True, verbose_name="Body")),
        _add_field_state_only("mailbasetemplate", "message_ru", models.TextField(
            help_text="Basic template for mail messages. {{content}} tag for msg.", null=True, verbose_name="Body")),
        _add_field_state_only("mailbasetemplate", "message_tg", models.TextField(
            help_text="Basic template for mail messages. {{content}} tag for msg.", null=True, verbose_name="Body")),

        # mailtemplate message translation fields
        _add_field_state_only("mailtemplate", "message_el", models.TextField(null=True, verbose_name="Body")),
        _add_field_state_only("mailtemplate", "message_en", models.TextField(null=True, verbose_name="Body")),
        _add_field_state_only("mailtemplate", "message_mn", models.TextField(null=True, verbose_name="Body")),
        _add_field_state_only("mailtemplate", "message_ru", models.TextField(null=True, verbose_name="Body")),
        _add_field_state_only("mailtemplate", "message_tg", models.TextField(null=True, verbose_name="Body")),

        # mailtemplate subject translation fields
        _add_field_state_only("mailtemplate", "subject_el", models.CharField(max_length=100, null=True, verbose_name="Subject")),
        _add_field_state_only("mailtemplate", "subject_en", models.CharField(max_length=100, null=True, verbose_name="Subject")),
        _add_field_state_only("mailtemplate", "subject_mn", models.CharField(max_length=100, null=True, verbose_name="Subject")),
        _add_field_state_only("mailtemplate", "subject_ru", models.CharField(max_length=100, null=True, verbose_name="Subject")),
        _add_field_state_only("mailtemplate", "subject_tg", models.CharField(max_length=100, null=True, verbose_name="Subject")),

        # maillog backend choices update
        migrations.AlterField(
            model_name="maillog",
            name="backend",
            field=models.CharField(
                choices=[
                    ("bot", "dbmail.backends.bot"),
                    ("mail", "unegui.dbmail_backends.mail"),
                    ("messenger", "unegui.dbmail_backends.messenger"),
                    ("push", "unegui.dbmail_backends.push"),
                    ("sms", "dbmail.backends.sms"),
                    ("tts", "dbmail.backends.tts"),
                ],
                db_index=True, default="mail", editable=False, max_length=25, verbose_name="Backend",
            ),
        ),
    ]
