from django.urls import path, include
from rest_framework.routers import DefaultRouter

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
    AppViewSet,
    PlanViewSet,
    SubscriptionViewSet
)

router = DefaultRouter()
# router.register("signup", SignupViewSet, basename="signup")
# router.register("login", LoginViewSet, basename="login")
router.register("apps", AppViewSet)
router.register("plans", PlanViewSet)
router.register("subscriptions", SubscriptionViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
