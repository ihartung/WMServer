from django.shortcuts import render
from main.models import Card, Deck
from django.http import HttpResponse, JsonResponse
from django.core import serializers

def DecksView(request):
    decks = Deck.objects.all().only('title')
    data = serializers.serialize('json', decks)
    return HttpResponse(data, content_type='application/json')


def DeckView(request, index=0):
    if request.method == "POST":
        deck = Deck()
        deck.title = request.POST['title']
        deck.save()
        content = request.FILES['cards'].read()
        for line in content.decode('utf-8').strip().split('\n'):
            tmp = Card()
            print(line)
            pair = line.split(',')
            tmp.front = pair[0]
            tmp.back = pair[1]
            tmp.deck = deck
            tmp.save()
        return
    if request.method == "DELETE":
        params = QueryDict(request.body)
        tmp = get_object_or_404(Deck, id=index)
        tmp.delete()
        return
    if request.method == "GET":
        cards = Card.objects.filter(deck=index).values('front','back')
        card_list = list(cards);
        return JsonResponse(card_list, safe=False)
    if request.method == "PATCH":
        params = QueryDict(request.body)
        tmp = get_object_or_404(Deck, id=index)
        for pair in params['cards']:
            tmp = Card()
            tmp.front = pair[0]
            tmp.back = pair[1]
            tmp.deck = deck.id
            tmp.save()
        return 

# Create your views here.
