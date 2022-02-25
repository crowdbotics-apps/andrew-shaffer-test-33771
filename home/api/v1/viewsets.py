from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import permissions
from home.models import App, Plan, Subscription
from .permissions import IsOwnerOrReadOnly

from home.api.v1.serializers import (
    SignupSerializer,
    UserSerializer,
    AppSerializer,
    PlanSerializer,
    SubscriptionSerializer
)


class SignupViewSet(ModelViewSet):
    serializer_class = SignupSerializer
    http_method_names = ["post"]


class LoginViewSet(ViewSet):
    """Based on rest_framework.authtoken.views.ObtainAuthToken"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(user)
        return Response({"token": token.key, "user": user_serializer.data})


class AppViewSet(ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # def get_queryset(self):
    #     return App.objects.filter(user=self.request.user)

class PlanViewSet(ModelViewSet):
    queryset = Plan.objects.all().order_by('price')
    serializer_class = PlanSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'post']

class SubscriptionViewSet(ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly]
    http_method_names = ['get', 'post', 'put', 'patch']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
