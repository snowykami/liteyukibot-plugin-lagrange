# -*- coding: utf-8 -*-
"""
Copyright (C) 2020-2024 LiteyukiStudio. All Rights Reserved 

@Time    : 2024/8/22 下午8:33
@Author  : snowykami
@Email   : snowykami@outlook.com
@File    : __init__.py.py
@Software: PyCharm
"""
import threading

from liteyuki import get_bot
from liteyuki.plugin import PluginMetadata, PluginType

from .start import launch

__plugin_meta__ = PluginMetadata(
    name="Lagrange-python for LiteyukiBot",
    description="An Python Implementation of NTQQ PC Protocol for LiteyukiBot",
    type=PluginType.APPLICATION,
)

bot = get_bot()


@bot.on_after_start
async def _():
    launch()
