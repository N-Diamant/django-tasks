from rest_framework.request import Request
from rest_framework.response import Response#with this , we can return errors or status code and customize the response
from rest_framework import status
from rest_framework.decorators import api_view,APIView
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404






@api_view(http_method_names=["GET","POST"])
def homepage(request:Request):

    if request.method == "POST":
        data = request.data
        response = {"message":"hello world","data":data}
        return Response(data=response,status=status.HTTP_201_CREATED)

    response = {"message":"hello world"}
    return Response(data=response,status=status.HTTP_200_OK)



##########these are class based views
class PostListCreateView(APIView):
    # a view for creating and listing posts
    serializer_class = PostSerializer
    def get(self,request:Request,*args,**kwargs):
        posts=Post.objects.all()

        serializer=self.serializer_class(instance=posts,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def post(self,request:Request,*args,**kwargs):
        data=request.data

        serializer=self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            response={
                "message":"Post Created",
                "data":serializer.data
            }
            return Response(data=response,status=status.HTTP_200_OK)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class PostRetrieveUpdateDeleteView(APIView):
    serializer_class=PostSerializer

    def get(self,request:Request,post_id:int):
        post =get_object_or_404(Post,pk=post_id)
        serializer = self.serializer_class(instance=post)

        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def put(self,request:Request,post_id:int):
      post =get_object_or_404(Post,pk=post_id)
      data=request.data
      serializer = self.serializer_class(instance=post,data=data)

      if serializer.is_valid():
        serializer.save()
        response={
            "message":"Post updated ",
            "data":serializer.data
        }
        return Response(data=response,status=status.HTTP_200_OK)
      else:
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)



    def delete(self,request:Request,post_id:int):
        post=get_object_or_404(Post,pk=post_id)

        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT )



###### these are function based views
# @api_view(http_method_names=["GET"])
# def post_detail(request:Request,post_id=int):
#     post = get_object_or_404(Post,pk=post_id)
#     serializer = PostSerializer(instance=post)
#     response={
#         "message":"post",
#         "data":serializer.data

#     }

#     return Response(data=response,status=status.HTTP_200_OK)




# @api_view(http_method_names=["PUT"])
# def update_post(request:Request,post_id=int):
#     post = get_object_or_404(Post,pk=post_id)
#     data = request.data
#     serializer =PostSerializer(instance=post,data=data)

#     if serializer.is_valid():
#         serializer.save()

#         response={
#             "message":"post updated successfully",
#             "data":serializer.data
#         }
#         return Response(data=response,status=status.HTTP_200_OK)

#     return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# #the get_object_or_404 function is a shortcut used to retrieve data from the db . and if not found it returns an error

# @api_view(http_method_names=["DELETE"])
# def delete_post(request:Request,post_id=int):
#     post = get_object_or_404(Post,pk=post_id)

#     post.delete()

#     return Response(status=status.HTTP_204_NO_CONTENT)


