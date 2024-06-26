# Generated by Django 4.2.6 on 2024-03-10 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_hashtag_post_tags'),
        ('users', '0002_user_profile_image_user_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='like_posts',
            field=models.ManyToManyField(blank=True, related_name='Like_users', to='posts.post', verbose_name='좋아요 누른 Post 목록'),
        ),
    ]
