from django.shortcuts import render

def DeckView(request):
    if request.method == "POST":
        deck = Deck()
        deck.title = request.POST['title']
        deck.save()
        for pair in request.POST'cards']:
            tmp = Card()
            tmp.front = pair[0]
            tmp.back = pair[1]
            tmp.deck = deck.id
            tmp.save()
        return
    if request.method = "DELETE":
        params = QueryDict(request.body)
        tmp = get_object_or_404(Deck, id=params['id'])
        tmp.delete()
        return
    if request.method = "GET":
        cards = Cards.objects.filter(deck=request.GET['id']).values('front','back')
        return cards
    if request.method = "PATCH":
        params = QueryDict(request.body)
        tmp = get_object_or_404(Deck, id=parmas['id'])
        for pair in params['cards']:
            tmp = Card()
            tmp.front = pair[0]
            tmp.back = pair[1]
            tmp.deck = deck.id
            tmp.save()
        return 


 

# Create your views here.
