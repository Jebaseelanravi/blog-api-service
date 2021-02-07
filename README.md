# blog-api-service
Simple Blog API service built using Django,GraphQL and Python

### Live Demo on Heroku

https://jeba-blogapi.herokuapp.com/graphql

## How to run this project in your machine

#### prerequisite 
- Python 3

#### Installation procedure

Clone the repo

```shell script
git clone https://github.com/Jebaseelanravi/blog-api-service.git
```

install the dependencies
```shell script

cd blog-api-service 

pip install -r requirements.txt

```
create the databases

```shell script

python manage.py makemigrations

python manage.py migrate
```

Load sample Data

```shell script

python manage.py loaddata data.json
```

run the server

```shell script
python manage.py runserver 8000

```

Run test

```shell script
python manage.py  test
```

Explore the application

Launch http://127.0.0.1:8000/graphql/  in your browser




### API's Implemented

1. ##### Implemented  a createPost() mutation which will create a Post (a blogpost object) with attributes {title, description, publish_date, author (just a name as TextField)}
    ```json5
        # GraphQL Query 
        mutation createpost{
          
          createPost(input:{     
            title: "My post - 2",
            description: "My second post on Django",
            author: "Geek-3"
          }){
            ok
            post{
              id
              title
              description
              publishDate
            }
          }
        # Response 
        {
          "data": {
            "createPost": {
              "ok": true,
              "post": {
                "id": "3",
                "title": "My post - 2",
                "description": "My second post on Django",
                "publishDate": "2021-02-06T18:32:55.033466+00:00"
              }
            }
          }
        }
        
        }
    ```
2. ##### Implement a updatePost($id) mutation which will update a Post attributes by $id 
      ```json5
        # GraphQL Query 
        mutation updatepost {
          updatePost(
            id:2,
            input:{
              title: "My post - 2 ",
                author: "jebas",
                description : "Second Post updated"
            }
          ){
            ok
            post{
              id
              title
              description
              commentSet{
                id
                text
              }
            }
          }}
        
        # Response 
        {
          "data": {
            "updatePost": {
              "ok": true,
              "post": {
                "id": "2",
                "title": "My post - 2 ",
                "description": "Second Post updated",
                "commentSet": []
              }
            }
          }
        }
      ```
3. ##### Implement a createComment() mutation which will create a Comment object with attributes {post (the blogpost object), text, author (just the name as a TextField)}
    ```json5
       # GraphQL Query 
        mutation createcomment{
          createComment(input:{
            text: "Post 2 is good",   
            author: "Jeba",
            postId:2,
            
            
          }){
            ok
            comment{
              text
              commentedOn
            }
          }
        }
        
        # Response 
        {
          "data": {
            "createComment": {
              "ok": true,
              "comment": {
                "text": "Post 2 is good",
                "commentedOn": "2021-02-06T18:36:28.852938+00:00"
              }
            }
          }
        }
      ```
4. ##### Implement a deleteComment($id) mutation to delete the given Comment by $id.
    ```json5
      # GraphQL Query 
      mutation deletecomment{
          deleteComment (id:2)
          {
            ok
          }
        }
        # Response 
        {
          "data": {
            "deleteComment": {
              "ok": true
            }
          }
        }
      ```
5. ##### Implement a post() query to list all the posts
    ```json5
       # GraphQL Query 
        query getposts {
         posts{
          id
          title
          publishDate
          description
          commentSet{
            id
            text
            
          }
        }
        }
        
        # Response 
        {
          "data": {
            "posts": [
              {
                "id": "3",
                "title": "My post - 3 ",
                "publishDate": "2021-02-06T18:32:55.033466+00:00",
                "description": "My thrid post",
                "commentSet": []
              },
              {
                "id": "2",
                "title": "My post - 2 ",
                "publishDate": "2021-02-06T18:30:30.642859+00:00",
                "description": "Second Post updated",
                "commentSet": []
              },
              {
                "id": "1",
                "title": "My post - 1 ",
                "publishDate": "2021-02-06T18:28:31.580932+00:00",
                "description": "My first post on Django ",
                "commentSet": [
                  {
                    "id": "1",
                    "text": "Post -1 looks cools"
                  }
                ]
              }
            ]
          }
        }
      ```
6. ##### Implement a post($id) query to get details of a post and all its comments
    ```json5
     # GraphQL Query 
     query getpostbyid{
          post(id:1){
            id
            title
            commentSet{
              text
            }
          }
        }
         # Response 
        {
          "data": {
            "post": {
              "id": "1",
              "title": "My post - 1 ",
              "commentSet": [
                {
                  "text": "Post -1 looks cools"
                }
              ]
            }
          }
        }
      ```

