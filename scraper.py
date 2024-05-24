import telebot
from bs4 import BeautifulSoup
import requests

# تعريف الوظيفة للحصول على محتوى الموقع
def get_website_content(url):
    re = requests.get(url)
    soup = BeautifulSoup(re.text, 'html.parser')

    story = soup.find_all("div", {'class': 'episodes-list-content'})
    z = story[0].find_all("div", {"class", "row display-flex"})
    card = z[0].find_all("div", {
      "col-lg-3 col-md-3 col-sm-4 col-xs-12 col-no-padding col-mobile-no-padding"
  })
    arr =[]
    episodes = {}
    for i in range(15):
        link_watch = str(card[i].find_all("a")[0].get('href'))
        profile_anime = str(card[i].find_all("a")[2].get('href'))
        anime_name_ep = str(card[i].find_all("a")[2].text)
        src_img = str(card[i].find_all('img')[0].get('src'))
        alt_img = str(card[i].find_all('img')[0].get('alt'))
        episodes[anime_name_ep ] = link_watch

    return episodes

# إنشاء متغير لرمز الوصول
API_TOKEN = '6918266799:AAFDEh4MUUenTotLULsCxjNrfY84AkF50Vc'

# إنشاء البوت
bot = telebot.TeleBot(API_TOKEN)

# تعريف وظيفة للرد على الأمر /start
@bot.message_handler(commands=['start'])
def send_website_content(message):
    url = "https://witanime.quest/"
    content = get_website_content(url)
    txt = ''
    for key, value in content.items():
        txt += '[ اسم الحلقة  :' +key+ " \nرابط الحلقة : " + value+'  ] \n'
    
    bot.reply_to(message, txt,disable_web_page_preview=True)

# بدء البوت
bot.polling()
