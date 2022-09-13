import uuid

from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import DO_NOTHING

from .validators import validator_pub_year


class User(AbstractUser):
    """User augmented fields."""

    USER_ROLE_USER = 'user'
    USER_ROLE_MODERATOR = 'moderator'
    USER_ROLE_ADMIN = 'admin'

    USER_ROLE_CHOICES = (
        (USER_ROLE_USER, 'User'),
        (USER_ROLE_MODERATOR, 'Moderator'),
        (USER_ROLE_ADMIN, 'Administrator'),
    )

    email = models.EmailField(
        verbose_name='E-mail',
        max_length=254,
        unique=True
    )
    role = models.CharField(
        verbose_name='Role',
        max_length=50,
        blank=True,
        choices=USER_ROLE_CHOICES,
        default=USER_ROLE_USER,
    )

    bio = models.TextField(
        verbose_name='Bio',
        blank=True,
        max_length=1000
    )

    confirmation_code = models.CharField(
        verbose_name='Confirmation code',
        max_length=100,
        null=True,
        default=str(uuid.uuid4())
    )

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'],
                name='unique_username_email'
            )
        ]

    @property
    def is_user(self):
        return self.role == self.USER_ROLE_USER

    @property
    def is_admin(self):
        return self.is_staff or self.role == self.USER_ROLE_ADMIN

    @property
    def is_moderator(self):
        return self.role == self.USER_ROLE_MODERATOR


class Category(models.Model):
    """Types of works (Movies, Books, Music)."""

    name = models.CharField(
        verbose_name='Category',
        max_length=100,
        blank=True,
        null=True,
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Genre(models.Model):
    """Genres of works

    One work can be linked to more than one genre.
    """
    name = models.CharField(
        verbose_name='Genre',
        max_length=100,
        blank=True,
        null=True
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
    )

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    def __str__(self):
        return self.name


class Title(models.Model):
    """Works for which reviews are written."""

    name = models.CharField(
        verbose_name='Title',
        max_length=200,
        blank=True,
        null=True,
    )
    year = models.PositiveSmallIntegerField(
        verbose_name='Year',
        validators=[validator_pub_year],
        null=True,
    )
    description = models.TextField(
        verbose_name='Description',
        blank=True,
        null=True,
    )
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Genre',
        related_name='title',
        db_index=True,
        blank=True,

    )
    category = models.ForeignKey(
        Category,
        verbose_name='Category',
        related_name='title',
        on_delete=DO_NOTHING,
        null=True,
    )

    class Meta:
        verbose_name = 'Title'
        verbose_name_plural = 'Titles'

    def __str__(self):
        return self.name


class Review(models.Model):
    """Reviews of works

    Review is linked to a specific piece of work.
    """

    title = models.ForeignKey(
        Title,
        verbose_name='Title',
        related_name='reviews',
        on_delete=models.CASCADE,
    )

    text = models.TextField(
        verbose_name='Review text'
    )

    pub_date = models.DateTimeField(
        verbose_name='Publication date',
        auto_now_add=True,
        db_index=True,
    )

    author = models.ForeignKey(
        User,
        verbose_name='Author',
        on_delete=models.CASCADE,
        related_name='reviews',
    )

    score = models.PositiveSmallIntegerField(
        verbose_name='Score',
        default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1),
        ],
        blank=False,
        null=False
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='unique_author_review'
            )
        ]

    def __str__(self):
        return self.text[:15]


class Comment(models.Model):
    """Comments on the feedback
    Comment is linked to a specific review.
    """

    text = models.TextField(
        verbose_name='Comment'
    )

    pub_date = models.DateTimeField(
        verbose_name='Publication date',
        auto_now_add=True,
        db_index=True,
    )

    author = models.ForeignKey(
        User,
        verbose_name='Author',
        on_delete=models.CASCADE,
        related_name='comments',
    )
    review = models.ForeignKey(
        Review,
        verbose_name='Review',
        related_name='comments',
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.text[:15]
