from pathlib import Path

BASE_DIR = Path(__file__).absolute().parent.parent
RESULT_DIR = 'results'
BOT_NAME = 'pep_parse'
NEWSPIDER_MODULE = 'pep_parse.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]
ROBOTSTXT_OBEY = True
FEEDS = {
    RESULT_DIR + '/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'encoding': 'utf-8',
    },
}
ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
