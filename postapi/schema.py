import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from postapi.models import Post, Comment
from graphene.types import InputObjectType


class PostType(DjangoObjectType):
    class Meta:
        model = Post


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment


class Query(ObjectType):

    post = graphene.Field(PostType, id=graphene.Int())
    comment = graphene.Field(CommentType, id=graphene.Int())
    posts = graphene.List(PostType)
    comments = graphene.List(CommentType)

    def resolve_post(self, info, **kwargs):
        id = kwargs.get('id')
        return Post.objects.get(pk=id)

    def resolve_comment(self, info, **kwargs):
        id = kwargs.get('id')
        return Comment.objects.get(pk=id)

    def resolve_posts(self, info, ** kwargs):
        return Post.objects.all()

    def resolve_comments(self, info, **kwargs):
        return Comment.objects.all()


class PostInput(InputObjectType):
    title = graphene.String()
    description = graphene.String()
    author = graphene.String()


class CommentInput(InputObjectType):

    # post = graphene.Field(PostType)
    text = graphene.String()
    author = graphene.String()
    postId = graphene.Int()


class CreatePost(graphene.Mutation):
    class Arguments:
        input = PostInput(required=True)

    ok = graphene.Boolean()
    post = graphene.Field(PostType)

    @staticmethod
    def mutate(root, info, id=None, input=None):
        ok = True
        post_instance = Post(title=input.title,
                             description=input.description,
                             author=input.author)
        post_instance.save()
        return CreatePost(ok, post_instance)


class CreateComment(graphene.Mutation):
    class Arguments:
        input = CommentInput(required=True)

    ok = graphene.Boolean()
    comment = graphene.Field(CommentType)

    @staticmethod
    def mutate(self, info, input=None):
        ok = False
        comment_instance = Comment(text=input.text, author=input.author,post_id = input.postId)
        comment_instance.save()
        ok = True
        return CreateComment(ok, comment_instance)


class UpdatePost(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = PostInput(required=True)

    ok = graphene.Boolean()
    post = graphene.Field(PostType)

    @staticmethod
    def mutate(self, info, id, input):
        ok = False
        post_instance = Post.objects.get(pk=id)
        post_instance.title = input.title
        post_instance.description = input.description
        post_instance.author = input.author
        post_instance.save()
        ok = True
        return UpdatePost(ok, post_instance)


class DeleteComment(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    ok = graphene.Boolean()

    @staticmethod
    def mutate(self, info, id):
        ok = False
        comment = Comment.objects.get(pk=id)
        comment.delete()
        ok = True
        return UpdatePost(ok)


class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
    create_comment = CreateComment.Field()
    delete_comment = DeleteComment.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)


