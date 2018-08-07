from django.db import models
"""
Class
"""

class Dojo(models.Model):
    Name = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    State = models.CharField(max_length=2)
    desc = models.TextField()

    def __repr__(self):
        return "<Dojo: {}|{} {} {}>".format(self.id, self.Name, self.City, self.State)


class Ninja(models.Model):
    dojo = models.ForeignKey(Dojo, on_delete=models.CASCADE, related_name="ninjas")
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)

    def __repr__(self):
        return "<Ninja: {}|{} {}>".format(self.id, self.fname, self.lname)

# from apps.dojoninjas.models import Dojo
# from apps.dojoninjas.models import Dojo

## loc1 = Dojo.objects.get(id=1) this adds it to the first location so on and so forth
#  ninja = Ninja.objects.create(fname="Johnny", lname="Schmuck", dojo=loc1) this adds it to the first location