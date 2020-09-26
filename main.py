import mechanicalsoup
import re
import time


class Goal:

    class _FootballNews:
        def __init__(self):
            self.browser = self.create_browser_object()
            self.headlines = None
        
        def create_browser_object(self):
            return mechanicalsoup.StatefulBrowser(
                raise_on_404=True,
                user_agent=(
                    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0)'
                    ' Gecko/20100101 Firefox/64.0'
                )
            )

        def fetch_news(self):
            self.browser.open('https://www.goal.com/en/news/1')
            raw_headlines = self.browser.get_current_page().find_all('h3')
            self.headlines = self.filter_headlines(raw_headlines)
            self.display_headlines(self.headlines)
        
        def filter_headlines(self, raw_headlines):
            filtration_regex_rule = re.compile(r'title="(.+)">')
            cleaned_headlines = {
                (filtration_regex_rule.search(str(i)).group(1)) for i in raw_headlines
            }
            return cleaned_headlines

        def display_headlines(self, headlines):
            for i in self.headlines:
                print(i+'\n\n')

        def close_browser(self):     
            self.browser.close()


    def get_news(self):
        l = self._FootballNews()
        print('loading...')
        time.sleep(2)
        print('fetching news headlines from goal.com...\n')
        l.fetch_news()
        l.close_browser()

    def start(self):
        try:
            self.get_news()
        except Exception:
            print('fail to connect')
            time.sleep(3)
            print("i'm gonna retry now...")
            self.start()
        input()


if __name__ == '__main__':
    Goal().start()
