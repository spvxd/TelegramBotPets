from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from bot import bot, dp
from aiogram.dispatcher.filters import Text
from database import database
ID = None


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    phone = State()


# @dp.message_handler(commands=['Moderator'], is_chat_admin=True)
async def make_changes(msg: types.Message):
    global ID
    ID = msg.from_user.id
    await bot.send_message(msg.from_user.id, 'Админка')
    await msg.delete()


# @dp.message_handler(commands='Загрузить', state=None)
async def process_cm_start(msg: types.Message):
    if msg.from_user.id == ID:
        await FSMAdmin.photo.set()
        await msg.reply('Загрузите фото пропавшего питомца')


# @dp.message_handler(state="*", commands='Отмена')
# @dp.message_handler(Text(equals = 'Отмена', ignore_case=True),state="*")
async def cancel_handler(msg: types.Message, state: FSMContext):
    if msg.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await msg.reply('Ок')

# @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(msg: types.Message, state: FSMContext):
    if msg.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = msg.photo[0].file_id
        await FSMAdmin.next()
        await msg.reply('Введите имя питомца')


# @dp.message_handler(state=FSMAdmin.name)
async def load_name(msg: types.Message, state: FSMContext):
    if msg.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = msg.text
        await FSMAdmin.next()
        await msg.reply('Введите подробное описание. Где пропал, во сколько, отличительные черты и т.д.')


# @dp.message_handler(state=FSMAdmin.description)
async def load_description(msg: types.Message, state: FSMContext):
    if msg.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = msg.text
        await FSMAdmin.next()
        await msg.reply('Введите ваши контакты')


# @dp.message_handler(state=FSMAdmin.phone)
async def load_phone(msg: types.Message, state: FSMContext):
    if msg.from_user.id == ID:
        async with state.proxy() as data:
            data['phone'] = msg.text
        await database.database_command(state)
        await state.finish()
        await msg.reply('Данные отправлены')


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(process_cm_start, commands=['upload'], state=None)
    dp.register_message_handler(cancel_handler, state="*", commands='Отмена')
    dp.register_message_handler(cancel_handler, Text(equals='Отмена', ignore_case=True), state="*")
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_phone, state=FSMAdmin.phone)
    dp.register_message_handler(make_changes, commands=['Moderator'], is_chat_admin=True)