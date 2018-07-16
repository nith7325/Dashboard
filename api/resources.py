from tastypie.resources import ModelResource
from api.models import Album
from tastypie.authorization import Authorization

class AlbumResource(ModelResource):
    class Meta:
        queryset = Album.objects.all()
        resource_name = 'album'
        authorization = Authorization()
        fields = ['date', 'market', 'alert', 'alert_details']

