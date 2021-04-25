from django.shortcuts import render, redirect
import random
from datetime import datetime


# Create your views here.
def index(request):
    if 'activity' not in request.session and 'gold_sum' not in request.session:
        request.session['activity'] = []
        request.session['gold_sum'] = 0
    context = {
		"gold_amount": request.session["gold_sum"],
		"activity_list": request.session["activity"],
	}
    return render(request, 'index.html', context)

def process_money(request, location):
    if request.method == "GET":
        dateTimeObj = datetime.now()
        timestampStr = dateTimeObj.strftime("%Y/%m/%d %I:%M:%S %p")
        if location == 'farm':
            rand_gold = round(10 + random.random() * 10)
        elif location == 'cave':
            rand_gold = round(5 + random.random() * 5)
        elif location == 'house':
            rand_gold = round(2 + random.random() * 3)
        else:
            rand_gold = round(random.random() * 50)
            if round(random.random()):
                request.session["gold_sum"] += rand_gold
                request.session["activity"] += [f"Entered the {location} and gained {rand_gold} golds. Hooray! ({timestampStr})"]
                return redirect("/")
            else:
                request.session["gold_sum"] -= rand_gold
                request.session["activity"] += [f"Entered the {location} and lost {rand_gold} golds. Ouch... ({timestampStr})"]
                return redirect("/")
        request.session["gold_sum"] += rand_gold
        request.session["activity"] += [f"Earned {rand_gold} golds from the {location} ({timestampStr})"]
        return redirect("/")

def reset(request):
    request.session.flush()
    return redirect("/")
