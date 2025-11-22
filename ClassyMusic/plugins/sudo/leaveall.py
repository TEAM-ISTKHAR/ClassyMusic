import asyncio
from pyrogram import filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import InviteRequestSent
from ClassyMusic import app, userbot
from ClassyMusic.misc import SUDOERS
from ClassyMusic.utils.database import get_assistant, is_active_chat, get_client
from ClassyMusic.core.userbot import assistants
from config import LOG_GROUP_ID as ISTKHAR


@app.on_message(filters.command(["leaveall1", f"leaveall1@{app.username}"]) & SUDOERS)
async def leave_all(client, message):
    if message.from_user.id not in SUDOERS:
        return

    left = 0
    failed = 0
    lol = await message.reply("🔄 ᴜsᴇʀʙᴏᴛ ʟᴇᴀᴠɪɴɢ ᴀʟʟ ᴄʜᴀᴛs !")
    try:
        userbot = await get_client(1)
        async for dialog in userbot.get_dialogs():
            if dialog.chat.id == ISTKHAR:
                continue
            if await is_active_chat(dialog.chat.id):
                continue
            try:
                await userbot.leave_chat(dialog.chat.id)
                left += 1
                await lol.edit(
                    f"ᴜsᴇʀʙᴏᴛ ʟᴇᴀᴠɪɴɢ ᴀʟʟ ɢʀᴏᴜᴘ...\n\nʟᴇғᴛ: {left} ᴄʜᴀᴛs.\nғᴀɪʟᴇᴅ: {failed} ᴄʜᴀᴛs."
                )
            except BaseException:
                failed += 1
                await lol.edit(
                    f"ᴜsᴇʀʙᴏᴛ ʟᴇᴀᴠɪɴɢ...\n\nʟᴇғᴛ: {left} chats.\nғᴀɪʟᴇᴅ: {failed} chats."
                )
            await asyncio.sleep(3)
    finally:
        await app.send_message(
            message.chat.id,
            f"✅ ʟᴇғᴛ ғʀᴏᴍ:* {left} chats.\n❌ ғᴀɪʟᴇᴅ ɪɴ:** {failed} chats.",
        )


@app.on_message(filters.command(["leaveall2", f"leaveall2@{app.username}"]) & SUDOERS)
async def leave_all(client, message):
    if message.from_user.id not in SUDOERS:
        return

    left = 0
    failed = 0
    lol = await message.reply("🔄 ᴜsᴇʀʙᴏᴛ ʟᴇᴀᴠɪɴɢ ᴀʟʟ ᴄʜᴀᴛs !")
    try:
        userbot = await get_client(2)
        async for dialog in userbot.get_dialogs():
            if dialog.chat.id == ISTKHAR:
                continue
            if await is_active_chat(dialog.chat.id):
                continue
            try:
                await userbot.leave_chat(dialog.chat.id)
                left += 1
                await lol.edit(
                    f"ᴜsᴇʀʙᴏᴛ ʟᴇᴀᴠɪɴɢ ᴀʟʟ ɢʀᴏᴜᴘ...\n\nʟᴇғᴛ: {left} ᴄʜᴀᴛs.\nғᴀɪʟᴇᴅ: {failed} ᴄʜᴀᴛs."
                )
            except BaseException:
                failed += 1
                await lol.edit(
                    f"ᴜsᴇʀʙᴏᴛ ʟᴇᴀᴠɪɴɢ...\n\nʟᴇғᴛ: {left} chats.\nғᴀɪʟᴇᴅ: {failed} chats."
                )
            await asyncio.sleep(3)
    finally:
        await app.send_message(
            message.chat.id,
            f"✅ ʟᴇғᴛ ғʀᴏᴍ:* {left} chats.\n❌ ғᴀɪʟᴇᴅ ɪɴ:** {failed} chats.",
        )

