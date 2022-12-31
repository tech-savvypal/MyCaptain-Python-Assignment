#Web scraper using BeautifulSoup4 and requests
import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import connect
parser=argparse.ArgumentParser()
parser.add_argument("--page_num_max", help="Enter the number of pages to parse", type=int)
parser.add_arugment("--dbname", help="Enter the name of db", type=str)
args=parser.parse_args()
oyo_url="https://www.oyorooms.com/search?location=Bangalore%2C%20Karnataka%2C%20India&city=Bangalore&searchType=city&coupon=&checkin=31%2F12%2F2022&checkout=01%2F01%2F2023&roomConfig%5B%5D=2&showSearchElements=false&country=india&guests=2&rooms=1&filters%5Bcity_id%5D=4"
page_num_Max=args.page_num_max
scraped_info_list=[]
connect.connect(args.dbname)
for page_num in range(1,page_num_Max):
    url=oyo_url+str(page_num)
    print("Get request for: "+url)
    req=requests.get(oyo_url + str(page_num))
    content=req.content
    soup=BeautifulSoup(content,"html.parser")
    all_hotels=soup.find_all("div",{"class":"hotelCardListing"})
    for hotel in all_hotels:
        hotel_dict={}
        hotel_dict["name"]=hotel.find("h3",{"class":"listingHotelDescription__hotelName"}).text
        hotel_dict["address"]=hotel.find("span",{"itemprop":"streetAddress"}).text
        hotel_dict["price"]=hotel.find("span",{"class":"listingPrice__finalPrice"}).text
        try:
            hotel_dict["rating"]=hotel.find("span",{"class":"hotelRating__ratingSummary"}).text
        except AttributeError:
            pass
        parent_amenities_element=hotel.find("div",{"class":"amenityWrapper"})
        amenities_list=[]
        for amenity in parent_amenities_element.find_all("div",{"class":"amenityWrapper__amenity"}):
            amenities_list.append(amenity.find("spam",{"class":"d-body-sm"}).text.strip())
        hotel_dict["amenities"]=', '.join(amenities_list[:-1])
        scraped_info_list.append(hotel.dict)
        connect.insert_into_table(args.dbname,tuple(hotel_dict.values()))
dataFrame=pandas.DataFrame(scraped_info_list)
dataFrame.to_csv("Oyo.csv")
connect.get_hotel_info(args.dbname)