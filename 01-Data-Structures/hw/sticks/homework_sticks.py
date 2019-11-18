wine_json1 = "winedata_1.json"
wine_json2 = "winedata_2.json"
wine_full_json = "winedata_full.json"
with open(wine_json2) as wine_file_2:
    file_string_2 = wine_file_2.read()
    for i in file_string_2.replace("}]", "}").replace("[{", "{").split("}, {"):
        print(i)
        # print(i.find("}", -1))

