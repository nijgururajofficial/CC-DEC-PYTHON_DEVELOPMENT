import pyshorteners as ps


def urlshortner():
    s = ps.Shortener(api_key='55cd8314adba3c11bbd147738ca6796420d06044')
    long_link = input("Enter the link: ")
    try:
        short_url = s.bitly.short(long_link)
        print(short_url)
    except:
        print("Enter valid url")

if __name__ == "__main__":
    urlshortner()

