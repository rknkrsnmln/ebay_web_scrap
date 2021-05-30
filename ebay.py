import csv
from bs4 import BeautifulSoup
import requests
from decimal import Decimal

barang = input('Masukan Nama Barang: \n')
berbintang = input('Cari Yang berbintang ? y/n \n')
gratis_ongkir = input('Geratis ongkir ? y/n \n')
harga_maks = Decimal(input('Masukan harga maksimum \n'))
csv_file = open('hasil_ebay_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(
    ['Nama', 'Harga', 'Biaya Kirim', 'Ket. Tambahan', 'Tautan'])


for i in range(1, 5):
    url = requests.get(
        'https://www.ebay.com/sch/i.html?_nkw=' + barang + '&_pgn=' + str(i)).text
    soup = BeautifulSoup(url, 'html.parser')
    hasil = soup.find_all('li', class_='s-item')
    for item in hasil:
        nama = item.h3.text
        harga = item.find('span', class_='s-item__price')
        kurir = item.find(
            'span', class_='s-item__shipping s-item__logisticsCost')
        tautan = item.find('a', class_='s-item__link')['href']
        bintang = item.find('span', class_='clipped')
        if None in (nama, harga, bintang, kurir, tautan):
            continue
        harga_str = harga.text.replace('IDR', '').replace(
            ',', '').strip()
        if ' to ' in harga_str:
            harga_int = Decimal(harga_str.split('to')[0])
        else:
            harga_int = Decimal(harga_str)
        if harga_int <= harga_maks:
            if gratis_ongkir == 'y':
                if 'Free Shipping' in kurir.text:
                    print(nama)
                    print(harga_int)
                    print(kurir.text)
                    print(bintang.text)
                    print(tautan)
                    print("================================================")
                    csv_writer.writerow(
                        [nama, harga_int, kurir.text, bintang.text, tautan])
            if berbintang == 'y':
                if 'stars' in bintang.text:
                    print(nama)
                    print(harga_int)
                    print(kurir.text.replace('IDR', '').replace(',', '').strip())
                    print(bintang.text)
                    print(tautan)
                    print("================================================")
                    csv_writer.writerow(
                        [nama, harga_int, kurir.text, bintang.text, tautan])
            else:
                print(nama)
                print(harga_int)
                print(kurir.text.replace('IDR', '').replace(',', '').strip())
                print(bintang.text)
                print(tautan)
                print("================================================")
                csv_writer.writerow(
                    [nama, harga_int, kurir.text, bintang.text, tautan])

   
   
#    dibawah ini hanya contoh saja, aktifkan kode yang diatas
    # url = requests.get(
    #     'https://www.ebay.com/sch/i.html?_nkw=' + barang + '&_pgn=1').text
    # soup = BeautifulSoup(url, 'html.parser')
    # hasil = soup.find_all('li', class_='s-item')
    # for item in hasil:
    #     bintang = item.find('span', class_='clipped')
    #     if bintang is None:
    #         continue
    #     else:
    #         if 'stars' in bintang.text:
    #             print(bintang)
    #         else:
    #             continue
    # if bintang is not None:
    #     if 'out of' in bintang:
    #         print(bintang)
    # else:
    #     continue
