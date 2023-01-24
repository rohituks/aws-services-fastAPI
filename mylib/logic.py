import wikipedia


def wiki(name="War Goddess", length=1):
    """This is wikipedia fetcher"""
    my_wiki = wikipedia.summary(name, length)
    return my_wiki

def search_wiki(name):
    """Search wikipedia for names"""
    results = wikipedia.search(name)
    return results