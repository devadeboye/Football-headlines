import mechanicalsoup
import re



class Goal:
    """
    public interface to the football news script

    function includes:
    - get_news: get football news headlines from goal.com.
    """

    class _FootballNews:
        """
        A non-public class to fetch the latest headlines
        from goal.com
        """

        #------------------------------------------------------

        def __init__(self):
            """
            initialise the browser
            """
            #create browser obj
            self.browser = mechanicalsoup.StatefulBrowser(
                raise_on_404=True,
                user_agent='Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0'
            )
            # temporarily store and filter the headline
            self.temp = set()

        #-------------------------------------------------

        def _fetch_news(self):
            """
            A non-public method to get the news headlines.
            """
            # open browser and go to goal.com
            self.browser.open('http://goal.com/en')

            # get latest headlines and store in the variable
            raw_headlines = self.browser.get_current_page().find_all('h3')
            
            # create the news regex pattern
            news_regex_obj = re.compile(r'title="(.+)">')

            # filter the headlines
            for i in raw_headlines:
                j = news_regex_obj.search(str(i))
                #print(j.group(1))
                self.temp.add(j.group(1))
                print(len(self.temp))

        #----------------------------------------------------------------

        def _rite(self):
            """
            A non-public method that writes the news to file
            """
            # open a txt file to write the news
            f = open('FBnews.txt', 'a')
            # write each news in the set to file
            for i in self.temp:
                f.write(i+'\n\n')
            print('completed')

        #-----------------------------------------------------

        def _close_browser(self):
            """
            closes the browser
            """      
            self.browser.close()

    #-----------------------------------------------------

    def get_news(self):
        l = self._FootballNews()
        l._fetch_news()
        l._rite()
        l._close_browser()

    

#------------ test --------------
if __name__ == '__main__':
    Goal().get_news()