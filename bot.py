import config
import logging
import datetime

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer("Привет!\nЯ тупой бот)") 

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer("/start - start \n/s - расписание на сегодня\n/n - номер недели\n/timetable - показывает всё расписание ")

@dp.message_handler(commands=['timetable'])
async def process_timetable_command(message: types.Message):
    await message.answer_photo("https://i.pinimg.com/564x/28/49/99/284999cfee9989202276b8fa51c8d375.jpg")
    
@dp.message_handler(commands=['s'])
async def process_timeday_command(message: types.Message):

    if datetime.datetime.today().isoweekday() == 1 :
        if int(datetime.datetime.today().strftime("%V"))%2 == 0:
            await message.answer("Сегодня понедельник чётная неделя: \n1 пара - окно \n2 пара - окно \n3 пара - Философия ПР \n4 пара - СМЗ ЛБ  ")

        else: 
            await message.answer("Сегодня понедельник нечётная неделя: \n1 пара - Python ЛК \n2 пара - Python ЛБ \n3 пара - Философия ПР \n4 пара - СМЗ ПР ")


    elif datetime.datetime.today().isoweekday() == 2 :
        if int(datetime.datetime.today().strftime("%V"))%2 == 0:
            await message.answer("Сегодня вторник чётная неделя: \n1 пара - окно \n2 пара - IP ЛК \n3 пара - IP ПР \n4 пара - МОС ЛК  ")

        else: 
            await message.answer("Сегодня вторник нечётная неделя: \n1 пара - окно \n2 пара - IP ЛК \n3 пара - окно \n4 пара - Философия ЛК ")
    elif datetime.datetime.today().isoweekday() == 3 :
        if int(datetime.datetime.today().strftime("%V"))%2 == 0:
            await message.answer("Сегодня среда чётная неделя: \n1 пара - окно \n2 пара - КМИМ ЛК \n3 пара - окно \n4 пара - IP ЛБ в шараге  ")

        else: 
            await message.answer("Сегодня среда нечётная неделя: \n1 пара - СМЗ ЛК  \n2 пара - КМИМ ПР \n3 пара - окно \n4 пара - IP ЛБ в шараге ")
    elif datetime.datetime.today().isoweekday() == 4 :
        if int(datetime.datetime.today().strftime("%V"))%2 == 0:
            await message.answer("Сегодня четверг чётная неделя: \nвыходной ")

        else: 
            await message.answer("Сегодня четверг нечётная неделя: \n1 пара - окно \n2 пара - окно \n3 пара - окно \n4 пара - ЕМТ ЛК в шараге ")
    elif datetime.datetime.today().isoweekday() == 5 :
        if int(datetime.datetime.today().strftime("%V"))%2 == 0:
            await message.answer("Сегодня пятница чётная неделя --> В шарагу : \n1 пара - ЕМТ ЛБ \n2 пара - МОС ЛБ ")

        else: 
            await message.answer("Сегодня пятница нечётная неделя --> В шарагу : \n1 пара - ЕМТ ПР \n2 пара - МОС ПР \n3 пара - КМИМ ЛБ ")
    else :
        if int(datetime.datetime.today().strftime("%V"))%2 == 0:
            await message.answer("выходной, следующая нечётная")
        else :
            await message.answer("выходной, следующая чётная")
        
#datetime.datetime.strptime(format[datetime.datetime.today(),'%U'])

@dp.message_handler(commands=['n'])
async def process_time_command(message: types.Message):
    await message.answer(datetime.datetime.today().strftime("%V"))  

if __name__ == "__main__":
	executor.start_polling(dp, skip_updates=True)