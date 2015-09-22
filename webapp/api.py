from tastypie.resources import ModelResource
from customer_care.models import User

__author__ = 'Otto'


class EntryResource(ModelResource):
    class Meta:
        queryset = User.objects.all()