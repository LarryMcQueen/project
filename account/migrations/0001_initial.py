# Generated by Django 3.1.3 on 2021-08-28 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('full_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('session', models.CharField(blank=True, choices=[('', 'Select Year'), ('2019/2020', '2019/2020')], max_length=100, null=True)),
                ('college', models.CharField(blank=True, choices=[('', 'Select College'), ('Science', 'College Of Science'), ('Technology', 'College OF Technology')], max_length=100, null=True)),
                ('level', models.CharField(blank=True, choices=[('', 'Select Level'), ('300', '300'), ('400', '400')], max_length=100, null=True)),
                ('gender', models.CharField(blank=True, choices=[('', 'Select Gender'), ('M', 'Male'), ('F', 'Female')], max_length=50, null=True)),
                ('department', models.CharField(blank=True, choices=[('', 'Select Department'), ('Chemistry', 'Chemistry'), ('Industrial Chemistry', 'Industrial Chemistry'), ('Physics', 'Physics'), ('Geophysics', 'Geophysics'), ('Geology', 'Geology'), ('Computer Science', 'Computer Science'), ('Mathematics', 'Mathematics'), ('Environmental Management Toxicology', 'Environmental Sci'), ('Petroleum Engineering', 'Petroleum Engr'), ('Chemical Engineering', 'Chemical Engr'), ('Electrical Electronics Engineering', 'Elect/Elect Engr'), ('Mechanical Engineering', 'Mechanical Engr'), ('Marine Engineering', 'Marine Engr')], max_length=50, null=True)),
                ('matric_number', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile_image')),
                ('date_joined', models.DateField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateField(auto_now_add=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SiwesInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bankName', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('accountNo', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('sort_code', models.CharField(blank=True, max_length=50, null=True)),
                ('phoneNo', models.CharField(blank=True, max_length=50, null=True)),
                ('industryName', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('industryAddress', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('industrySupervisorname', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('industrySupervisorPhoneno', models.CharField(blank=True, max_length=50, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
            ],
        ),
    ]
