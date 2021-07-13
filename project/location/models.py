from django.db import models


class Province(models.Model):
    name = models.CharField(max_length=50, null=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def to_json(self):
        data = {
            "id": self.id,
            "name": self.name,
        }
        return data


class District(models.Model):
    name = models.CharField(max_length=50, null=False)
    province_id = models.ForeignKey(Province, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def to_json(self):
        data = {"id": self.id, "name": self.name, "province_id": self.province_id.id}
        return data
