from sqlalchemy import Column, DATETIME, Integer, VARCHAR, CHAR, PrimaryKeyConstraint, UniqueConstraint
from sqlalchemy.orm import relationship
from .group_chat_member_schema import GroupChatMemberSchema
from .group_chat_schema import GroupChatSchema
from .message_schema import MessageSchema
from .friendship_schema import FriendshipSchema

from ..schema import Base

class UserSchema(Base):
    __tablename__ = "user"
    user_id = Column(Integer, nullable=False, autoincrement="auto")
    username = Column(VARCHAR(25), nullable=False)
    first_name = Column(VARCHAR(30), nullable=True)
    last_name = Column(VARCHAR(30), nullable=True)
    birthdate = Column(DATETIME, nullable=True)
    password_hash = Column(CHAR(60), nullable=False)
    email = Column(VARCHAR(255), nullable=False)
    
    # passive_deletes is assigned on the one side of a one-to-many relationship. It ensures that the database handles ON DELETE operations.
    # passive_updates is default to True.
    # on only the one side of a one to many relationship, specify table schema name using the class import __name__.
    friend_requests_sent = relationship(
        FriendshipSchema.__name__,
        foreign_keys=[FriendshipSchema.requester_id],
        back_populates="requester",
        passive_deletes=True)
    friend_requests_recieved = relationship(
        FriendshipSchema.__name__,
        foreign_keys=[FriendshipSchema.addressee_id],
        back_populates="addressee",
        passive_deletes=True)
    
    messages_sent = relationship(
        MessageSchema.__name__,
        foreign_keys=[MessageSchema.sender_id],
        back_populates="message_sender",
        passive_deletes=True)
    
    messages_recieved = relationship(
        MessageSchema.__name__,
        foreign_keys=[MessageSchema.reciever_id],
        back_populates="message_reciever",
        passive_deletes=True)
    
    group_chats =  relationship(
        GroupChatSchema.__name__,
        secondary=GroupChatMemberSchema, 
        back_populates="members",
        passive_deletes=True)

    PrimaryKeyConstraint(user_id)
    
    UniqueConstraint(email)
    UniqueConstraint(username)
    
    # TODO: add account status which can be banned or disabled.
    # TODO: maybe add account type (google, facebook, email and password etc.)