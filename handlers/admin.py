from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from bot import bot, dp


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    phone = State()


# @dp.message_handler(commands='Загрузить', state=None)
async def process_cm_start(msg: types.Message):
    await FSMAdmin.photo.set()
    await msg.reply('Загрузите фото пропавшего питомца')


# @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = msg.photo[0].file_id
    await FSMAdmin.next()
    await msg.reply('Введите имя питомца')


# @dp.message_handler(state=FSMAdmin.name)
async def load_name(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = msg.text
    await FSMAdmin.next()
    await msg.reply('Введите подробное описание. Где пропал, во сколько, отличительные черты и т.д.')


# @dp.message_handler(state=FSMAdmin.description)
async def load_description(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = msg.text
    await FSMAdmin.next()
    await msg.reply('Введите ваши контакты')


# @dp.message_handler(state=FSMAdmin.phone)
async def load_phone(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = msg.text

    async with state.proxy() as data:
        await msg.reply(str(data))
    await state.finish()


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(process_cm_start, commands=['upload'], state=None)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_phone, state=FSMAdmin.phone)
