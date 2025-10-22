from django.test import TestCase
from django.urls import reverse
from .models import Note


class NoteModelTest(TestCase):
    """Tests for the Note model, checking for the expected title
    and content."""

    def setUp(self):
        # Create Note object for testing
        Note.objects.create(title='Test Note', content='This is a test note.')

    def test_note_has_title(self):
        note = Note.objects.get(id=1)
        self.assertEqual(note.title, 'Test Note')

    def test_note_has_content(self):
        note = Note.objects.get(id=1)
        self.assertEqual(note.content, 'This is a test note.')


class NoteViewTest(TestCase):
    """Tests for views related to notes, checking if a note is
    displayed and if it has the right details."""

    def setUp(self):
        Note.objects.create(title='Test Note', content='This is a test note.')

    def test_note_list_view(self):
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)

    def test_note_detail_view(self):
        note = Note.objects.get(id=1)
        response = self.client.get(reverse('note_detail',
                                           args=[str(note.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')
        self.assertContains(response, 'This is a test note.')


class NoteUseCase(TestCase):
    """Tests the remaining use cases, checking if an updated note has
    the expected details, and if a note is removed after deletion."""

    def setUp(self):
        # Create Note object for testing
        Note.objects.create(title='Test Note', content='This is a test note.')

    def test_update_note(self):
        note = Note.objects.get(id=1)
        # Update note details
        note.content = "This is updated."
        note.save()
        # Get updated note and check details
        note_updated = Note.objects.get(id=1)
        self.assertEqual(note_updated.content, 'This is updated.')

    def test_delete_note(self):
        note = Note.objects.get(id=1)
        note.delete()
        response = self.client.get(reverse('note_list'))
        self.assertNotContains(response, 'Test Note')
