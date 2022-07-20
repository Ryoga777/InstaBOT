from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
import time
import schedule

user = "" #inserisci il tuo username tra le virgolette
pwd = "" #inserisci la tua password tra le virgolette

set_workspace(Path=None)

instagrammer = InstaPy(user, pwd)

def automation():
    with smart_run(instagrammer):
        instagrammer.set_do_comment(enabled = True, percentage = 20)
        instagrammer.set_comment(["Hi! Would you follow me? I'd be honored!"])
        instagrammer.like_by_tags(["cosplay", "instacosplay", "cosplayersofinstagram"], amount=100, media = "Photo")
        instagrammer.set_do_follow(enabled = True, percentage = 25, times = 2)

def get_followers():
    with smart_run(instagrammer):
        #inserisci lo username di un utente a scelta da cui prendere i followers
        instagrammer.grab_followers(username="", live_match=True, store_locally=True, amount="full")

schedule.every().monday.at("12:00").do(get_followers)
schedule.every().wednesday.at("10:00").do(automation)

while(True):
    schedule.run_pending()
    time.sleep(10)