#!/usr/bin/env python3
"""
APPLICATION
"""

import os
import logging
import yaml
from configtree import Loader, Tree
from app import selenium
from app import notification


# def run():
#     for url in configs['URL']:
#         pass
#         """
#         if selenium.get_retail_info(url):
#             notification(key, url)
#         """


if __name__ == "__main__":

    # Set log level
    logging.basicConfig(level=logging.INFO)

    # Set config path
    config_path = os.path.join(os.getcwd(), 'config.yaml')

    # Load config
    logging.info(f"Loading config file from {config_path}")
    load = Loader()
    configs = load(config_path)

    # Initialize selenium
    logging.info("Initializing selenium chrome driver...")
    selenium = selenium.ChromeSelenium()
    logging.info("Succeed to create chrome driver!!")
    selenium.is_selling(configs["URL"][0])

    # Initialize notification
    logging.info(f"Initializing telegram...")
    telegram = notification.Telegram(
        auth=configs["telegram.auth"], bot_id=configs["telegram.bot_id"])
    logging.info("Succeed to create telegram!!")

    # runcron('period', 'run')
