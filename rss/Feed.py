import feedparser
import datetime
import dateutil.parser as parser
import locale
locale.setlocale(locale.LC_TIME,'')

class Feed:

    def __init__(self, url):
        try:
            self.data = feedparser.parse(url)
        except:
            print("Error trying to parse given URL.")
    
    def getTitle(self):
        """ Returns the feed's title """
        try:
            title = self.data.feed.title
        except:
            title = "No title"
        finally:
            return title
    
    def getLink(self):
        """ Returns the feed's link """
        try:
            link = self.data.feed.link
        except:
            link = "No link"
        finally:
            return link
    
    def getDescription(self):
        """ Returns the feed's description """
        try:
            description = self.data.feed.description
        except:
            description = "No description"
        finally:
            return description

    def getPublished(self):
        """ Returns the feed's published date """
        try:
            published = parser.parse(self.data.feed.published).strftime("%A %d-%m-%Y").capitalize()
        except:
            published = "No date"
        finally:
            return published

    def getEntry(self, idx):
        """ Returns the feed's entry of index idx """
        try:
            entry = self.data.entries[idx]
            try:
                title = entry.title
            except:
                title = "No title"
            try:
                link = entry.link
            except:
                link = "No link"
            try:
                description = entry.description
            except:
                description = "No description"
            try:
                published = entry.published
            except:
                published = "No published date"
            entry = Entry(title, link, description, published)        
        except:
            entry = Entry("No title", "No link", "No description", "No published date")
        finally:
            return entry
    
    def getLength(self):
        """ Returns the length of the feed """
        try:
            length = len(self.data.entries)
        except:
            length = 0
        finally:
            return length
    
    def getEntries(self):
        """ Returns the feed' entries as a list """
        entries = []
        for idx in range(self.getLength()):
            entries.append(self.getEntry(idx))
        return entries

class Entry:
    
    def __init__(self, title, link, description, published):
        self.title = title
        self.link = link
        self.description = description
        self.published = published
    
    def getTitle(self):
        """ returns entry's title """
        return self.title
    
    def getLink(self):
        """ returns entry's link """
        return self.link
    
    def getDescription(self):
        """ returns entry's description """
        return self.description
    
    def getPublished(self):
        """ returns entry's published date """
        return parser.parse(self.published).strftime("%A %d-%m-%Y").capitalize()