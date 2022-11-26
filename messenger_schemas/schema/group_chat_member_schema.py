from sqlalchemy import (
    Column,
    ForeignKeyConstraint,
    Integer,
    PrimaryKeyConstraint,
    Table,
)
from ..schema import Base

GroupChatMemberSchema = Table(
    "group_chat_member",
    Base.metadata,
    Column("group_chat_id", Integer, nullable=False),
    Column("member_id", Integer, nullable=False),
    PrimaryKeyConstraint("group_chat_id", "member_id"),
    ForeignKeyConstraint(
        ["group_chat_id"],
        ["group_chat.group_chat_id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
        name="group_chat_member_group_chat_id_FK",
    ),
    ForeignKeyConstraint(
        ["member_id"],
        ["user.user_id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
        name="group_chat_member_member_id_FK",
    ),
)
