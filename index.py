from flask import Blueprint, render_template
from module.api import Api

import random

main_routes = Blueprint("main_routes", __name__)
api = Api()

category = [
    "highfive",
    "happy",
    "sleep",
    "handhold",
    "laugh",
    "bite",
    "poke",
    "tickle",
    "kiss",
    "wave",
    "thumbsup",
    "stare",
    "cuddle",
    "smile",
    "baka",
    "blush",
    "nom",
    "think",
    "pout",
    "facepalm",
    "wink",
    "shoot",
    "smug",
    "nope",
    "cry",
    "pat",
    "nod",
    "punch",
    "dance",
    "feed",
    "shrug",
    "bored",
    "kick",
    "hug",
    "yeet",
    "slap",
    "neko",
    "husbando",
    "kitsune",
    "waifu",
]


@main_routes.route("/")
def home_page():
    title = "Home"
    return render_template(
        "page/home.html", title=title
    )

@main_routes.route("/select_category")
def select_category_page():
    title = "Select Category"
    categorys = category
    return render_template(
        "page/select_category.html", title=title, category=categorys
    )

@main_routes.route("/select_category/highfive")
def highfive_page():
    urls = api.highfive()
    title = "highfive"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/happy")
def happy_page():
    urls = api.happy()
    title = "happy"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/sleep")
def sleep_page():
    urls = api.sleep()
    title = "sleep"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/handhold")
def handhold_page():
    urls = api.handhold()
    title = "handhold"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/laugh")
def laugh_page():
    urls = api.laugh()
    title = "laugh"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/bite")
def bite_page():
    urls = api.bite()
    title = "bite"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/poke")
def poke_page():
    urls = api.poke()
    title = "poke"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/tickle")
def tickle_page():
    urls = api.tickle()
    title = "tickle"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/kiss")
def kiss_page():
    urls = api.kiss()
    title = "kiss"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/wave")
def wave_page():
    urls = api.wave()
    title = "wave"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/thumbsup")
def thumbsup_page():
    urls = api.thumbsup()
    title = "thumbsup"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/stare")
def stare_page():
    urls = api.stare()
    title = "stare"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/cuddle")
def cuddle_page():
    urls = api.cuddle()
    title = "cuddle"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/smile")
def smile_page():
    urls = api.smile()
    title = "smile"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/baka")
def baka_page():
    urls = api.baka()
    title = "baka"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/blush")
def blush_page():
    urls = api.blush()
    title = "blush"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/nom")
def nom_page():
    urls = api.nom()
    title = "nom"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/think")
def think_page():
    urls = api.think()
    title = "think"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/pout")
def pout_page():
    urls = api.pout()
    title = "pout"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/facepalm")
def facepalm_page():
    urls = api.facepalm()
    title = "facepalm"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/wink")
def wink_page():
    urls = api.wink()
    title = "wink"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/shoot")
def shoot_page():
    urls = api.shoot()
    title = "shoot"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/smug")
def smug_page():
    urls = api.smug()
    title = "smug"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/nope")
def nope_page():
    urls = api.nope()
    title = "nope"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/cry")
def cry_page():
    urls = api.cry()
    title = "cry"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/pat")
def pat_page():
    urls = api.pat()
    title = "pat"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/nod")
def nod_page():
    urls = api.nod()
    title = "nod"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/punch")
def punch_page():
    urls = api.punch()
    title = "punch"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/dance")
def dance_page():
    urls = api.dance()
    title = "dance"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/feed")
def feed_page():
    urls = api.feed()
    title = "feed"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/shrug")
def shrug_page():
    urls = api.shrug()
    title = "shrug"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/bored")
def bored_page():
    urls = api.bored()
    title = "bored"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/kick")
def kick_page():
    urls = api.kick()
    title = "kick"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/hug")
def hug_page():
    urls = api.hug()
    title = "hug"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/yeet")
def yeet_page():
    urls = api.yeet()
    title = "yeet"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/slap")
def slap_page():
    urls = api.slap()
    title = "slap"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/neko")
def neko_page():
    urls = api.neko()
    title = "neko"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/husbando")
def husbando_page():
    urls = api.husbando()
    title = "husbando"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/kitsune")
def kitsune_page():
    urls = api.kitsune()
    title = "kitsune"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )


@main_routes.route("/select_category/waifu")
def waifu_page():
    urls = api.waifu()
    title = "waifu"
    random_category = random.sample(category, 5)
    return render_template(
        "page/page.html", urls=urls, title=title, random_category=random_category
    )
