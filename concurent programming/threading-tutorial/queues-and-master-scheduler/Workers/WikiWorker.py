import stat
import requests
import threading
from bs4 import BeautifulSoup, Tag


class WikiWorker(threading.Thread):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
        # self.start()

    def _extract_company_symbols(self, page_html):
        soup = BeautifulSoup(page_html, "html.parser")
        table = soup.find(id="constituents")
        if isinstance(table, Tag):
            table_rows = table.find_all("tr")
            for table_row in table_rows[1:]:
                symbol = table_row.find("td").text.strip("\n")
                yield symbol

    def get_sp_500_companies(self):
        response = requests.get(self._url)
        print(self._url)
        if response.status_code != 200:
            print("Could not get the page")
            return []
        yield from self._extract_company_symbols(response.text)

    def run(self):
        self.get_sp_500_companies()


if __name__ == "__main__":
    worker = WikiWorker()
    for symbol in worker.get_sp_500_companies():
        print(symbol)
