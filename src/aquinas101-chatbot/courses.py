#! python

from parse_pages import get_page, get_soup, get_youtube_url, get_urls
from dataclasses import dataclass


COURSE_PAGE_URL = "https://aquinas101.thomisticinstitute.org/an-introduction-to-the-summa"

# write a class for a Lesson that will have multiple types of content
@dataclass
class Lesson:
    """A class to represent a lesson."""

    URL: str
    course_num: int
    lesson_num: int
    course_link: object
    title: str

    def __str__(self):
        """Return a string representation of the Lesson class."""
        return f"Lesson({self.url})"

    def __repr__(self):
        """Return a string representation of the Lesson class."""
        return f"Lesson({self.title})"


# write a new class that will be used to store a course and all its content
@dataclass
class Course:
    """A class to represent a course."""

    lessons: list[object]
    URL: str
    title: str

    def __init__(self, url):
        """Initialize the Course class."""
        self.url = url
        self.page = get_page(url)
        self.soup = get_soup(self.page)
        self.yt_url = get_youtube_url(self.soup)
        self.urls = get_urls(self.soup, "aquinas101.thomisticinstitute.org")

    def __str__(self):
        """Return a string representation of the Course class."""
        return f"Course({self.url})"

    def __repr__(self):
        """Return a string representation of the Course class."""
        return f"Course({self.title})"
