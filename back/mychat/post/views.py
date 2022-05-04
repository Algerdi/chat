from rest_framework import generics, status, permissions
from .serializers import PostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Post


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# class PostCreate(APIView):
#     def post(self, request):
#         serializers = PostSerializer(data=request.data)
#         serializers.is_valid(raise_exception=True)
#         serializers.save()
#         if serializers:
#             return Response(status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializers.data)

class PostCreate(generics.CreateAPIView):
    
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)