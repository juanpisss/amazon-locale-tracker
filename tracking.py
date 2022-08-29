from urllib import request
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import os
import json
import tinycss

g_urls = [
"https://images-na.ssl-images-amazon.com/images/G/{}/x-locale/common/small-logo.gif",
"https://images-na.ssl-images-amazon.com/images/G/{}/ShoppingPortal/logo._TTD_.png",
"https://images-na.ssl-images-amazon.com/images/G/{}/x-locale/checkout/checkout-spc-items-banner.jpg",
"https://images-na.ssl-images-amazon.com/images/G/{}/x-locale/checkout/checkout-spc-ship-banner.jpg",
"https://images-na.ssl-images-amazon.com/images/G/{}/x-locale/checkout/checkout-spc-address-banner.gif",
"https://images-na.ssl-images-amazon.com/images/G/{}/x-locale/checkout/checkout-spc-taxinformation-banner.png",
"https://images-na.ssl-images-amazon.com/images/G/{}/x-locale/checkout/checkout-spc-pay-banner.jpg",
"https://images-na.ssl-images-amazon.com/images/G/{}/checkout/payselect/progressbar-payments.gif",
"https://images-na.ssl-images-amazon.com/images/G/{}/x-locale/checkout/confirm-banner.gif",
"https://images-na.ssl-images-amazon.com/images/G/{}/x-locale/checkout/truespc/secured-ssl.png",
"https://images-na.ssl-images-amazon.com/images/G/{}/gno/sprites/nav-sprite-global_bluebeacon-1x_optimized_layout1.png",
"https://images-na.ssl-images-amazon.com/images/G/{}/gno/sprites/nav-sprite-global-1x-hm-dsk-reorg.png",
"https://images-na.ssl-images-amazon.com/images/G/{}/gno/sprites/nav-sprite-global-2x-hm-dsk-reorg.png",
"https://images-na.ssl-images-amazon.com/images/G/{}/gno/sprites/timeline_sprite_1x.png",
"https://images-na.ssl-images-amazon.com/images/G/{}/gno/sprites/timeline_sprite_2x.png",
"https://images-na.ssl-images-amazon.com/images/G/{}/payments-portal/r1/issuer-images/sprite-map.png",
"https://images-na.ssl-images-amazon.com/images/G/{}/x-locale/common/buttons/continue-shopping.gif",
"https://images-na.ssl-images-amazon.com/images/G/{}/x-locale/common/amazon-logo.gif",
"https://images-na.ssl-images-amazon.com/images/G/{}/x-locale/common/amazon-logo-tiny.gif",
"https://m.media-amazon.com/images/G/{}/marketing/prime/new_prime_logo_RGB_blue.png",
"https://m.media-amazon.com/images/G/{}/x-locale/cs/te/logo.png",
"https://m.media-amazon.com/images/G/{}/marketing/prime/CTYP/primelogoblue.png",
"https://m.media-amazon.com/images/G/{}/advantage/vendor-central/site-logo.jpg",
"https://images-na.ssl-images-amazon.com/images/G/{}/error/logo._TTD_.png",
"https://images-na.ssl-images-amazon.com/images/G/{}/error/title._TTD_.png",
"https://images-na.ssl-images-amazon.com/images/G/{}/error/500-title._TTD_.png",
"https://images-na.ssl-images-amazon.com/images/G/{}/rainier/nav/sc-unified.png"
]
seller_logo = "https://m.media-amazon.com/images/G/01/sell/navigation/logos/amazon{TLD}-half-logo.svg"
bs4_urls = [
    "https://www.amazon.com/customer-preferences/country",
    "https://sell.amazon.com/"
]
relevant_urls = [
    "https://m.media-amazon.com/images/G/01/magicarp/common/Amazon_Carrier_Standard_Operating_Procedure_SOP_Pan-EU_NGAmazon.pdf",

    # Colombia
    "https://sellercentral.amazon.com.co/",
    "https://images-na.ssl-images-amazon.com/images/G/01/magicarp/common/Carrier_Central_Manual_COAmazon.pdf",
    "https://vendorcentral.amazon.com.co/",
    "https://brandregistry.amazon.com.co/",
    "https://affiliate-program.amazon.com.co/",
    "http://vender.amazon.com.co/",
    # Chile
    "https://sellercentral.amazon.cl/",
    "https://images-na.ssl-images-amazon.com/images/G/01/magicarp/common/Carrier_Central_Manual_CLAmazon.pdf",
    "https://vendorcentral.amazon.cl/",
    "https://brandregistry.amazon.cl/",
    "https://affiliate-program.amazon.cl/",
    "http://vender.amazon.cl/",

    # Nigeria
    "https://sellercentral.amazon.com.ng/",
    "https://images-na.ssl-images-amazon.com/images/G/01/magicarp/common/Carrier_Central_Manual_NGAmazon.pdf",
    "https://vendorcentral.amazon.com.ng/",
    "https://brandregistry.amazon.com.ng/",
    "https://affiliate-program.amazon.com.ng/",

    # South Africa
    "https://sellercentral.amazon.co.za/",
    "https://images-na.ssl-images-amazon.com/images/G/01/magicarp/common/Carrier_Central_Manual_ZAAmazon.pdf",
    "https://vendorcentral.amazon.co.za/",
    "https://brandregistry.amazon.co.za/",
    "https://affiliate-program.amazon.co.za/"

]

