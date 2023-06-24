from api.models import Book, Comment
from django.contrib.auth.models import User

from graphene_django import DjangoObjectType

class BookType(DjangoObjectType): 
    class Meta:
        model = Book
        fields = "__all__"

class CommentType(DjangoObjectType): 
    class Meta:
        model = Comment
        fields = "__all__"

class UserType(DjangoObjectType): 
    class Meta:
        model = User
        fields = "__all__"