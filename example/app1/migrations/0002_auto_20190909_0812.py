# Generated by Django 2.2.5 on 2019-09-09 08:12

from django.db import migrations


def my_editor(app, schema_editor):
    Person = app.get_model("app1", "Person")
    schema_editor.remove_field(Person, "age")


class Migration(migrations.Migration):

    dependencies = [("app1", "0001_initial")]

    operations = [migrations.RunPython(my_editor)]
