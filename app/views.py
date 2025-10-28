from rest_framework import status, viewsets
from rest_framework.response import Response

from app.filters import ExpenseFilter
from app.models import Category, Expense
from app.serializers import (
    CategoryReadSerializer,
    CategoryWriteSerializer,
    ExpenseReadSerializer,
    ExpenseWriteSerializer,
)


class CategoryViewSet(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        write_serializer = CategoryWriteSerializer(
            data=request.data, context={"request": request}
        )
        write_serializer.is_valid(raise_exception=True)
        expense = write_serializer.save(creator=request.user)

        response_serializer = CategoryReadSerializer(
            expense, context={"request": request}
        )
        return Response(
            response_serializer.data, status=status.HTTP_201_CREATED
        )

    def get_queryset(self):
        return Category.objects.filter(creator=self.request.user)

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return CategoryReadSerializer
        return CategoryWriteSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        write_serializer = self.get_serializer(data=request.data)
        write_serializer.is_valid(raise_exception=True)
        expense = write_serializer.save(creator=request.user)

        response_serializer = ExpenseReadSerializer(
            expense, context={"request": request}
        )
        return Response(
            response_serializer.data,
            status=status.HTTP_201_CREATED,
        )

    def get_queryset(self):
        return Expense.objects.filter(creator=self.request.user)

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ExpenseReadSerializer
        return ExpenseWriteSerializer

    filterset_class = ExpenseFilter
