from django.shortcuts import render, redirect
import random
from datetime import datetime


# Create your views here.
def index(request):
    if 'activity' not in request.session and 'gold_sum' not in request.session:
        request.session['activity'] = []
        request.session['gold_sum'] = 0
    # print(request.session["color"])
    context = {
		"gold_amount": request.session["gold_sum"],
		"activity_list": request.session["activity"],
	}
    return render(request, 'index.html', context)

def process_money(request):
    if request.method == "POST":
        dateTimeObj = datetime.now()
        timestampStr = dateTimeObj.strftime("%Y/%m/%d %I:%M %p")
        hidden_input_value = request.POST["gold"]
        if hidden_input_value == '1':
            rand_gold = round(10 + random.random() * 10)
            request.session["gold_sum"] += rand_gold
            request.session["activity"] += [f"Earned {rand_gold} golds from the farm ({timestampStr})"]
        if hidden_input_value == '2':
            rand_gold = round(5 + random.random() * 5)
            request.session["gold_sum"] += rand_gold
            request.session["activity"] += [f"Earned {rand_gold} golds from the cave ({timestampStr})"]
        if hidden_input_value == '3':
            rand_gold = round(2 + random.random() * 3)
            request.session["gold_sum"] += rand_gold
            request.session["activity"] += [f"Earned {rand_gold} golds from the house ({timestampStr})"]
        if hidden_input_value == '4':
            rand_gold = round(random.random() * 50)
            if round(random.random()):
                request.session["gold_sum"] += rand_gold
                request.session["activity"] += [f"Entered the casino and gained {rand_gold} golds. Hooray! ({timestampStr})"]
            else:
                request.session["gold_sum"] -= rand_gold
                request.session["activity"] += [f"Entered the casino and lost {rand_gold} golds. Ouch... ({timestampStr})"]
        return redirect("/")

def reset(request):
    # request.session["gold_sum"] = 0
    # request.session["activity"] = []
    # request.session["color"] = ""
    request.session.flush()
    return redirect("/")
