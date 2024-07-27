import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError
import itertools
from urllib.parse import urljoin
from urllib import robotparser
from urllib.parse import urlparse
import re, time, os

#for html downloads
import requests
#scraping
from lxml.html import fromstring


#Define folder parameters
folder_name = "downloads"
current_directory = os.getcwd()
new_folder_path = os.path.join(current_directory, folder_name)
# Create the folder if it does not exist
if not os.path.exists(new_folder_path):
    os.makedirs(new_folder_path)




def download(url,user_agent='wswp', num_retries=2,charset='utf-8'):
    """
    Download and return html text from url
    """
    print('Downloading:', url)
    request = urllib.request.Request(url)
    request.add_header('User-agent', user_agent)
    try:
        html_b = urllib.request.urlopen(request)
        encoding = html_b.headers.get_content_charset()
        if not encoding:
            encoding=charset
        html = html_b.read().decode(encoding)
    except (URLError, HTTPError, ContentTooShortError) as e:
        print('Download error:', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # recursively retry 5xx HTTP errors
                return download(url, num_retries - 1)
    return html


def link_crawler(start_url, link_regex,robots_url=None,user_agent='wswp',max_depth=2,delay=2,scrape_callback=None):
    """ Crawl from the given start URL following links matched by
    link_regex
    """
    if not robots_url:
        robots_url = r'{}/robots.txt'.format(start_url)
        rp = get_robots_parser(robots_url)

    throttle = Throttle(delay)# wait interval before trying to load link

    crawl_queue = [start_url]
    #keep track which URL's have seen before
    #seen = set(crawl_queue)
    seen ={}
    while crawl_queue:
        url = crawl_queue.pop()
        #check url passes robots.txt restrictions
        '''
        Normally, the next code check if the crawler is authorized to crawl the site, but due to parts of this site being restricted, it results
        in failed authorization. I have added a 'not' befotre rp.can_fetch() to force the code to download the parts that are accessible anyways.
        '''
        if not rp.can_fetch(user_agent, url):
            depth = seen.get(url, 0)
            if depth == max_depth:
                print('Skipping %s due to depth' % url)
                continue
            throttle.wait(url)
            html = download(url, user_agent=user_agent)       
            if html:
                #do something with html, like scraping
                if scrape_callback:
                    scrape_callback(url,html)
                # filter for links matching our regular expression
                for link in get_links(html):
                    if re.search(link_regex, link):
                        abs_link = urljoin(start_url, link)
                        # check if have already seen this link
                        if abs_link not in seen:
                            #seen.add(abs_link)
                            seen[abs_link] = depth + 1
                            crawl_queue.append(abs_link)
            else:
                continue
        else:
            print('Blocked by robots.txt:', url)

def get_links(html):
    """ Return a list of links from html
    """
    # a regular expression to extract all links from the webpage
    webpage_regex = re.compile("""<a[^>]+href=["'](.*?)["']""",re.IGNORECASE)
    # list of all links from the webpage
    return webpage_regex.findall(html)

def get_robots_parser(robots_url):
    " Return the robots parser object using the robots_url "
    rp = robotparser.RobotFileParser()
    rp.set_url(robots_url)
    rp.read()
    return rp

class Throttle:
    """Add a delay between downloads to the same domain
    """
    def __init__(self, delay):
        # amount of delay between downloads for each domain
        self.delay = delay
        # timestamp of when a domain was last accessed
        self.domains = {}

    def wait(self, url):
        domain = urlparse(url).netloc
        last_accessed = self.domains.get(domain)
        if self.delay > 0 and last_accessed is not None:
            sleep_secs = self.delay - (time.time() - last_accessed)
            if sleep_secs > 0:
            # domain has been accessed recently so need to sleep
                time.sleep(sleep_secs)
            # update the last accessed time
        self.domains[domain] = time.time()


def download_pdf(url,html,folder=new_folder_path):
    #get current Csv file path
    tree = fromstring(html)
    anchor_list=tree.xpath("//div[@class='col-lg-12']/a")
    if anchor_list:
        #take the third element of the achor list, corresponding to the latest CSV file. NOTE that for DV-2015, this element is located at index 3
        anchor=anchor_list[2]
        abs_link = urljoin(url,anchor.get('href'))
        rawdownload_attribute= abs_link
        """
        Download csv file from link and save to folder
        """
        # Get the file name from the URL
        file_name = anchor.text
        # Join the folder name and the file name
        file_path = os.path.join(folder, file_name)
        # Send a GET request to the URL
        user_agent = '*'
        headers = {'User-Agent':user_agent}
        response = requests.get(rawdownload_attribute,headers=headers)
        # Check if the response is successful
        if response.status_code == 200:
            # Write the content of the response to a binary file
            with open(file_path, "wb") as f:
                f.write(response.content)
                print("Writing:",f.name, " from ",rawdownload_attribute)
            # Return the file path
            return file_path
        else:
            # Raise an exception if the response is not successful
            raise Exception(f"Failed to download csv from source url")
    else:
        return

def main():
    link_regex=r"ceacFY\d{2}\.html\b" 
    start_url="https://dvcharts.xarthisius.xyz/"
    link_crawler(start_url, link_regex,scrape_callback=download_pdf)
   
if __name__ == '__main__':
    main()