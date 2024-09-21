import os
import time
from pathlib import Path

BASE_DIR = Path(__file__).absolute().parent.parent


class PepParsePipeline:
    def open_spider(self, spider):
        self.result_dir = BASE_DIR / 'results'
        os.makedirs(self.result_dir, exist_ok=True)
        self.status_count = {}
        self.total_peps = 0

    def process_item(self, item, spider):
        self.status_count[item['status']] = self.status_count.get(
            item['status'],
            0
        ) + 1
        self.total_peps += 1
        return item

    def close_spider(self, spider):
        timestamp = time.strftime('%Y-%m-%dT%H-%M-%S')
        file_path = os.path.join(
            self.result_dir, f'status_summary_{timestamp}.csv'
        )
        with open(file_path, mode='w', encoding='utf-8') as f:
            f.write('Статус, Количество\n')
            for status, count in self.status_count.items():
                f.write(f'{status}: {count}\n')
            f.write(f'Total: {self.total_peps}\n')
