# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Headline(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=255)  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='Datetime', blank=True, null=True)  # Field name made lowercase.
    vader = models.FloatField(db_column='Vader', blank=True, null=True)  # Field name made lowercase.
    liuhu = models.FloatField(db_column='LiuHu', blank=True, null=True)  # Field name made lowercase.
    newssourceid = models.ForeignKey('Newssource', models.DO_NOTHING, db_column='NewsSourceId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Headline'


class Headlinekeyword(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    headlineid = models.ForeignKey(Headline, models.DO_NOTHING, db_column='HeadlineId')  # Field name made lowercase.
    keywordid = models.ForeignKey('Keyword', models.DO_NOTHING, db_column='KeywordId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HeadlineKeyword'


class Keyword(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Keyword'


class Newssource(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    url = models.CharField(db_column='Url', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        
        db_table = 'NewsSource'
