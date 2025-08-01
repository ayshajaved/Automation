import requests
from bs4 import BeautifulSoup
import random
import time
from plyer import notification

'''
Web scraping + Automation
'''
def get_random_quote():
    try:
        response = requests.get("http://quotes.toscrape.com/tag/love")
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("div", class_="quote")
        if not quotes:
            return "Error", "Unknown", "No quote found."
        quote = random.choice(quotes)
        text = quote.find("span", class_="text").text.strip()[:200]
        author = quote.find("small", class_="author").text.strip()
        return f"Love Quote #{random.randint(1, 100)}", author, text
    except:
        return "Error", "Unknown", "Could not fetch quote."

def send_notification(title, message):
    try:
        notification.notify(
            title=title,
            message=message,
            app_name="Love Quotes",
            timeout=15
        )
    except:
        print("Notification failed.")

def main():
    try:
        interval = float(input("Interval (minutes, e.g., 60): ")) * 60
        num_quotes = int(input("Number of quotes: "))
        if interval <= 0 or num_quotes <= 0:
            print("Please enter positive numbers.")
            return
    except:
        print("Invalid input. Use numbers.")
        return

    print(f"Sending quotes every {interval/60} minutes.")
    for i in range(num_quotes):
        title, author, text = get_random_quote()
        message = f"By {author}\n{text}"
        send_notification(title, message)
        print(f"Sent: {title} - {message}")
        time.sleep(interval)
    print("Finished sending quotes.")

if __name__ == "__main__":
    main()