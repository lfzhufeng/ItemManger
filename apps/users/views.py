from rest_framework.views import APIView
from utils.token import CustomTokenObtainPairSerializer
from .modules.serializer import UserSerializer
from utils.response import APIResponse

class CustomTokenObtainPairView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = CustomTokenObtainPairSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return APIResponse(code=0, data=serializer.validated_data, message='Success')


class RegisterView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return APIResponse(code=0, message='Success')



