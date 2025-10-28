from django.contrib import admin

from .models import Category, Expense


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "creator")


class CategoryInline(admin.TabularInline):
    model = Expense.categories.through


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("id", "value", "creator", "description")
    inlines = [CategoryInline]
