from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Define a function to handle the /start command
def start(update, context):
    update.message.reply_text('Hi! I am Xiu.')

# Define a function to handle normal messages
def respond(update, context):
    user_message = update.message.text.lower()
    
    # Define responses based on user messages
    if 'hi' in user_message:
        update.message.reply_text('Hi! ဘာလာရှာတာလည်း?')
    elif 'lee' in user_message:
        update.message.reply_text('Lee lar Kmkl')
    elif 'နေကောင်းလား' in user_message:
        update.message.reply_text("ကောင်းတယ်")
    elif 'ဘယ်သူလည်း' in user_message:
        update.message.reply_text("မင်းဖေ")
    elif 'ကောင်မလေး' in user_message:
        update.message.reply_text(" S FA ကောင်")
    elif 'ကောင်လေး' in user_message:
        update.message.reply_text(" ဘဲပစ်မ ")
    elif 'စားပြီးပြီလား' in user_message:
        update.message.reply_text(" မစားရသေးဘူး၊ကျွေးမှာလား? ")
    elif 'ဘာလုပ်' in user_message:
        update.message.reply_text("စော်နဲ့ချက်")
    elif 'ေစာ်ရှိလား' in user_message:
        update.message.reply_text("သုံးယောက်တောင် ")
    elif 'ဘဲရှိလား' in user_message:
        update.message.reply_text(" သုံးကောင်ရှိ ")
    elif 'နာမည်ဘယ်လို‌ေခါ်လည်း' in user_message:
        update.message.reply_text(" ဆရာကြီး")
    elif '‌ေစာ်ရှာ‌ေပး' in user_message:
        update.message.reply_text(" ငှက်ပျောပင်စိုက်")
    elif 'ချစ်လား' in user_message:
        update.message.reply_text(" သေလိုက် ")
    elif 'ချစ်တယ်' in user_message:
        update.message.reply_text("ကောင်မလေးရှိတယ် ")
    elif 'ကောင်မလေးရှာ‌ေပး' in user_message:
        update.message.reply_text(" ငှက်ပျောပင်စိုက် ")
    else:
        update.message.reply_text("လူနားလည်အောင်ပြော")

# Function to create the application and add handlers
def create_app(token: str) -> Updater:
    updater = Updater(token, use_context=True)
    
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, respond))
    
    return updater
    
