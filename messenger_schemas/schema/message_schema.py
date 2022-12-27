from __future__ import annotations

from sqlalchemy import (
    BOOLEAN,
    Column,
    DATETIME,
    ForeignKeyConstraint,
    Integer,
    VARCHAR,
    PrimaryKeyConstraint,
)
from ..schema import BaseRecord, Base
from sqlalchemy.orm import relationship
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .user_schema import UserSchema
    from .group_chat_schema import GroupChatSchema


class MessageSchema(Base, BaseRecord):
    __tablename__ = "message"
    message_id = Column(Integer, nullable=False, autoincrement="auto")
    sender_id = Column(Integer, nullable=True)
    reciever_id = Column(Integer, nullable=True)
    content = Column(VARCHAR(300), nullable=False)
    created_date_time = Column(DATETIME, nullable=False)
    last_edited_date_time = Column(DATETIME, nullable=True)
    group_chat_id = Column(Integer, nullable=True)
    seen = Column(BOOLEAN, nullable=True, server_default="0")

    ForeignKeyConstraint(
        [sender_id],
        ["user.user_id"],
        onupdate="CASCADE",
        ondelete="SET NULL",
        name="message_sender_id_FK",
    )

    ForeignKeyConstraint(
        [reciever_id],
        ["user.user_id"],
        onupdate="CASCADE",
        ondelete="SET NULL",
        name="message_reciever_id_FK",
    )

    ForeignKeyConstraint(
        [group_chat_id],
        ["group_chat.group_chat_id"],
        onupdate="CASCADE",
        ondelete="SET NULL",
        name="message_group_chat_id_FK",
    )

    message_sender: UserSchema = relationship(
        "UserSchema", foreign_keys=[sender_id], back_populates="messages_sent"
    )
    message_reciever: UserSchema = relationship(
        "UserSchema",
        foreign_keys=[reciever_id],
        back_populates="messages_recieved",
    )
    group_chat: GroupChatSchema = relationship(
        "GroupChatSchema", back_populates="group_chat_messages"
    )

    PrimaryKeyConstraint(message_id)

    def key(self) -> Any:
        return self.message_id
