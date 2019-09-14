# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Knight.foo'
        db.delete_column('app1_knight', 'foo')
        db.delete_column('app1_knight', 'name')


    def backwards(self, orm):
        # Adding field 'Knight.foo'
        db.add_column('app1_knight', 'foo',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)


    models = {
        'app1.knight': {
            'Meta': {'object_name': 'Knight'},
            'age': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'dances_whenever_able': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'of_the_round_table': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['app1']
