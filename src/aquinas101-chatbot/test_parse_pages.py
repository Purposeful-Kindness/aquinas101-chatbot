
# import the functions to test
from parse_pages import get_page, get_soup, get_youtube_url, get_urls


# write a test function to test the above functions
def test_functions():
    url = "https://aquinas101.thomisticinstitute.org/saint-and-scholar"
    page = get_page(url)
    soup = get_soup(page)
    yt_url = get_youtube_url(soup)
    urls = get_urls(soup, "aquinas101.thomisticinstitute.org")
    assert yt_url == "https://youtu.be/V_FuJXZOy90"
    assert len(urls) == 11
    assert urls[0] == "https://aquinas101.thomisticinstitute.org"
    print("All tests passed")
