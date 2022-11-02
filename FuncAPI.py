# The main API functions for the operation of the application,
# without using functions for the operation of in-game sub-applications

# Основные функции API для работы приложения,
# без использования функций для работы внутриигровых подприложений

def reg_in(name, password, image) -> [session_token, recovery_token, ID]:
    pass


def log_in(name, password) -> [session_token, ID]:
    generation_token()


def log_out(session_token):
    remove(session_token)


def load_profile_image(ID) -> image:
    pass


def change_profile_image(session_token, image):
    update(image)


def change_profile_name(session_token, old_name, new_name):
    name = old_name
    name.update(new_name)


def delete_user(session_token, password):
    delete(ID)


def load_available_languages() -> ListOf('eng', 'ru', 'jp'):
    pass


def load_profile_status(ID) -> [ID, name, scores, lives]:
    pass


def load_top10() -> ListOf(ID, name, score):
    pass


# The main API functions for in-game sub-applications
# Основные функции API  для работы внутриигровых подприложений

def start_translate_session(session_token, native_language, foreign_language) -> [sessionID, word]:
    pass


def start_isTruth_session(session_token, native_language, foreign_language) -> [sessionID, foreign_word, offereg_translate]:
    pass


...

def end_session(session_token, sessionID) -> Status:
    pass
