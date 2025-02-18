# Generated by Django 3.1 on 2020-08-18 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminAccount',
            fields=[
                ('SId', models.AutoField(primary_key=True, serialize=False)),
                ('SFname', models.CharField(default='First Name', max_length=100)),
                ('SLname', models.CharField(default='Last Name', max_length=100)),
                ('SEmail', models.CharField(default='Email Name', max_length=100)),
                ('SUsername', models.CharField(default='Username ', max_length=100)),
                ('SPassword', models.TextField(default='Password ', max_length=3000)),
                ('SContactNo', models.CharField(default='Contact no', max_length=100)),
                ('SProfile', models.ImageField(default='dummy.jpg', upload_to='SuperAdmin/')),
                ('Token', models.CharField(default='0000', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Card_detail',
            fields=[
                ('Card_detail_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(default='Name', max_length=200)),
                ('Card_number', models.IntegerField(default='0')),
                ('Month', models.CharField(default='Month', max_length=200)),
                ('Year', models.CharField(default='Year', max_length=200)),
                ('Cvc', models.IntegerField(default='12345')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('Charge_Day', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('Category_Id', models.AutoField(primary_key=True, serialize=False)),
                ('C_Name', models.CharField(default='Name', max_length=100)),
                ('C_Image', models.ImageField(default='dummy.jpg', upload_to='Category/')),
                ('Status', models.CharField(choices=[('active', 'Active'), ('inactive', 'In_Active')], default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('Course_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Series_Image', models.ImageField(default='dummy.jpg', upload_to='Series_Image/')),
                ('Series_Name', models.CharField(default='Name', max_length=100)),
                ('Decsription', models.TextField(default='Desc')),
                ('Difficulty', models.CharField(choices=[('beginner', 'Beginner'), ('moderate', 'Moderate'), ('intermediate', 'Intermediate'), ('advance', 'Advance')], default='', max_length=100)),
                ('Intensity', models.CharField(choices=[('level1', 'Level_1'), ('level2', 'Level_2'), ('level3', 'Level_3'), ('level4', 'Level_4')], default='', max_length=100)),
                ('Status', models.CharField(choices=[('active', 'Active'), ('inactive', 'In_Active')], default='', max_length=100)),
                ('Subject', models.CharField(choices=[('Request_to_Change_Title', 'Request to Change Title'), ('Request_to_Remove_Video', 'Request to Remove Video'), ('Request_to_Change_Title', 'Request to Change Title'), ('other', 'other')], default='', max_length=100)),
                ('Message', models.TextField(default='No Message')),
                ('Category_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superadmin.category')),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Package_Name', models.CharField(choices=[('yearly', 'Premium'), ('monthly', 'Monthly'), ('notsubscribe', 'Not Subscribe to Any Package')], default='', max_length=100)),
                ('Package_Id', models.CharField(choices=[('yearly', 'Yearly'), ('monthly', 'Monthly'), ('notsubscribe', 'Not Subscribe to Any Package')], default='', max_length=100)),
                ('Duration', models.IntegerField(default='1')),
                ('Amount', models.FloatField(default='1', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer_Account',
            fields=[
                ('Trainer_Account_Id', models.AutoField(primary_key=True, serialize=False)),
                ('U_Fname', models.CharField(default='First Name', max_length=100)),
                ('U_Lname', models.CharField(default='Last Name', max_length=100)),
                ('U_Email', models.CharField(default='Email Name', max_length=100)),
                ('Username', models.CharField(default='Username ', max_length=100)),
                ('SPassword', models.TextField(default='Password ', max_length=3000)),
                ('U_ContactNo', models.CharField(default='Contact no', max_length=100)),
                ('U_Desc', models.TextField(default='No')),
                ('Gender', models.CharField(default='Male', max_length=100)),
                ('DOB', models.DateField(auto_now_add=True, null=True)),
                ('Joining_Date', models.DateField(auto_now_add=True, null=True)),
                ('Referal_Code', models.CharField(default='12345', max_length=100)),
                ('U_Image', models.ImageField(default='dummy.jpg', upload_to='TrainerAccount/')),
                ('Token', models.CharField(default='0000', max_length=20)),
                ('Status', models.CharField(choices=[('active', 'Active'), ('inactive', 'In_Active')], default='', max_length=100)),
                ('role', models.CharField(default='Teacher', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User_Account',
            fields=[
                ('User_Account_Id', models.AutoField(primary_key=True, serialize=False)),
                ('U_Fname', models.CharField(default='First Name', max_length=100)),
                ('U_Lname', models.CharField(default='Last Name', max_length=100)),
                ('U_Email', models.CharField(default='Email Name', max_length=100)),
                ('Username', models.CharField(default='Username ', max_length=100)),
                ('SPassword', models.TextField(default='Password ', max_length=3000)),
                ('U_ContactNo', models.CharField(default='Contact no', max_length=100)),
                ('U_Desc', models.TextField(default='No')),
                ('Gender', models.CharField(default='Male', max_length=100)),
                ('DOB', models.DateField(auto_now_add=True, null=True)),
                ('Joining_Date', models.DateField(auto_now_add=True, null=True)),
                ('U_Image', models.ImageField(default='dummy.jpg', upload_to='Useraccount/')),
                ('Token', models.CharField(default='0000', max_length=20)),
                ('Status', models.CharField(choices=[('active', 'Active'), ('inactive', 'In_Active')], default='', max_length=100)),
                ('Subscription', models.CharField(choices=[('yearly', 'Yearly'), ('monthly', 'Monthly'), ('notsubscribe', 'Not Subscribe to Any Package')], default='', max_length=100)),
                ('Refered_by_Trainer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='superadmin.trainer_account')),
            ],
        ),
        migrations.CreateModel(
            name='Upload_Single_Video',
            fields=[
                ('Upload_Single_Video_id', models.AutoField(primary_key=True, serialize=False)),
                ('Title_Name', models.CharField(default='Title', max_length=100)),
                ('Difficulty', models.CharField(choices=[('beginner', 'Beginner'), ('moderate', 'Moderate'), ('intermediate', 'Intermediate'), ('advance', 'Advance')], default='', max_length=100)),
                ('Intensity', models.CharField(choices=[('level1', 'Level_1'), ('level2', 'Level_2'), ('level3', 'Level_3'), ('level4', 'Level_4')], default='', max_length=100)),
                ('Decsription', models.TextField(default='Desc')),
                ('Video', models.FileField(default='dummy.jpg', upload_to='Videos/')),
                ('Thumbnail', models.ImageField(default='dummy.jpg', upload_to='Thumbnail/')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('Category_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superadmin.category')),
                ('Trainer_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superadmin.trainer_account')),
            ],
        ),
        migrations.CreateModel(
            name='Subject_Video',
            fields=[
                ('Subject_Video_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Title_Name', models.CharField(default='Title', max_length=100)),
                ('Difficulty', models.CharField(choices=[('beginner', 'Beginner'), ('moderate', 'Moderate'), ('intermediate', 'Intermediate'), ('advance', 'Advance')], default='', max_length=100)),
                ('Intensity', models.CharField(choices=[('level1', 'Level_1'), ('level2', 'Level_2'), ('level3', 'Level_3'), ('level4', 'Level_4')], default='', max_length=100)),
                ('Decsription', models.TextField(default='Desc')),
                ('Video', models.FileField(default='dummy.jpg', upload_to='Videos/')),
                ('Thumbnail', models.ImageField(default='dummy.jpg', upload_to='Thumbnail/')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('Category_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superadmin.category')),
                ('Course_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superadmin.course')),
                ('Trainer_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superadmin.trainer_account')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('Request_id', models.AutoField(primary_key=True, serialize=False)),
                ('Subject', models.CharField(default='subject', max_length=200)),
                ('message', models.CharField(default='message', max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('Status', models.CharField(choices=[('done', 'Done'), ('undone', 'Un_Done')], default='', max_length=100)),
                ('Series_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superadmin.course')),
                ('Subject_Video_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superadmin.subject_video')),
                ('Trainer_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superadmin.trainer_account')),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('Playlist_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(default='Title', max_length=100)),
                ('Decsription', models.TextField(default='Desc')),
                ('Image', models.ImageField(default='dummy.jpg', upload_to='Playlist/')),
                ('Subject_Video_Id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='superadmin.subject_video')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('Payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('Charge_id', models.CharField(default='jhdfkjdhfkjdkfjdkl', max_length=500)),
                ('status', models.IntegerField(default='1')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('Charge_Day', models.DateTimeField(auto_now_add=True, null=True)),
                ('Card_detail_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superadmin.card_detail')),
                ('Package_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superadmin.package')),
                ('User_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superadmin.user_account')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('Feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('Email', models.CharField(default='email', max_length=200)),
                ('Subject', models.CharField(default='subject', max_length=200)),
                ('message', models.CharField(default='message', max_length=200)),
                ('Attachment', models.FileField(default='dummy.jpg', upload_to='Feedback/')),
                ('User_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superadmin.user_account')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='Trainer_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superadmin.trainer_account'),
        ),
        migrations.AddField(
            model_name='card_detail',
            name='Package_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superadmin.package'),
        ),
        migrations.AddField(
            model_name='card_detail',
            name='User_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superadmin.user_account'),
        ),
    ]
