from djongo import models

# Create your models here.
class Book(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=255)
    content = models.TextField()
    
    @property
    def pk(self):
        return self._id
    
    def __str__(self):
        return self.name