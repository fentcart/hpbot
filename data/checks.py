import json
import discord
from discord.ext import commands

def getProfile(userID):
    with open("data/warns.json", "r", encoding='utf-8') as config:
        data = json.load(config)
    return data["users"].get(str(userID))

def addWarning(userID, warning):
    with open("data/warns.json", "r+", encoding='utf-8') as config:
        data = json.load(config)
        if str(userID) not in data["users"]:
            data["users"][str(userID)] = {"warnings": []}
        data["users"][str(userID)]["warnings"].append(warning)
        config.seek(0)
        json.dump(data, config, indent=4)
        config.truncate()

def removeWarning(userID, warnID):
    with open("data/warns.json", "r+", encoding='utf-8') as config:
        data = json.load(config)
        if str(userID) in data["users"]:
            warnings = data["users"][str(userID)]["warnings"]
            data["users"][str(userID)]["warnings"] = [warn for warn in warnings if warn["id"] != warnID]
            config.seek(0)
            json.dump(data, config, indent=4)
            config.truncate()

def getWarnings(userID):
    profile = getProfile(userID)
    return profile["warnings"] if profile and "warnings" in profile else []

def is_staff():
    async def predicate(ctx: discord.ApplicationContext):
        if not ctx.guild:  # Ensure the command is invoked in a guild
            return False
        
        role_ids = [1009943383785078836, 1136451117610446848]  # Replace with your actual role IDs
        user_roles = [role.id for role in ctx.author.roles]
        if not any(role_id in user_roles for role_id in role_ids):
            return False
        
        return True
    
    return commands.check(predicate)
