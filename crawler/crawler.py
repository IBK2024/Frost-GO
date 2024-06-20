from math import ceil
from queue import Queue
from threading import Thread
from time import sleep
from typing import Any, Dict, List, NoReturn

from pymongo.database import Database

from general.parse_robot_txt import parse_robot_txt
from models.crawled import Crawled
from models.queue import Queue as QueueCollection


class Crawler:
    """
    Crawler downloads pages in the queue table of the database

    Only downloads pages if allowed be the robot.txt

    If any errors adds link to failed crawl.
    """

    # !Variables
    max_number_of_threads = 0
    to_parse_directory = ""
    queue: List[Dict[str, str | float]] = []
    crawled: List[Dict[str, str]] = []
    db: Database[Dict[str, Any]]
    crawlerQueue: Queue[float] = Queue()

    def __init__(
        self,
        max_number_of_threads: int,
        to_parse_directory: str,
        db: Database[Dict[str, Any]],
    ) -> None:
        self.max_number_of_threads = max_number_of_threads
        self.to_parse_directory = to_parse_directory
        self.db = db

        # !Get items in crawled and queue collections
        queue = QueueCollection(self.db["queue"])
        crawled = Crawled(db["crawled"])

        self.queue = queue.get()
        self.crawled = crawled.get()

        # !Creates threads
        self.main()

    # !Creates threads
    def main(self) -> None:
        "Creates the threads needed for the crawler"
        Thread(target=self.work, daemon=True).start()
        for _ in range(ceil(self.max_number_of_threads / 2)):
            Thread(target=self.crawl_work, daemon=True).start()
        for _ in range(ceil(self.max_number_of_threads / 2)):
            Thread(target=self.crawl_work, daemon=True).start()

    # !Assigns tasks to the crawling threads
    def work(self) -> NoReturn:
        """Assigns tasks to the crawling threads"""
        while True:
            # !Iterates over links in queue assigns them to the crawler thread
            for item in self.queue:
                self.crawlerQueue.put(float(item["id"]))

            # !Waits for all tasks to be completed
            self.crawlerQueue.join()

            # !Waits for 3 seconds before continuing
            sleep(3)

    # !Picks a website from the task queue and crawls it
    def crawl_work(self) -> NoReturn:
        """Picks a website from the task queue and crawls it"""
        while True:
            # !Picks an id from the task queue gets the item from the database
            link_in_db = [
                item for item in self.queue if item["id"] == self.crawlerQueue.get()
            ][0]

            is_allowed = parse_robot_txt(str(link_in_db["url"]))

            if is_allowed is True:
                print(link_in_db)

            # !Finishes the task
            self.crawlerQueue.task_done()
