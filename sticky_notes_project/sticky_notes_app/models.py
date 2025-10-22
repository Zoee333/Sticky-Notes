from django.db import models

# Create your models here.
""" Design and define the model for your sticky notes application,
    including fields for the title and content of each note"""


class Note(models.Model):
    """Model representing a sticky note.
    Fields:
    - title: CharField for note title, max length 255
    - content: TextField for note content
    - created_at: DateTimeField for note creation date and time
    Methods:
    - __str__: Returns a string representation and shows the title
    :param models.Model: Django's base model class."""

    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
