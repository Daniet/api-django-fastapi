from django.test import TestCase

from characters.models import Character

class CharacterModelTest(TestCase):
    def setUp(self):
        self.character = Character.objects.create(
            name="SpiderMan",
            alter_ego="Peter Parker",
            power="Throw spider web"
        ) 

    def test_character_create(self):
        self.assertEquals(self.character.name, "SpiderMan")
        self.assertEquals(self.character.alter_ego, "Peter Parker")
        self.assertEquals(self.character.power, "Throw spider web")

    def test_charcter_update(self):
        self.character.alter_ego = "Mike Morales"
        self.character.save()

        self.assertEquals(self.character.alter_ego, "Mike Morales")
