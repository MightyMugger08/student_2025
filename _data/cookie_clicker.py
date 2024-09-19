import time

class CookieClicker:
    def __init__(self):
        self.cookies = 0
        self.cookies_per_click = 1

    def click(self):
        self.cookies += self.cookies_per_click
        print(f"You clicked! You now have {self.cookies} cookies.")

    def buy_upgrade(self):
        if self.cookies >= 10:
            self.cookies -= 10
            self.cookies_per_click += 1
            print(f"Upgrade bought! Cookies per click is now {self.cookies_per_click}.")
        else:
            print("Not enough cookies to buy upgrade.")

    def status(self):
        print(f"Cookies: {self.cookies}")
        print(f"Cookies per click: {self.cookies_per_click}")

def main():
    game = CookieClicker()
    
    while True:
        print("\n1. Click for cookies")
        print("2. Buy upgrade (10 cookies)")
        print("3. Show status")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            game.click()
        elif choice == '2':
            game.buy_upgrade()
        elif choice == '3':
            game.status()
        elif choice == '4':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

        time.sleep(1)  # Slow down the loop to make it more readable

if __name__ == "__main__":
    main()
