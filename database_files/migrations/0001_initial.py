from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

from database_files.models import *

class Migration(migrations.Migration):
    initial = True
    
    dependencies = [
    ]
    
    operations = [
        migrations.CreateModel(
            name="File",
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,serialise=False,verbose_name="FILE")),
                ('content', models.TextField()),
                ('size', models.IntegerField()),
                objects
            ]
        )
    ]
    
    
    
    '''
    content = models.TextField()
    size = models.IntegerField()
    
    objects = FileManager()
    '''
    
    
    '''
    def forwards(self, orm):
        
        # Adding model 'File'
        db.create_table('database_files_file', (
            ('id', orm['database_files.File:id']),
            ('content', orm['database_files.File:content']),
            ('size', orm['database_files.File:size']),
        ))
        db.send_create_signal('database_files', ['File'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'File'
        db.delete_table('database_files_file')
        
    
    
    models = {
        'database_files.file': {
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {})
        }
    }
    
    complete_apps = ['database_files']
'''
