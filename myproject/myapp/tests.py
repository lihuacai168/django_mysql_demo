from django.test import TestCase

from .models import OptimisticLockModel, PessimisticLockModel


class OptimisticLockModelTestCase(TestCase):
    def test_version_increment(self):
        my_model = OptimisticLockModel.objects.create(name="test", value=1)
        initial_version = my_model.version

        # Ensure the version field is incremented on save
        my_model.save()
        self.assertEqual(my_model.version, initial_version + 1)

    # def test_version_conflict(self):
    #     my_model_1 = OptimisticLockModel.objects.create(name="test", value=1)
    #     my_model_2 = OptimisticLockModel.objects.get(name="test")
    #
    #     # Ensure that a version conflict raises an exception
    #     my_model_1.value = 2
    #     my_model_1.save()
    #
    #     my_model_2.value = 3
    #     with self.assertRaises(ExpectedlyVersionError):
    #         my_model_2.save()


class MyModelTestCase(TestCase):
    def test_update_value(self):
        my_model = PessimisticLockModel.objects.create(name="test", value=1)
        PessimisticLockModel.update_value(name="test", value=2)

        # Ensure the value is updated
        my_model.refresh_from_db()
        self.assertEqual(my_model.value, 2)

    # def test_select_for_update(self):
    #     my_model_1 = PessimisticLockModel.objects.create(name="test", value=1)
    #     my_model_2 = PessimisticLockModel.objects.get(name="test")
    #
    #     with transaction.atomic():
    #         # Ensure that the second transaction is blocked until the first one is finished
    #         my_model_1.update_value(name="test", value=2)
    #
    #         with self.assertRaises(Exception):
    #             my_model_2.value = 3
    #             my_model_2.refresh_from_db()
    #             my_model_2.save()
