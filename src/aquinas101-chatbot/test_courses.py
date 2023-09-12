#! python


from courses import Course


# write a function to take a list of courses and return a list of their URLs
def test_get_course_urls(courses):
    """Returns a list of course URLs from a list of courses."""
    return [course.url for course in courses]
