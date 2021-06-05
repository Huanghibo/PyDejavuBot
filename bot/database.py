# -*- coding: utf-8 -*-
# SCRIPT # ======================================================================================================================
# Name...........: PyDejavuBot - Free Open Source Telegram Bot, designed for recognize a melody.
# File name......: database.py
# Description ...: Is designed to work with the database. Is the conductor between databases with the bot master code
# Author ........: ZhymabekRoman
# ===============================================================================================================================

import sqlite3


class SQLighter:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.connection.execute("PRAGMA foreign_keys = ON")  # Need for working with foreign keys in db
        self.cursor = self.connection.cursor()

    def select_user(self, user_id):
        with self.connection:
            return self.cursor.execute("SELECT * FROM users WHERE user_id= :0", {'0': user_id}).fetchone()

    def create_user(self, user_id, user_name) -> None:
        with self.connection:
            self.cursor.execute("INSERT INTO users VALUES (:0, :1)", {'0': user_id, '1': user_name})

    def select_user_folders(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM folders Where user_id= :0", {'0': user_id}).fetchall()
            return result

    def select_folder_samples(self, folder_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM audio_samples WHERE folder_id= :0", {'0': folder_id}).fetchall()
            return result

    def select_folder(self, folder_id):
        with self.connection:
            return self.cursor.execute("SELECT * FROM folders WHERE folder_id= :0", {'0': folder_id}).fetchone()

    def create_folder(self, user_id, folder_name) -> None:
        """Создает папку"""
        with self.connection:
            self.cursor.execute("INSERT INTO folders (folder_name, user_id) VALUES (:0, :1)", {'0': folder_name, '1': user_id})

    def delete_folder(self, folder_id) -> None:
        """Удаляет папку"""
        with self.connection:
            self.cursor.execute("DELETE FROM folders WHERE folder_id= :0", {'0': folder_id})

    def register_audio_sample(self, folder_id, audio_sample_name, file_id) -> None:
        """Регистрирует сэмпл в папку"""
        with self.connection:
            self.cursor.execute("INSERT INTO audio_samples (audio_sample_name, folder_id, file_unique_id) VALUES (:0, :1, :2)", {'0': audio_sample_name, '1': folder_id, '2': file_id})

    def unregister_audio_sample(self, folder_id, sample_name) -> None:
        """Удаляет определенный сэмпл из папки"""
        with self.connection:
            self.cursor.execute("DELETE FROM audio_samples WHERE audio_sample_name= :0 AND folder_id= :1", {'0': sample_name, '1': folder_id})
