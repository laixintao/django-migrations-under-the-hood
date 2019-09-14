# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Knight.age'
        db.delete_column('app1_knight', 'age')


    def backwards(self, orm):
        # Adding field 'Knight.age'
        db.add_column('app1_knight', 'age',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)


    models = {
        'app1.knight': {
            'Meta': {'object_name': 'Knight'},
            'dances_whenever_able': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'of_the_round_table': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['app1']
