from django.http import HttpResponse
from django.template.loader import get_template
import datetime
from polls.models import Choice, Question

from googleplaces import GooglePlaces, types, lang

def get_food(request):
    YOUR_API_KEY = 'AIzaSyBznqCQUV501t1F1cM7Wasce3_W6PzVmHs'

    names = []
    ratings = []
    websites = []
    phones = []
    addresses = []
    photo_urls = []

    google_places = GooglePlaces(YOUR_API_KEY)

    query_result = google_places.nearby_search(
            location='Pasadena, California', keyword='Pizza',
            radius=1000, types=[types.TYPE_FOOD])

    if query_result.has_attributions:
        print query_result.html_attributions


    for place in query_result.places:
        # Returned places from a query are place summaries.
        names.append(place.name)

        # The following method has to make a further API call.
        place.get_details()
        ratings.append(str(place.rating))
        addresses.append(str(place.formatted_address))
        phones.append(str(place.local_phone_number))
        websites.append(str(place.website))

        c = Choice(question=Question.objects.get(id=1), distance = 'NA', rating = place.rating,
        choice_text = place.name, votes = 0)
        c.save()
        # Getting place photos
        i = 0
        # for photo in place.photos:
        #     if i<=0:
        #         # 'maxheight' or 'maxwidth' is required
        #         photo.get(maxheight=500, maxwidth=500)
        #         # MIME-type, e.g. 'image/jpeg'
        #         photo.mimetype
        #         # Image URL
        #         photo_urls.append(photo.url)
        #         # Original filename (optional)
        #         photo.filename
        #         # Raw image data
        #         photo.data
        #     i+=1


    t = get_template('api.html')
    html = t.render({
        'names': names,
        'ratings': ratings,
        'addresses': addresses,
        'phones': phones,
        'websites': websites
    })
    return HttpResponse(html)

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('base.html')
    html = t.render({
        'now': now
    })
    return HttpResponse(html)