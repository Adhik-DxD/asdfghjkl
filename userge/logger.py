# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/uaudith/Userge/blob/master/LICENSE >
#
# All rights reserved.

__all__ = ['logging']

import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s - %(levelname)s] - %(name)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    handlers=[
                        RotatingFileHandler(
                            "logs/userge.log", maxBytes=(20480), backupCount=10),
                        logging.StreamHandler()
                    ])

for name, logger in logging.root.manager.loggerDict.items():
    if name.startswith('pyrogram'):
        logger.disabled = True
