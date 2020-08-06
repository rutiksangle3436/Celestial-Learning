from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
# Create your views here.

#curl -X POST -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTk2MzYxMzg5LCJqdGkiOiJmNjQzMjUyN2MwMGU0YThiYmYwZGE2N2M3NjFkYzA2OCIsInVzZXJfaWQiOjEwfQ.FvYv7drBdsQMJaXwA02TKe2ZQXt0Eq7fa549J9cGW5Y" http://127.0.0.1:8000/api/token/test/
class TestToken(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def post(self, request):
        username = request.user
        content = {'Username': str(username)}
        return Response(content)