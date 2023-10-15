import requests, random

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
application = ApplicationBuilder().token(TOKEN).build()

# /start to generate a list of available commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hi! \n\n/dog - generate a random dog pic \n\n/quote - generate a random quote \n\nSend 'Random:' followed by a list of choices seperated by commas to randomly generate a choice \nE.g. 'Random: a, b, c'")

async def dog(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=((requests.get("https://dog.ceo/api/breeds/image/random")).json())["message"])

async def choose(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (update.message.text).split(':')
    if msg[0] == "random" or msg[0] == "Random":
        msg = msg[1].split(',')
        await context.bot.send_message(chat_id=update.effective_chat.id, text = random.choice(msg))

async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    quotes = [' Life is about making an impact, not making an income. --Kevin Kruse',
    'Whatever the mind of man can conceive and believe, it can achieve. –Napoleon Hill',
    'Strive not to be a success, but rather to be of value. –Albert Einstein',
    'Two roads diverged in a wood, and I—I took the one less traveled by, And that has made all the difference.  –Robert Frost',
    'I attribute my success to this: I never gave or took any excuse. –Florence Nightingale',
    'You miss 100% of the shots you don’t take. –Wayne Gretzky',
    'The most difficult thing is the decision to act, the rest is merely tenacity. –Amelia Earhart',
    'Definiteness of purpose is the starting point of all achievement. –W. Clement Stone',
    'Life is not about getting and having, it is about giving and being. –Kevin Kruse',
    'Life is what happens to you while you are busy making other plans. –John Lennon',
    'We become what we think about. –Earl Nightingale',
    'The mind is everything. What you think you become.  –Buddha',
    'The best time to plant a tree was 20 years ago. The second best time is now. –Chinese Proverb',
    'Eighty percent of success is showing up. –Woody Allen',
    'Your time is limited, so don’t waste it living someone else’s life. –Steve Jobs',
    'Winning isn’t everything, but wanting to win is. –Vince Lombardi',
    '23. I am not a product of my circumstances. I am a product of my decisions. –Stephen Covey',
    'You can never cross the ocean until you have the courage to lose sight of the shore. –Christopher Columbus',
    'If you hear a voice within you say “you cannot paint,” then by all means paint and that voice will be silenced. –Vincent Van Gogh',
    'Ask and it will be given to you; search, and you will find; knock and the door will be opened for you. –Jesus',
    'When I let go of what I am, I become what I might be. –Lao Tzu',
    'You can’t fall if you don’t climb.  But there’s no joy in living your whole life on the ground. –Unknown',
    'Limitations live only in our minds.  But if we use our imaginations, our possibilities become limitless. –Jamie Paolinetti',
    'It does not matter how slowly you go as long as you do not stop. –Confucius',
    'The best and most beautiful things in the world cannot be seen or even touched – they must be felt with the heart. —Helen Keller',
    'You must be the change you wish to see in the world. —Mahatma Gandhi',
    'The greatest glory in living lies not in never falling, but in rising every time we fall. —Nelson Mandela',
    'Friendship is the only cement that will ever hold the world together. —Woodrow Wilson',
    'Don’t let yesterday take up too much of today. — Will Rogers',
    'Either you run the day or the day runs you. — Jim Rohn',
    'Alone we can do so little, together we can do so much. — Helen Keller',
    'Friends are the family we choose. — Jennifer Aniston',
    'Just keep swimming — Dory, Finding Nemo',
    'Never regret anything that made you smile. ~ Mark Twain',
    'Rise above the storm and you will find the sunshine. ~ Mario Fernández',
    'Be not afraid of going slowly, be afraid only of standing still.” ~ Chinese Proverb',
    'The most wasted of days is one without laughter. ~E.E. Cummings',
    'In the middle of difficulty lies opportunity. ~ Albert Einstein',
    'The journey of a thousand miles begins with one step. ~ Lao Tzu',
    'Everything is hard before it is easy. ― Goethe J.W.',
    'Try to be a rainbow in someone’s cloud. —Maya Angelou',
    'Keep a little fire burning; however small, however hidden. ―Cormac McCarthy',
    'Turn your wounds into wisdom. — Oprah Winfrey',
    'Life is like riding a bicycle. To keep your balance, you must keep moving. — Albert Einstein']
    length = len(quotes)
    await context.bot.send_message(chat_id=update.effective_chat.id, text = quotes[random.randint(0, length-1)])

if __name__ == '__main__':
    start_handler = CommandHandler('start', start)
    dog_handler = CommandHandler('dog', dog)
    choose_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), choose)
    quote_handler = CommandHandler('quote', quote)

    application.add_handler(start_handler)
    application.add_handler(dog_handler)
    application.add_handler(choose_handler)
    application.add_handler(quote_handler)
    
    application.run_polling()

