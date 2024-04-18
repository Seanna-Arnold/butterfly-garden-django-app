from django.db import models
from django.urls import reverse
from datetime import date

CYCLES = (
    ('E', 'Eggs Layed'),
    ('H', 'Eggs Hatched'),
    ('C', 'Chrysalis(pupa)'),
    ('A', 'Adulthood')
)

class Flora(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('floras_detail', kwargs={'pk': self.id})


# Create your models here.
class Butterfly(models.Model):
  name = models.CharField(max_length=100)
  scientific = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  size = models.CharField(max_length=100)
  floras = models.ManyToManyField(Flora)

  # Changing this instance method
  # does not impact the database, therefore
  # no makemigrations is necessary
  def __str__(self):
    return f'{self.name} ({self.id})'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'butterfly_id': self.id})
    
  def cycle_for_today(self):
    return self.cycle_set.filter(date=date.today()).count() >= len(CYCLES)
  
class Cycle(models.Model):
  date = models.DateField('cycle date')
  cycle = models.CharField(max_length=1, choices=CYCLES, default=CYCLES[0][0])
  butterfly = models.ForeignKey(Butterfly, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_cycle_display()} on {self.date}"

  class Meta:
    ordering = ['-date']
