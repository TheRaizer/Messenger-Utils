from __future__ import annotations

from sqlalchemy import Column, Integer, VARCHAR, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from .group_chat_member_schema import GroupChatMemberSchema
from .message_schema import MessageSchema
from ..schema import BaseRecord, Base
from typing import TYPE_CHECKING, Any, List

if TYPE_CHECKING:
    from .user_schema import UserSchema


class GroupChatSchema(Base, BaseRecord):
    __tablename__ = "group_chat"
    group_chat_id = Column(Integer, nullable=False, autoincrement="auto")
    name = Column(VARCHAR(20), nullable=False)

    group_chat_messages: List[MessageSchema] = relationship(
        MessageSchema.__name__,
        back_populates="group_chat",
        passive_deletes=True,
    )
    members: List[UserSchema] = relationship(
        "UserSchema",
        secondary=GroupChatMemberSchema,
        back_populates="group_chats",
    )

    PrimaryKeyConstraint(group_chat_id)

    def key(self) -> Any:
        return self.group_chat_id
