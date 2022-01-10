from django.contrib.auth import get_user_model
from django.test import TestCase


class UsersManagersTests(TestCase):
    def test_create_user(self):
        user_model = get_user_model()
        user = user_model.objects.create_user(
            email='name@example.com',
            password='foo',
            cpf='123456789',
            first_name='name',
            last_name='last name'
        )
        self.assertEqual(user.email, 'name@example.com')
        self.assertEqual(user.first_name, 'name')
        self.assertEqual(user.last_name, 'last name')
        self.assertEqual(user.cpf, '123456789')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_trusty)
        self.assertFalse(user.is_superuser)

        with self.assertRaises(TypeError):
            user_model.objects.create_user(
                email='name@example.com',
                password='foo'
            )
        with self.assertRaises(ValueError):
            user_model.objects.create_user(
                email='',
                password='',
                cpf='',
                first_name='',
                last_name=''
            )

    def test_create_superuser(self):
        user_model = get_user_model()
        user = user_model.objects.create_superuser(
            email='name@example.com',
            password='foo',
            cpf='123456789',
            first_name='name',
            last_name='last name'
        )
        self.assertEqual(user.email, 'name@example.com')
        self.assertEqual(user.cpf, '123456789')
        self.assertEqual(user.first_name, 'name')
        self.assertEqual(user.last_name, 'last name')
        self.assertFalse(user.is_trusty)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_active)

        with self.assertRaises(TypeError):
            user_model.objects.create_superuser(
                email='name@example.com',
                password='foo'
            )
        with self.assertRaises(ValueError):
            user_model.objects.create_superuser(
                email='',
                password='',
                cpf='',
                first_name='',
                last_name=''
            )
