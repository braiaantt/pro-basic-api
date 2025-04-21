from app.database.fake_database import contents
from app.models.content_model import Content, ContentPublic

def get_public_contents():
    public_contents = [
        ContentPublic(id=content.id, title=content.title, role_required=content.role_required)
        for content in contents
        if content.role_required < 2
    ]

    return public_contents

def get_content(content_id: int):
    for content in contents:
        if content.id == content_id:
            return content
        
    return None    

def add_content(new_content: Content):
    for content in contents:
        if content.id == new_content.id:
            return False
        
    contents.append(new_content)
    return True

def update_content(updated_content: Content):
    for index, content in enumerate(contents):
        if content.id == updated_content.id:
            contents[index] = updated_content
            return True
        
    return False

def delete_content(content_id: int):
    for index, content in enumerate(contents):
        if content.id == content_id:
            del contents[index]
            return True

    return False