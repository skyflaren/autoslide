import requests
import shutil
import os
import asyncio
import httpx

class ImageScraper:
    # Image Quality: small, regular, full, raw, thumb
    def __init__(self, per_page=10, quality="thumb", download_dir="Slide Images"):
        self.queries = ["dog"]
        self.query = ""
        self.per_page = per_page
        self.quality = quality
        self.download_dir = download_dir
        self.headers = {"Accept": "*/*", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.5",
                        "Connection": "keep-alive", "Host": "unsplash.com",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0"}

    # Synchronous Methods

    def get_request(self):
        url = f"https://unsplash.com/napi/search?query={self.query}&per_page={self.per_page}"
        return requests.request("GET", url, headers=self.headers)

    def get_data(self):
        self.data = self.get_request().json()

    def scrape(self, queries):
        self.queries = queries
        ret = []
        for query in queries:
            self.query = query
            self.get_data()
            if self.data['photos']['results']:
                top_result = self.data['photos']['results'][0]
                name = top_result['id']
                url = top_result['urls'][self.quality]
                # print(f"{self.query}: ", end="")
                # print(url)
                ret.append([name, url])
            else:
                print("No results found")
        return ret

    # Asynchronous Methods WIP

    # async def get_request(self, query):
    #     async with httpx.AsyncClient() as client:
    #         url = f"https://unsplash.com/napi/search?query={query}&per_page={self.per_page}"
    #         return client.get(url, headers=self.headers)

    # async def get_data(self, query):
    #     return self.get_request(query).json()

    # async def process(self, query):
    #     data = self.get_data(query)
    #     if self.data['photos']['results']:
    #         top_result = self.data['photos']['results'][0]
    #         name = top_result['id']
    #         url = top_result['urls'][self.quality]
    #         # print(f"{self.query}: ", end="")
    #         # print(url)
    #         return [name, url]

    #     print("No results found")
    #     return []

    # async def scrape(self, queries):
    #     self.queries = queries
    #     reqs = await asyncio.gather(*(process(query) for query in self.queries))
    #     return reqs

    # Other methods

    def set_download_dir(self, download_dir):
        self.download_dir = download_dir

    def download_images(self, data):
        if not os.path.exists(self.download_dir):
            os.mkdir(self.download_dir)

        for i, items in enumerate(data):
            slide_dir = os.path.join(self.download_dir, f"Slide {i + 1}")

            # Checking if folder exists
            if not os.path.exists(slide_dir):
                os.mkdir(slide_dir)

            scraped = self.scrape(items)

            ind = 0
            for name, url in scraped:
                # print(url)
                filepath = f"{os.path.join(os.path.realpath(os.getcwd()), slide_dir, ind)}.jpg"
                ind += 1
                r = requests.get(url, stream=True)
                # print(r.status_code)
                if r.status_code == 200:
                    r.raw.decode_content = True
                    with open(filepath, "wb") as f:
                        shutil.copyfileobj(r.raw, f)
                else:
                    print("Bad request")

        print("Done")


if __name__ == "__main__":
    queries = ["cool-robot", "big-building", "supercapacitor", "ttc", "municipality", "health-insurance-plan", "majority"]
    scraper = ImageScraper(per_page=5, quality="regular")
    scraper.scrape(queries)