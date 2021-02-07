from django.test.testcases import TestCase
import graphene
from .schema import Query, Mutation
from .models import Post
import json


class BlogApiTest(TestCase):

    def setUp(self):
        super().setUp()
        Post.objects.create(title="sample", description="test_description", author="test_author")
        self.getpostbyid = """
                    query getpostbyid{
          post(id:1){
            id
            title
            commentSet{
              text
            }
          }
        }
        """

        self.getallposts = """query getposts {
                             posts{
                              id
                              title
                              author
                              description
                              commentSet{
                                id
                                text
                                
                              }
                            }
                            }"""

        self.createPost = """
        mutation createpost{
      
      createPost(input:{     
        title: "My post - 2",
        description: "My second post on Django",
        author: "Geek-3"
        }){
        ok
        post{
          
          title
          description
          publishDate
        }
      }
        """
        self.schema = graphene.Schema(query=Query, mutation=Mutation)

    def test_getpostbyid_api(self):
        result = self.schema.execute(self.getpostbyid)
        self.assertDictEqual({"post": {"id": "1", "title": "sample", "commentSet": []}}, result.data)

    def test_getallposts_api(self):
        result = self.schema.execute(self.getallposts)
        self.assertEqual("test_author", result.data.get('posts')[0].get("author"))




