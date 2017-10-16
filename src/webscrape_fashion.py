import scipy as sp
import PIL
import numpy as np
from selenium import webdriver
import time
import boto3
from multiprocessing.dummy import Pool
import pymongo
import mongo_fashion


def scrape_fitnyc(self):
    anchor = "td.primaryMediaClass > a"
    image_links = b.find_elements_by_css_selector(anchor)

    objs = []
    for i in range(len(image_links)):
        try:
            obj_links = "td.primaryMediaClass > a"
            image_links = b.find_elements_by_css_selector(obj_links)
            image_link = image_links[i]

            obj = {}
            image_link.click()
            time.sleep(5)

            obj_img = "div#singlemedia > div > a > img"
            img = b.find_element_by_css_selector(obj_img)
            pic = PIL.Image.open(img)
            obj['image'] = np.array(pic)

            obj_name = "div#singledata div.objname"
            obj['name'] = b.find_element_by_css_selector(obj_name).text

            obj_labels = "div#singledata div.paragraph"
            data = b.find_elements_by_css_selector(obj_labels)
            for item in (p.text for p in data):
                if ": " in item:
                    k, v = item.split(": ")
                    obj[k.lower()] = v
                else:
                    k, v = item
                    obj['description'] = v

            if 'object number' in obj:
                filename = f"fitnyc_{obj['object number']}_{obj['date']}.png"

            insert_db(objs.append(obj))

        except Exception as e:
            print(repr(e))
        finally:
            b.back()
            time.sleep(5)


def run_scrape(url):
    b.get(url)
    scrape_fitnyc()


def pool_scrape():
    pool = Pool(20)
    pool.map(run_scrape, url_list_1900_to_present)



url_list_1900_to_present = ["http://fashionmuseum.fitnyc.edu/view/objects/aslist/760/0/dynasty-desc?t:state:flow=2e22af4a-785f-4810-b535-e2f2d8d6a954",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/760/25/dynasty-desc?t:state:flow=4a3332f7-2729-4f0d-b846-b2b3e2991c01",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/761/0/dynasty-desc?t:state:flow=6e74c025-032e-48a0-a5a2-9575fd0182e7",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/761/25/dynasty-desc?t:state:flow=410ed3ca-1a4e-4086-a85f-c57cfc506c11",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/761/50/dynasty-desc?t:state:flow=e94a3212-b7a0-4dc6-94e8-47956090f549",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/761/75/dynasty-desc?t:state:flow=7219a422-fe36-471a-917e-ee7d70fd30e7",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/761/100/dynasty-desc?t:state:flow=dc072027-59f8-44c5-b549-ae5d283d7b33",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/762/0/dynasty-desc?t:state:flow=764a7190-fe1f-4f8e-b3d8-e3c82f1c75bc",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/762/25/dynasty-desc?t:state:flow=97490e37-a5e7-4d0a-9c35-32c4360ebbe4",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/762/50/dynasty-desc?t:state:flow=6a0e883a-0081-4946-a1d8-92e200d0844f",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/763/0/dynasty-desc?t:state:flow=5600c02a-91b0-4c83-968d-699f0f47324d",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/763/25/dynasty-desc?t:state:flow=1e11b6e7-0259-4045-9168-a10520e9a89b",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/763/50/dynasty-desc?t:state:flow=f3e609c4-7db8-4ab2-89f4-12f5eb3d6ff7",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/763/75/dynasty-desc?t:state:flow=4cc98a82-29c1-4043-b10b-881cd8a09af6",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/764/0/dynasty-desc?t:state:flow=49e72127-80f0-4eff-8a3c-276f6c4fbaa3",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/764/25/dynasty-desc?t:state:flow=68bd1b8d-e7c1-4d27-ae04-0f5ca64caf2d",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/764/50/dynasty-desc?t:state:flow=9e4e939d-7073-4bff-864d-ab8abf2644fc",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/764/75/dynasty-desc?t:state:flow=41ee7ac6-4620-4656-9eda-f24332b4d1be",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/764/100/dynasty-desc?t:state:flow=b0236e05-e77e-466d-bc8e-326ffe0cd2bf",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/764/125/dynasty-desc?t:state:flow=682a2275-2def-47fc-bf52-9f60a05da6ab",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/764/125/dynasty-desc?t:state:flow=682a2275-2def-47fc-bf52-9f60a05da6ab",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/764/150/dynasty-desc?t:state:flow=544b6985-f096-4959-9618-38ac6e8f77bd",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/764/175/dynasty-desc?t:state:flow=49956835-6bcf-40f3-aeb5-af57e339aaaf",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/765/0/dynasty-desc?t:state:flow=6b39479c-dce4-4a1b-b9ad-26e06823a034",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/765/25/dynasty-desc?t:state:flow=3a497a4e-20a2-49d8-bdce-ee7da4f08921",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/765/50/dynasty-desc?t:state:flow=84d19ddb-dd9c-4128-8d5f-52d4095227df",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/765/75/dynasty-desc?t:state:flow=bca5dba2-66b8-4104-b2c7-16bba7dd2ec6",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/766/0/dynasty-desc?t:state:flow=6402ffe9-869d-466a-a0d1-fae389478fe0",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/766/25/dynasty-desc?t:state:flow=18e2cb4f-cfc3-4b41-9abd-410a504bc684",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/766/50/dynasty-desc?t:state:flow=e2ce32eb-230d-4ada-b070-2f98e8e86f92",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/766/75/dynasty-desc?t:state:flow=7250d9ee-bfd3-4025-a0e2-6f000835ac75",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/767/0/dynasty-desc?t:state:flow=397c4f4f-7fc5-434a-a35e-fd197d0d19fc",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/767/25/dynasty-desc?t:state:flow=8214e270-d4b7-486e-be8d-0da2e1cd49d9",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/767/50/dynasty-desc?t:state:flow=fb03552b-35da-4e81-8d63-d5a87d2c3162",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/767/75/dynasty-desc?t:state:flow=0d2b3b94-56d9-49e4-b997-103d5c3d697e",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/767/100/dynasty-desc?t:state:flow=037e4668-72df-4f87-9d45-197d6473d562",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/831/0/dynasty-desc?t:state:flow=585c202d-8182-4954-b071-8159a5711ed8",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/831/25/dynasty-desc?t:state:flow=243ec510-a111-4c86-b016-c0d43e84bd4e",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/831/50/dynasty-desc?t:state:flow=ed1ad330-9d36-40d5-a529-85e24f53f276",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/831/75/dynasty-desc?t:state:flow=c63f8b7a-538c-4fd8-95ca-2c73f11c62d0",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/831/100/dynasty-desc?t:state:flow=cbffcae1-1d3f-4a63-80cf-3462dd2f71c5",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/831/125/dynasty-desc?t:state:flow=5c8f8ac5-8288-48b1-b14b-569dbe53e26e",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/830/0/dynasty-desc?t:state:flow=3a6d0fb2-f214-4e3c-9b8a-5b8d68d5b32e",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/830/25/dynasty-desc?t:state:flow=7426793e-bac9-4f0a-a536-a877fc8bc281",
                            "http://fashionmuseum.fitnyc.edu/view/objects/aslist/830/50/dynasty-desc?t:state:flow=d9177b4e-0fc8-4dd5-8247-a32b9c7fd44e"
                            ]
pool_scrape()
