from django.db import models
from django.core.exceptions import ValidationError


class CourseManager(models.Manager):

    def BookValidator(self, form):

        errors = []

        if len(form['cname']) < 5:
            errors.append("Name must be at least 5 characters.")
        if len(form['desc']) < 15:
            errors.append("Description must be at least 15 characters.")
        if len(errors) == 0:
            course = Course.objects.create(
                cname=form['cname'], desc=form['desc'])
            return (True, course)
        else:
            return (False, errors)


class Course(models.Model):
    cname = models.CharField(max_length=15)
    desc = models.TextField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<User {}| {} {}".format(self.id, self.cname, self.desc)

    objects = CourseManager()
