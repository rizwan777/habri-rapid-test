# Generated by Django 2.2 on 2023-04-07 02:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remarks', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AcedemicDetail',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.BaseModel')),
                ('enrollment_id', models.CharField(blank=True, max_length=50, null=True)),
                ('in_class_of', models.IntegerField()),
                ('section', models.CharField(blank=True, max_length=20, null=True)),
            ],
            bases=('core.basemodel',),
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.BaseModel')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('last_name', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(blank=True, choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER')], max_length=100)),
                ('relationship_to_student', models.CharField(blank=True, choices=[('FATHER', 'FATHER'), ('MOTHER', 'MOTHER'), ('ADOPTED', 'ADOPTED'), ('OTHER', 'OTHER')], max_length=100)),
                ('relationship_desc', models.CharField(blank=True, max_length=50, null=True)),
                ('aadhar_no', models.IntegerField()),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='parents_profile/')),
                ('aadhar_picture', models.ImageField(blank=True, null=True, upload_to='parents_aadhar/')),
                ('profession', models.CharField(blank=True, max_length=50, null=True)),
                ('designation', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('core.basemodel', models.Model),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.BaseModel')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('last_name', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(blank=True, choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER')], max_length=100)),
                ('aadhar_no', models.IntegerField()),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='student_profile/')),
                ('aadhar_picture', models.ImageField(blank=True, null=True, upload_to='student_aadhar/')),
                ('mobile', models.CharField(blank=True, max_length=128, null=True, unique=True)),
                ('height', models.CharField(blank=True, max_length=120, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('state', models.CharField(blank=True, max_length=1024, null=True)),
                ('city', models.CharField(blank=True, max_length=1024, null=True)),
                ('country', models.CharField(blank=True, max_length=1024, null=True)),
                ('locality', models.CharField(blank=True, max_length=1024, null=True)),
                ('address', models.CharField(blank=True, max_length=1024, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('core.basemodel', models.Model),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.BaseModel')),
                ('document_id', models.BooleanField(default=False)),
                ('email_to_std_sent', models.BooleanField(default=False)),
                ('email_to_admin_sent', models.BooleanField(default=False)),
                ('acedemic_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.AcedemicDetail')),
                ('parent_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Parent')),
                ('student_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Student')),
            ],
            bases=('core.basemodel',),
        ),
        migrations.AddField(
            model_name='parent',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Student'),
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.BaseModel')),
                ('type_of_doc', models.CharField(blank=True, choices=[('AADHAR_CARD', 'AADHAR_CARD'), ('POA', 'POA'), ('POI', 'POI'), ('TC', 'TC'), ('OTHER', 'OTHER')], max_length=100)),
                ('doc', models.ImageField(blank=True, null=True, upload_to='documents/')),
                ('doc_desc', models.CharField(blank=True, max_length=50, null=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Student')),
            ],
            bases=('core.basemodel',),
        ),
        migrations.AddField(
            model_name='acedemicdetail',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Student'),
        ),
    ]
