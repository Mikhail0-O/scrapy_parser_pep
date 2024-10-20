# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


from collections import defaultdict
from datetime import datetime

from constants import BASE_DIR


class PepParsePipeline:

    def open_spider(self, spider):
        self.count_statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.count_statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / 'results'
        print(results_dir)
        results_dir.mkdir(exist_ok=True)
        filename = (results_dir / datetime.now().strftime(
                    'status_summary_%Y-%m-%d_%H-%M-%S.csv'))
        with open(filename, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for status, count in self.count_statuses.items():
                f.write(f'{status},{count}\n')
            f.write(f'Total,{sum(self.count_statuses.values())}\n')
