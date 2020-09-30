from main.models import (Auction, AuctionLot, Artwork, ArtImage, Artist)

DEPARTMENTS = [
    ("Contemporary Art", "00000164-609b-d1db-a5e6-e9ff01230000"),
    ("Impressionist & Modern Art", "00000164-609b-d1db-a5e6-e9ff08ab0000"),
    ("Chinese Works of Art", "00000164-609b-d1db-a5e6-e9ff0b150000"),
    ("19th Century European Paintings", "00000164-609a-d1db-a5e6-e9fff79f0000"),
    ("19th Century Furniture & Sculpture", "00000164-609b-d1db-a5e6-e9ff043c0000"),
    ("20th Century Design", "00000164-609a-d1db-a5e6-e9fffe5f0000"),
    ("Aboriginal Art", "00000164-609a-d1db-a5e6-e9ffff8d0000"),
    ("African & Oceanic Art", "00000164-609b-d1db-a5e6-e9ff01850000"),
    ("African Modern & Contemporary Art", "00000164-609a-d1db-a5e6-e9fffdf80000"),
    ("American Art", "00000164-609b-d1db-a5e6-e9ff0a800000"),
    ("Ancient Sculpture and Works of Art", "00000164-609a-d1db-a5e6-e9fff35f0000"),
    # ("Automobiles | RM Sotheby's", "00000164-609a-d1db-a5e6-e9fffd920000"),
    # ("Books & Manuscripts", "00000164-609b-d1db-a5e6-e9ff03270000"),
    ("British Paintings 1550-1850", "00000164-609b-d1db-a5e6-e9ff06270000"),
    ("British Watercolours & Drawings 1550-1850", "00000164-609a-d1db-a5e6-e9fff8660000"),
    ("Canadian Art", "00000164-609a-d1db-a5e6-e9fffffb0000"),
    ("Chinese Paintings – Classical", "00000164-609b-d1db-a5e6-e9ff08440000"),
    ("Chinese Paintings – Modern", "00000164-609b-d1db-a5e6-e9ff0ba60000"),
    # ("Clocks & Barometers", "00000164-609b-d1db-a5e6-e9ff00600000"),
    # ("Coins and Medals", "00000164-609b-d1db-a5e6-e9ff0c320000"),
    ("Contemporary Arab, Iranian & Turkish Art", "00000164-609a-d1db-a5e6-e9fffd2c0000"),
    ("Contemporary Ink Art", "00000164-609a-d1db-a5e6-e9fff6760000"),
    ("English Furniture", "00000164-609b-d1db-a5e6-e9ff0b610000"),
    ("European Ceramics", "00000164-609a-d1db-a5e6-e9fff9320000"),
    ("European Sculpture & Works of Art", "00000164-609a-d1db-a5e6-e9fffa760000"),
    ("French & Continental Furniture", "00000164-609b-d1db-a5e6-e9ff0bec0000"),
    # ("Handbags and Accessories", "0000016d-01ed-d6c8-a77d-19ff8f010001"),
    # ("House Sales & Private Collections", "00000164-609a-d1db-a5e6-e9fffa0b0000"),
    ("Indian, Himalayan & Southeast Asian Art", "00000164-609a-d1db-a5e6-e9ffff270000"),
    ("Indian & South Asian Modern & Contemporary Art", "00000164-609b-d1db-a5e6-e9ff07220000"),
    ("Irish Art", "00000164-609b-d1db-a5e6-e9ff068c0000"),
    ("Islamic Art", "00000164-609b-d1db-a5e6-e9ff09100000"),
    ("Israeli & International Art", "00000164-609b-d1db-a5e6-e9ff055d0000"),
    ("Japanese Art", "00000164-f0d1-d221-a575-f2fda8e90000"),
    ("Judaica", "00000164-609a-d1db-a5e6-e9fffb460000"),
    ("Latin American Art", "00000164-609b-d1db-a5e6-e9ff0a350000"),
    # (" Luxury Collectibles", "0000016d-16fd-d23f-affd-f6fdebac0001"),
    ("Modern & Contemporary Southeast Asian Art", "00000164-609b-d1db-a5e6-e9ff04fc0000"),
    ("Modern & Post-War British Art", "00000164-609b-d1db-a5e6-e9ff02b50000"),
    ("Modern Asian Art", "00000164-609a-d1db-a5e6-e9fff8ca0000"),
    # ("Musical Instruments", "00000164-609a-d1db-a5e6-e9fffc6a0000"),
    ("Objects of Vertu", "00000164-609a-d1db-a5e6-e9fff4f10000"),
    ("Old Master Drawings", "00000164-609b-d1db-a5e6-e9ff07e20000"),
    ("Old Master Paintings", "00000164-609a-d1db-a5e6-e9fffadc0000"),
    ("Orientalist Paintings", "00000164-609a-d1db-a5e6-e9fff5b50000"),
    ("Photographs", "00000164-609a-d1db-a5e6-e9fff73c0000"),
    ("Pre-Columbian Art", "00000164-609b-d1db-a5e6-e9ff03900000"),
    ("Prints", "00000164-609b-d1db-a5e6-e9ff09a60000"),
    # ("Rugs & Carpets", "00000164-609b-d1db-a5e6-e9ff09ed0000"),
    ("Russian Art", "00000164-609a-d1db-a5e6-e9fffec40000"),
    ("Scottish Art", "00000164-609a-d1db-a5e6-e9fff3c20000"),
    # ("Silver", "00000164-609a-d1db-a5e6-e9fffba40000"),
    # ("Special Projects", "00000164-609b-d1db-a5e6-e9ff049d0000"),
    # ("Spirits", "0000016d-6f17-ddcf-a3ed-ff7fde360000"),
    # ("Stamps", "00000164-609b-d1db-a5e6-e9ff024e0000"),
    ("Swiss Art", "00000164-609b-d1db-a5e6-e9ff0acd0000"),
    ("Victorian, Pre-Raphaelite & British Impressionist Art", "00000164-609a-d1db-a5e6-e9fff6150000"),
    # ("Wine & Spirits", "00000164-609a-d1db-a5e6-e9fffcc80000"),
]

BASE_URL = "https://www.sothebys.com/en/results"
def build_url():
    return "?".join([BASE_URL,
                     "&".join(["from=",
                               "to="] + [f"f2={d[1]}" for d in DEPARTMENTS])])
                               
def get_auctions():
    page = 1