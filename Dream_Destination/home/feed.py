from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse
from product.models import TravellPlace


class latest_feed(Feed):
    title="free travel"
    link="/drcomments/"
    description="when you want a trip, vist our website ;enjoy your trip in dream destination"
    def items(self):
        return TravellPlace.objects.order_by("date")[:3]
    def item_title(self,place):
        return place.name
    def item_description(self,place):
        return truncatewords(place.des,10)
    def item_link(self,place):
        return reverse("homepage")   
                

