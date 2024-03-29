# Generated by Django 2.1.9 on 2019-06-30 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrators',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('aid', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=64)),
                ('bid', models.CharField(max_length=32, unique=True)),
                ('publisher_date', models.DateField(auto_now_add=True)),
                ('publisher_state', models.CharField(choices=[('checkout', '已出版'), ('dai', '待出版'), ('status', '审核中')], default='checkout', max_length=20)),
                ('authors', models.ManyToManyField(to='booksys.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Brorrow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_date', models.DateField(auto_now_add=True)),
                ('bookname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookname', to='booksys.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('cid', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Loss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('penalty_money', models.CharField(max_length=64)),
                ('lid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lid', to='booksys.Book')),
                ('lname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lname', to='booksys.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Overdue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('penalty_money', models.CharField(max_length=64)),
                ('overdue_date', models.DateField(auto_now_add=True)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booksys.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('address', models.CharField(max_length=64, unique=True)),
                ('city', models.CharField(max_length=32)),
                ('state_province', models.CharField(max_length=32)),
                ('country', models.CharField(max_length=32)),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Readers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('rid', models.CharField(max_length=32, unique=True)),
                ('sex', models.CharField(max_length=64)),
                ('Contact_number', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Returnbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Damage_situation', models.CharField(choices=[('checkout', '完好'), ('status', '损坏')], default='checkout', max_length=20)),
                ('Expired_condition', models.CharField(choices=[('checkout', '未逾期'), ('status', '逾期')], default='checkout', max_length=20)),
                ('tid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tid', to='booksys.Book')),
                ('tname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tname', to='booksys.Book')),
            ],
        ),
        migrations.AddField(
            model_name='overdue',
            name='reader_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booksys.Readers'),
        ),
        migrations.AddField(
            model_name='brorrow',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booksys.Readers'),
        ),
        migrations.AddField(
            model_name='brorrow',
            name='wid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wid', to='booksys.Book'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booksys.Publisher'),
        ),
    ]