@app.on_message(filters.command(["leaveall3", f"leaveall3@{app.username}"]) & SUDOERS)
async def leave_all(client, message):
    if message.from_user.id not in SUDOERS:
        return

    left = 0
    failed = 0
    lol = await message.reply("🔄 ᴜsᴇʀʙᴏᴛ ʟᴇᴀᴠɪɴɢ ᴀʟʟ ᴄʜᴀᴛs !")
    try:
        userbot = await get_client(3)
        async for dialog in userbot.get_dialogs():
            if dialog.chat.id == ISTKHAR:
                continue
            if await is_active_chat(dialog.chat.id):
                continue
            try:
                await userbot.leave_chat(dialog.chat.id)
                left += 1
                await lol.edit(
                    f"ᴜsᴇʀʙᴏᴛ ʟᴇᴀᴠɪɴɢ ᴀʟʟ ɢʀᴏᴜᴘ...\n\nʟᴇғᴛ: {left} ᴄʜᴀᴛs.\nғᴀɪʟᴇᴅ: {failed} ᴄʜᴀᴛs."
                )
            except BaseException:
                failed += 1
                await lol.edit(
                    f"ᴜsᴇʀʙᴏᴛ ʟᴇᴀᴠɪɴɢ...\n\nʟᴇғᴛ: {left} chats.\nғᴀɪʟᴇᴅ: {failed} chats."
                )
            await asyncio.sleep(3)
    finally:
        await app.send_message(
            message.chat.id,
            f"✅ ʟᴇғᴛ ғʀᴏᴍ:* {left} chats.\n❌ ғᴀɪʟᴇᴅ ɪɴ:** {failed} chats.",
        )


@app.on_message(filters.command(["leaveall4", f"leaveall4@{app.username}"]) & SUDOERS)
async def leave_all(client, message):
    if message.from_user.id not in SUDOERS:
        return

    left = 0
    failed = 0
    lol = await message.reply("🔄 ᴜsᴇʀʙᴏᴛ ʟᴇᴀᴠɪɴɢ ᴀʟʟ ᴄʜᴀᴛs !")
    try:
        userbot = await get_client(4)
        async for dialog in userbot.get_dialogs():
            if dialog.chat.id == ISTKHAR:
                continue
            if await is_active_chat(dialog.chat.id):
                continue
            try:
                await userbot.leave_chat(dialog.chat.id)
                left += 1
                await lol.edit(
                    f"ᴜsᴇʀʙᴏᴛ ʟᴇᴀᴠɪɴɢ ᴀʟʟ ɢʀᴏᴜᴘ...\n\nʟᴇғᴛ: {left} ᴄʜᴀᴛs.\nғᴀɪʟᴇᴅ: {failed} ᴄʜᴀᴛs."
                )
            except BaseException:
                failed += 1
                await lol.edit(
                    f"ᴜsᴇʀʙᴏᴛ ʟᴇᴀᴠɪɴɢ...\n\nʟᴇғᴛ: {left} chats.\nғᴀɪʟᴇᴅ: {failed} chats."
                )
            await asyncio.sleep(3)
    finally:
        await app.send_message(
            message.chat.id,
            f"✅ ʟᴇғᴛ ғʀᴏᴍ:* {left} chats.\n❌ ғᴀɪʟᴇᴅ ɪɴ:** {failed} chats.",
        )


@app.on_message(filters.command(["leaveall5", f"leaveall5@{app.username}"]) & SUDOERS)
async def leave_all(client, message):
    if message.from_user.id not in SUDOERS:
        return

    left = 0
    failed = 0
    lol = await message.reply("🔄 ᴜsᴇʀʙᴏᴛ ʟᴇᴀᴠɪɴɢ ᴀʟʟ ᴄʜᴀᴛs !")
    try:
        userbot = await get_client(5)
        async for dialog in userbot.get_dialogs():
            if dialog.chat.id == ISTKHAR:
                continue
            if await is_active_chat(dialog.chat.id):
                continue
            try:
                await userbot.leave_chat(dialog.chat.id)
                left += 1
                await lol.edit(
                    f"ᴜsᴇʀʙᴏᴛ ʟᴇᴀᴠɪɴɢ ᴀʟʟ ɢʀᴏᴜᴘ...\n\nʟᴇғᴛ: {left} ᴄʜᴀᴛs.\nғᴀɪʟᴇᴅ: {failed} ᴄʜᴀᴛs."
                )
            except BaseException:
                failed += 1
                await lol.edit(
                    f"ᴜsᴇʀʙᴏᴛ ʟᴇᴀᴠɪɴɢ...\n\nʟᴇғᴛ: {left} chats.\nғᴀɪʟᴇᴅ: {failed} chats."
                )
            await asyncio.sleep(3)
    finally:
        await app.send_message(
            message.chat.id,
            f"✅ ʟᴇғᴛ ғʀᴏᴍ:* {left} chats.\n❌ ғᴀɪʟᴇᴅ ɪɴ:** {failed} chats.",
        )

