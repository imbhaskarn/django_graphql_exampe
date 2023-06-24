from graphene import Mutation
import graphene
from .types import BookType, UserType
from ..models import Book
from django.contrib.auth.models import User


import graphene
import graphql_jwt



class UserInput(graphene.InputObjectType):
    success = graphene.Boolean()
    error_msg = graphene.String()


class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    @staticmethod
    def mutate(root, info, username=None, password = None, email = None):
        user = User.objects.filter(username=username, email =email).first()
        if user:
            return CreateUser(success=False, error_msg = 'User with that email and username already exists!')

        new_user = User.objects.create_user(
            username=username, email=email, password=password)
        del new_user.password
        return CreateUser(user=new_user)


class BookInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    author = graphene.String()
    year_published = graphene.String()
    review = graphene.Int()


class CreateBook(graphene.Mutation):
    class Arguments:
        book_data = BookInput(required=True)

    book = graphene.Field(BookType)

    @staticmethod
    def mutate(root, info, book_data=None):
        book_instance = Book(
            title=book_data.title,
            author=book_data.author,
            year_published=book_data.year_published,
            review=book_data.review
        )
        book_instance.save()
        return CreateBook(book=book_instance)


class UpdateBook(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        book_data = BookInput(required=True)

    book = graphene.Field(BookType)

    @staticmethod
    def mutate(root, info, id, book_data=None):

        book_instance = Book.objects.get(pk=id)

        if book_instance:
            book_instance.title = book_data.title
            book_instance.author = book_data.author
            book_instance.year_published = book_data.year_published
            book_instance.review = book_data.review
            book_instance.save()

            return UpdateBook(book=book_instance)
        return UpdateBook(book=None)


class DeleteBook(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    book = graphene.Field(BookType)

    @staticmethod
    def mutate(root, info, id):
        book_instance = Book.objects.get(pk=id)
        book_instance.delete()

        return None


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    create_user = CreateUser.Field()
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()
    delete_book = DeleteBook.Field()
