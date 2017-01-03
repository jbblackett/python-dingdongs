import facebook

token = ""

graph = facebook.GraphAPI(access_token=token, version='2.7')

for i in range(690):
    img = open("C:\\Users\\admin\\Desktop\\frames\\" + "scene" + (str(i+38).zfill(5)) + ".jpg", "rb")
    graph.put_photo(img)
