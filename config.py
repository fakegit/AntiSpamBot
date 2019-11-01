# please change token and salt
TOKEN:   str = "token_here"
SALT:    str = "whatever"
WORKERS: int = 32

AT_ADMINS_RATELIMIT: int = 5*60
# memorize some chat messages in case that some users
# send messages before the bot restricts them
STORE_CHAT_MESSAGES: int = 100
# do garbage collection every 7200 seconds
GARBAGE_COLLENTION_INTERVAL: int = 7200

# These options can be changed per group
CHAT_SETTINGS = {
    'WELCOME_WORDS': [
        '新入群的用户，请在 %time% 秒内回答如下问题',
    ],

    'CLG_QUESTIONS': [
        ['archlinux 是一个 什么 GNU/Linux 发行版', '滚动', '滑动', '移动', '转动', '跳动', '活动', '浮动', '不动'],
        ['您进群的目的是什么', '学习交流', '发小广告', '垃圾信息', '炸群爆破'],
    ],

    'CHALLENGE_SUCCESS': [
        "验证成功。",
    ],

    'PERMISSION_DENY': [
        "您无需验证",
        "瞎点什么，没你什么事！",
        "这是给人家管理员点的地方！",
        "点你妹！你就这么想被口球吗？",
    ],

    'CHALLENGE_TIMEOUT': 5*60,
    'UNBAN_TIMEOUT': 5*60,
    'FLOOD_LIMIT': 10,
}

CHAT_SETTINGS_HELP = {
    'WELCOME_WORDS': ("欢迎词", "设置欢迎词，其中%time%代表验证时间限制(秒)，多个选择请分多行输入"),
    'CLG_QUESTIONS': ("验证问题", "设置验证问题，格式为:\n问题\n正确答案\n错误答案\n(多个错误答案)"),
    'CHALLENGE_SUCCESS': ("验证成功消息", "验证成功时的弹窗消息，应为一段文字，多个选择请分多行输入"),
    'PERMISSION_DENY': ("无需验证消息", "无需验证时的弹窗消息，应为一段文字，多个选择请分多行输入"),
    'CHALLENGE_TIMEOUT': ("验证超时时间", "验证超时时间，单位为秒，范围为1到3600"),
    'UNBAN_TIMEOUT': ("解封时间", "超时或者验证失败后的解封时间，单位为秒，设置为0或大于86400即为永久封禁"),
    'FLOOD_LIMIT': ("防止刷屏", "在验证超时时间内，超过一定数量的加群触发刷屏防护。设置为0为禁用，1为始终启用"),
}

# use userbot backend. DO NOT change if you don't know what it is.
USER_BOT_BACKEND: bool = False
API_ID:   int = 00000 # Your api id
API_HASH: str = 'Your api hash'

DEBUG: bool = False