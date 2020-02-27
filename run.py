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
from apscheduler.schedulers.blocking import BlockingScheduler


def cronjob():
    """ Cronjob """
    for url in configs['urls']:
        logging.info(f"Cron: {url}")
        if selenium.is_selling(url):
            logging.info(f"{url} is on stock!!")
            if telegram.send_message(url):
                logging.info(f"Success to send message for {url}")
            else:
                logging.info(f"Failed to send message for {url}")
        else:
            logging.info(f"{url} is out of stock!!")


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

    # Initialize notification
    logging.info(f"Initializing telegram...")
    telegram = notification.Telegram(
        auth=configs["telegram.auth"], bot_id=configs["telegram.bot_id"])
    logging.info("Succeed to create telegram!!")

    # Run cronjob
    scheduler = BlockingScheduler()
    scheduler.add_job(cronjob, 'interval',
                      seconds=configs["cron.interval"],
                      timezone="Asia/Seoul",
                      max_instances=configs["cron.max_instance"])
    scheduler.start()
