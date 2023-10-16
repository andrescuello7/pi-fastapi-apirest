# Router for call of HTTP request
class RoutesEnum:
    post_character = '/api/character/add'
    get_all_characters = '/api/character/getAll'
    get_character_by_id = '/api/character/get/{id}'
    delete_character = '/api/character/delete/{id}'