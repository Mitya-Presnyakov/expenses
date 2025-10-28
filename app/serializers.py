from rest_framework import serializers

from app.models import Category, Expense


class CategoryReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ["creator"]


class CategoryWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class CategoryForExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class ExpenseReadSerializer(serializers.ModelSerializer):
    categories = CategoryForExpenseSerializer(many=True, read_only=True)

    class Meta:
        model = Expense
        fields = [
            "id",
            "value",
            "spent_at",
            "description",
            "created_at",
            "updated_at",
            "categories",
        ]


class ExpenseWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ["value", "spent_at", "description", "categories"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get("request")
        queryset = Category.objects.filter(creator=request.user)
        self.fields["categories"].child_relation.queryset = queryset
