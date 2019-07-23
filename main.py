import weather_scrapy as scrapy
import csv_writer as cw

if __name__ == "__main__":
    url = "https://karki23.github.io/Weather-Data/assignment.html"
    links = scrapy.get_all_links_from_web_page(url)
    for link in links:
        file_name = link.split("/")
        country = file_name[-1][:-5]
        file_name = "data\weather_data" + "_" + country + ".csv"
        print("Getting the data from \nLink: {} ".format(link))
        rows = scrapy.get_tabular_data_from_web_page(link)
        print("Inserting '{}' data inside {} ".format(country, file_name))
        cw.write_data_into_csv(file_name,rows[1:])
        cw.write_data_into_csv('data_all\weather_data_all.csv', rows[1:], 'a')