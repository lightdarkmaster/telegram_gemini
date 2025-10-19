import pyautogui
import time
import random

# ====== SETTINGS ======
num_inquiries = 100        # Number of inquiries to send
start_delay = 5            # Delay before starting (in seconds)Inquiry #6: Do you sell watches and jewelry?
interval = 10             # Delay between each message
# =======================

inquiries = [
    "Do you have discounts on clothing today?",
    "What time does your store close?",
    "Are there any new arrivals in the women's section?",
    "Can I return an item without a receipt?",
    "Do you sell branded perfumes?",
    "Is there a sale on electronics right now?",
    "Where can I find men's formal wear?",
    "Do you have size 9 sneakers available?",
    "Is there a fitting room near the shoe section?",
    "Can I use my loyalty points for online purchases?",
    "Do you offer gift wrapping services?",
    "When is your next clearance sale?",
    "Do you accept credit card payments?",
    "Are there any promo codes available today?",
    "Can I reserve an item over the phone?",
    "Do you have eco-friendly shopping bags?",
    "Is parking free for shoppers?",
    "Do you have a lost and found department?",
    "Can I return online purchases in-store?",
    "Do you offer student discounts?",
    "Where is the customer service counter?",
    "Do you have layaway plans?",
    "Are pets allowed inside the store?",
    "Is there an ongoing sale in the home section?",
    "Do you sell kitchen appliances?",
    "Can I get a refund for damaged items?",
    "Do you have kids' school uniforms?",
    "Can I check if an item is available before visiting?",
    "Do you offer alteration services?",
    "Is there a restroom for customers?",
    "Can I get a replacement for a defective item?",
    "Do you offer senior citizen discounts?",
    "Can I get updates about new promotions?",
    "Do you sell mobile phone accessories?",
    "Is there an ATM inside the store?",
    "Do you provide delivery services?",
    "Can I use GCash or Maya for payment?",
    "Is there a dress code for entering the store?",
    "Do you sell cosmetics and skincare items?",
    "Can I exchange an item I bought last week?",
    "Do you have a loyalty membership program?",
    "Can I use multiple vouchers in one purchase?",
    "Do you offer same-day delivery?",
    "Are there any promos for household items?",
    "Is there a section for imported goods?",
    "Do you have furniture on display?",
    "Can I order online and pick up in-store?",
    "Do you sell gift cards?",
    "Is your toy section open today?",
    "Can I get assistance finding a product?",
    "Do you have a customer feedback form?",
    "Are you hiring new staff currently?",
    "Do you sell watches and jewelry?",
    "Can I get an installment plan for appliances?",
    "Is there a sale for home décor items?",
    "Do you have a maternity section?",
    "Can I exchange gifts after Christmas?",
    "Do you sell books or stationery?",
    "Is the food court open right now?",
    "Do you provide shopping assistance for seniors?",
    "Are there exclusive deals for members?",
    "Can I order through your website?",
    "Do you offer free samples for cosmetics?",
    "Is there a baby section in your store?",
    "Do you sell travel luggage?",
    "Can I pre-order out-of-stock items?",
    "Do you validate parking tickets?",
    "Do you sell kitchen utensils?",
    "Can I use a foreign credit card?",
    "Are there ongoing deals for couples or families?",
    "Do you provide student IDs for discounts?",
    "Is there an information desk near the entrance?",
    "Do you sell electronics accessories?",
    "Do you provide installation for appliances?",
    "Can I get a store catalog?",
    "Do you have a section for local brands?",
    "Is there a 24-hour branch nearby?",
    "Do you offer curbside pickup?",
    "Are you open during holidays?",
    "Do you sell bedsheets and blankets?",
    "Can I buy items in bulk for discounts?",
    "Do you have return policy information online?",
    "Do you accept digital receipts?",
    "Do you sell hair care products?",
    "Can I use a discount coupon on sale items?",
    "Is there a cashier on the 2nd floor?",
    "Do you sell perfumes for men?",
    "Do you have a repair service for watches?",
    "Can I buy display items?",
    "Do you offer a rewards program for frequent shoppers?",
    "Do you have sections for imported snacks?",
    "Is there a self-checkout counter?",
    "Can I pre-book items before they go on sale?",
    "Do you sell seasonal decorations?",
    "Do you have fitness or sports gear?",
    "Can I check prices online?",
    "Do you provide receipts via email?",
    "Do you sell small kitchen appliances?",
    "Do you have a section for clearance items?",
    "Are you open on Sundays?",
    "Can I get directions to your store?",
    "Do you have free WiFi in the store?",
    "Do you sell sunglasses and eyewear?",
]

# Shuffle inquiries (optional)
random.shuffle(inquiries)

print(f"Starting in {start_delay} seconds...")
print("Click the chat or message box where you want to send the messages.")
time.sleep(start_delay)

for i, inquiry in enumerate(inquiries[:num_inquiries], start=1):
    # message = f"Inquiry #{i}: {inquiry}"
    message = inquiry
    pyautogui.typewrite(message)
    pyautogui.press('enter')
    print(f"✅ Sent: {message}")
    time.sleep(interval)

print("🎉 All 100 unique department store inquiries have been sent successfully.")
