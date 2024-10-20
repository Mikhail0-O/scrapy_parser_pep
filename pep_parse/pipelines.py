from collections import defaultdict
from datetime import datetime
import csv

from constants import BASE_DIR, FOLDER_FOR_DATA


class PepParsePipeline:

    def __init__(self):
        self.results_dir = BASE_DIR / FOLDER_FOR_DATA
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.count_statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.count_statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        filename = (self.results_dir / datetime.now().strftime(
                    'status_summary_%Y-%m-%d_%H-%M-%S.csv'))
        with open(filename, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Статус', 'Количество'])
            rows = [(status, count) for status, count in
                    self.count_statuses.items()]
            rows.append(('Total', sum(self.count_statuses.values())))
            writer.writerows(rows)
