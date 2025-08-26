from django.urls import path
from .views import (
    note_list,
    note_detail,
    note_create,
    note_update,
    note_delete,
)

# URL patterns
urlpatterns = [
    # For displaying list of all notes
    path("", note_list, name="note_list"),

    # For displaying the details of one note
    path("note/<int:pk>/", note_detail, name="note_detail"),

    # For creating a new note
    path("note/new", note_create, name="note_create"),

    # For updating an existing note
    path("note/<int:pk>/edit/", note_update, name="note_update"),

    # For deleting an existing not
    path("note/<int:pk>/delete/", note_delete, name="note_delete"),
]