def scrape(url, mode=""):
    print(url)
    resp = request.urlopen(url)
    html = resp.read().decode("utf8")
    soup = BeautifulSoup(html)

    match mode:
        case "customer-preferences":
            css_url = soup.find_all("link", rel="stylesheet")[1]["href"]
            css_data = request.urlopen(css_url).read().decode("utf8")
            stylesheet = tinycss.make_parser().parse_stylesheet(css_data)
            
            for rule in stylesheet.rules:
                for selector in rule.selector:
                    try: 
                        value = selector.value
                        if value == "icp-nav-globe-img-2":
                            for declaration in rule.declarations:
                                for tok in declaration.value:
                                    if tok.type == "URI":
                                        sprite_flag_url = tok.value
                    except Exception: 
                        pass
 
            request.urlretrieve(css_url, "css/customer-preferences/cp_css.css")
            request.urlretrieve(sprite_flag_url, "css/customer-preferences/cp_sprite.png")
        case "seller-central":
            css_url = soup.find_all("link", rel="stylesheet")[1]["href"]
            flag_sprites_url = "https://m.media-amazon.com/images/G/01/sell/navigation/flags/flag-sprite.svg"

            request.urlretrieve(css_url, "css/seller-central/sc_css.css")
            request.urlretrieve(flag_sprites_url, "css/seller-central/sc_flag_sprites.svg")

def download(url, loc=None):
    try:
        request.urlopen(url)
        if loc == None:
            loc = urlparse(url).path[1:]
            try:
                subdirs = os.path.split(loc)
                os.makedirs(subdirs[0])
            except Exception: # subdirectory already exists
                pass
        print(loc)
        request.urlretrieve(url, loc)
        print(url)
    except Exception as e: # 404
        return

if __name__ == "__main__":
    print("Initiating with /G/Locales...")
    for locale in range(1, 100):
        if locale <= 9:
            locale = f"0{locale}"
            print(locale)
        else:
            print(locale)
        for url in g_urls:
            url = url.format(locale)
            download(url)
    
    print("Continuing with Seller Logos...")
    with open("tlds.json", "r") as f:
        data = json.load(f)
    for country in data:
        for tld in data[country]:
            tld = tld.replace(".", "-")
            url = seller_logo.format(TLD=tld)
            filename = os.path.split(url)[1]
            download(url, loc=f"seller_logos/{filename}")
    
    print("Continuing with relevant URLs...")
    # will always be a 404/501 until god knows when
    for url in relevant_urls:
        filename = os.path.split(url)[1]
        download(url, f"relevant/{filename}")
    
    print("Finishing with CSS sprites...")
    scrape(bs4_urls[0], mode="customer-preferences")
    scrape(bs4_urls[1], mode="seller-central")