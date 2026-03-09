import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.in/Nike-REVOLUTION-7-WHITE-RED-BLACK-PHOTON-DUST-FB2207-102-9UK/dp/B0CZDDLCPX/ref=zg_bs_c_shoes_d_sccl_2/523-4112886-7711507?pd_rd_w=SMk83&content-id=amzn1.sym.b908f532-cbe7-4274-8b24-b671acc58bd2&pf_rd_p=b908f532-cbe7-4274-8b24-b671acc58bd2&pf_rd_r=N4ZVKJ56RS4Z02SJREMH&pd_rd_wg=pRWaa&pd_rd_r=ec3bf1c7-1008-43e4-a090-442e4fec7d40&pd_rd_i=B0CZDDLCPX&psc=1"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

reviews = soup.select(".review-text-content span")

for r in reviews:
    print(r.get_text(strip=True)) 