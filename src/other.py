# -*- coding: utf-8 -*-
# SCRIPT # ======================================================================================================================
# Name...........: PyDejavuBot - Free Open Source Telegram Bot, designed for recognize a melody.
# File name......: other.py
# Description ...: It stores codes that are not particularly relevant to bot health, but are vital
# Author ........: ZhymabekRoman
# ===============================================================================================================================
import re
import string
import random
import base64
import asyncio
from dataclasses import dataclass
from functools import wraps, partial
try:
    from user_data import config
except ImportError:
    pass # Fixme

# https://pynative.com/python-generate-random-string/
def generate_random_string(length: int) -> str:
    """Returns random generated string with a certain quantity letters"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

@dataclass
class path:
    """Возвращяет путь к личным папкам пользывателей, а-ля конструктор путей"""
    user_id: str
    user_folder: str = ""

    def tmp_audio_samples(self, file_name = "") -> str:
        return f'{config.USER_DATA_PATH}/audio_sample/tmp/{self.user_id}/{self.user_folder}/{file_name}'
    def processed_audio_samples(self, file_name = "") -> str:
        return f'{config.USER_DATA_PATH}/audio_sample/processed/{self.user_id}/{self.user_folder}/{file_name}'

    def tmp_query_audio(self, file_name = "") -> str:
        return f'{config.USER_DATA_PATH}/query/tmp/{self.user_id}/{self.user_folder}/{file_name}'
    def processed_query_audio(self, file_name = "") -> str:
        return f'{config.USER_DATA_PATH}/query/processed/{self.user_id}/{self.user_folder}/{file_name}'
    
    def fingerprint_db(self) -> str:
        return f'{config.USER_DATA_PATH}/audio_sample/fingerprint_db/{self.user_id}/{self.user_folder}.fpdb'
    def fingerprint_db_dir_path(self) -> str:
        return f'{config.USER_DATA_PATH}/audio_sample/fingerprint_db/{self.user_id}/'

# Не помню откуда взял этот код =)
def check_string_for_except_chars(string: str) -> str:
    """Поверяет строку на недопустимые символы, в случае если будут то возвращяет словарь с присутсвующими запрещенными символами"""
    exception_chars = '\\\/\|<>\?:"\*'
    find_exceptions = re.compile('([{}])'.format(exception_chars))
    return find_exceptions.findall(string)
    
def base64_encode(message: str) -> str:
    """Зашифровывает строку в base64"""
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message
    
def base64_decode(base64_message: str) -> str:
    """Расшифровывает base64 строку"""
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    return message

def async_wrap(func):
    @wraps(func)
    async def run(*args, loop=None, executor=None, **kwargs):
        if loop is None:
            loop = asyncio.get_event_loop()
        pfunc = partial(func, *args, **kwargs)
        return await loop.run_in_executor(executor, pfunc)
    return run 