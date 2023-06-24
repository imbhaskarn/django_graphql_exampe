import graphene
from .mutation import Mutation

from graphene_django import DjangoObjectType, DjangoListField
from api.models import Book, Comment
from api.graphql.types import (
    BookType,
    CommentType
)


class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    book = graphene.Field(BookType, book_id=graphene.Int())
    
    def resolve_all_books(self, info, **kwargs):
        
        return Book.objects.all()

    def resolve_book(self, info, book_id):
        return Book.objects.get(pk=book_id)
    
    all_comments = graphene.List(CommentType)
    comment = graphene.Field(CommentType, comment_id=graphene.Int())
    
    def resolve_all_comments(self, info, **kwargs):
        return Comment.objects.all()

    def resolve_comment(self, info, comment_id):
        return Comment.objects.get(pk=comment_id)
    




schema = graphene.Schema(query=Query, mutation=Mutation)
