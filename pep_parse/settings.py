from pathlib import Path

BASE_DIR = Path(__file__).absolute().parent.parent
RESULT_DIR = 'results'
BOT_NAME = 'pep_parse'
SPIDER_MODULE_PATH = 'pep_parse.spiders'
SPIDER_MODULES = [SPIDER_MODULE_PATH]
NEWSPIDER_MODULE = SPIDER_MODULE_PATH
ROBOTSTXT_OBEY = True
FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'encoding': 'utf-8',
    },
}
ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
