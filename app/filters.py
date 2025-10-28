import django_filters

from app.models import Category, Expense


class ExpenseFilter(django_filters.FilterSet):
    min_spent_at = django_filters.DateTimeFilter(
        field_name="spent_at", lookup_expr="gte"
    )
    max_spent_at = django_filters.DateTimeFilter(
        field_name="spent_at", lookup_expr="lte"
    )

    min_value = django_filters.NumberFilter(
        field_name="value", lookup_expr="gte"
    )
    max_value = django_filters.NumberFilter(
        field_name="value", lookup_expr="lte"
    )

    categories = django_filters.ModelMultipleChoiceFilter(
        field_name="categories"
    )

    class Meta:
        model = Expense
        fields = ["spent_at", "value", "categories"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = kwargs.get("request")
        queryset = Category.objects.filter(creator=request.user)
        self.filters["categories"].queryset = queryset
