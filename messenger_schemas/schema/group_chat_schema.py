from sqlalchemy import Column, Integer, VARCHAR, PrimaryKeyConstraint
from sqlalchemy.orm import relationship

from messenger_schemas.schema.group_chat_member_schema import GroupChatMemberSchema
from messenger_schemas.schema.message_schema import MessageSchema

from ..schema import Base

class GroupChatSchema(Base):
    __tablename__ = "group_chat"
    group_chat_id = Column(Integer, nullable=False, autoincrement="auto")
    name = Column(VARCHAR(20), nullable=False)
    
    group_chat_messages = relationship(MessageSchema.__name__, back_populates="group_chat", passive_deletes=True)
    members = relationship("UserSchema", secondary=GroupChatMemberSchema.__name__, back_populates="group_chats")
    
    PrimaryKeyConstraint(group_chat_id)