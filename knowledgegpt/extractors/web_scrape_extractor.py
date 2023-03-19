from knowledgegpt.utils.utils_scrape import scrape_content
from knowledgegpt.extractors.base_extractor import BaseExtractor


class WebScrapeExtractor(BaseExtractor):
    """
    Function that takes a URL as input and returns the response answer.
    """

    def __init__(self, url, embedding_extractor: str, model_lang: str, is_turbo: bool = False, verbose: bool = False, save_index: bool = False, index_path: str = None):
        super().__init__(embedding_extractor=embedding_extractor, model_lang=model_lang, is_turbo=is_turbo, verbose=verbose, save_index=save_index, index_path=index_path)
        self.url = url

    def prepare_df(self):
        if self.df is None:
            if not self.verbose:
                print("Scraping website...")
            if not self.url:
                raise ValueError("url is missing")
            self.df = scrape_content(self.url)
