from djongo import models


'''COLOR_CHOICES = (
    ('green','GREEN'),
    ('blue', 'BLUE'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'),
)'''

# Create your models here.
class Book(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=255)
    content = models.TextField()
#    color = models.CharField(max_length=6, choices=COLOR_CHOICES, default='green')

    def __str__(self):
        return self.name