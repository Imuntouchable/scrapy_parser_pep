import csv
import time
from collections import defaultdict
from pathlib import Path

from .settings import BASE_DIR, RESULT_DIR


class PepParsePipeline:
    def __init__(self):
        self.result_dir = Path(BASE_DIR / RESULT_DIR)
        self.result_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.status_count = defaultdict(int)

    def process_item(self, item, spider):
        self.status_count[item['status']] += 1
        return item

    def close_spider(self, spider):
        timestamp = time.strftime('%Y-%m-%dT%H-%M-%S')
        file_path = self.result_dir / f'status_summary_{timestamp}.csv'
        rows = [(status, count) for status, count in self.status_count.items()]
        rows.append(('Total', sum(self.status_count.values())))
        with open(file_path, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Статус', 'Количество'])
            writer.writerows(rows)
