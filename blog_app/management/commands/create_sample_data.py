from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog_app.models import BlogPost, Tweet

class Command(BaseCommand):
    help = 'Create sample data for testing search functionality'

    def handle(self, *args, **options):
        # Create a test user if it doesn't exist
        user, created = User.objects.get_or_create(
            username='testuser',
            defaults={'email': 'test@example.com'}
        )
        if created:
            user.set_password('testpass123')
            user.save()
            self.stdout.write(self.style.SUCCESS('Created test user'))

        # Create sample BlogPost data
        blog_posts_data = [
            {
                'title': 'Django Web Development',
                'content': 'Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel.'
            },
            {
                'title': 'Python Programming Tips',
                'content': 'Python is a versatile programming language that is widely used in web development, data science, artificial intelligence, and more. Here are some essential tips for Python developers to improve their coding skills and productivity.'
            },
            {
                'title': 'Database Design Best Practices',
                'content': 'Good database design is crucial for the performance and maintainability of your applications. Learn about normalization, indexing, relationships, and other important concepts in database design.'
            },
            {
                'title': 'Web Security Fundamentals',
                'content': 'Security is a critical aspect of web development. Understanding common vulnerabilities like SQL injection, XSS attacks, and CSRF protection is essential for building secure web applications.'
            }
        ]

        for post_data in blog_posts_data:
            BlogPost.objects.get_or_create(
                title=post_data['title'],
                defaults={
                    'user': user,
                    'content': post_data['content']
                }
            )

        # Create sample Tweet data with titles and content
        tweet_data = [
            {
                'title': 'Learning Django',
                'text': 'Just started learning Django framework!',
                'content': 'Django is amazing for web development. The ORM, admin interface, and built-in authentication make development so much easier.'
            },
            {
                'title': 'Python Tips',
                'text': 'Some useful Python tips for beginners',
                'content': 'List comprehensions, decorators, and context managers are powerful Python features that every developer should know.'
            },
            {
                'title': 'Database Optimization',
                'text': 'Database performance is crucial',
                'content': 'Proper indexing, query optimization, and database design can significantly improve your application performance.'
            }
        ]

        for tweet_info in tweet_data:
            Tweet.objects.get_or_create(
                text=tweet_info['text'],
                defaults={
                    'user': user,
                    'title': tweet_info['title'],
                    'content': tweet_info['content']
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully created sample data'))
