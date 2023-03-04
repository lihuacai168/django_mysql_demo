# Create your models here.
from django.core.exceptions import ObjectDoesNotExist
from django.db import models, transaction


class ExpectedlyVersionError(Exception):
    pass


class OptimisticLockModel(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField()
    version = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # 如果没有版本号，就创建一个
        if not self.version:
            self.version = 1
        # 否则递增版本号
        else:
            self.version += 1

        # 保存时检查版本号
        try:
            super().save(*args, **kwargs)
        except ObjectDoesNotExist:
            raise ExpectedlyVersionError("version conflict")


class PessimisticLockModel(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField()

    @classmethod
    @transaction.atomic
    def update_value(cls, name, value):
        obj = cls.objects.select_for_update().get(name=name)
        obj.value = value
        obj.save()
