import json
import cv2

def mapping(array,video):
    cap = cv2.VideoCapture(str('../upload/'+str(video)))
    frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    video_len_sec = frame / fps
    r=open('./jsons/info.json',"r")
    f = open('../pages/mapping.js', 'w') # 書き込みモードで開く
    copy_f=open('./output/mapping.js','w')
    dic=json.load(r)
    f.write("""function initMap() {
      var opts = {
        zoom: 150,
        center: new google.maps.LatLng("""+str(dic[str(20)]["lat"])+","+str(dic[str(20)]["lon"])+"""),
        mapTypeId: google.maps.MapTypeId.SATELLITE
      };
      var map = new google.maps.Map(document.getElementById("map"), opts);
      var flightPlanCoordinates = [
    """) # 引数の文字列をファイルに書き込む
    copy_f.write("""function initMap() {
      var opts = {
        zoom: 150,
        center: new google.maps.LatLng("""+str(dic[str(20)]["lat"])+","+str(dic[str(20)]["lon"])+"""),
        mapTypeId: google.maps.MapTypeId.SATELLITE
      };
      var map = new google.maps.Map(document.getElementById("map"), opts);
      var flightPlanCoordinates = [
    """) # 引数の文字列をファイルに書き込む

    for i in range(int(video_len_sec*10)):
        if dic[str(i)]["lat"]!=500 or dic[str(i)]["lon"]!=500:
            f.write("new google.maps.LatLng("+str(dic[str(i)]["lat"])+","+str(dic[str(i)]["lon"])+")")
            copy_f.write("new google.maps.LatLng("+str(dic[str(i)]["lat"])+","+str(dic[str(i)]["lon"])+")")
            if i!=video_len_sec*10-1:
                f.write(",")
                copy_f.write(",")

    f.write("];")
    copy_f.write("];")

    for i in array:
        f.write("var img_node"+str(i)+""" = document.createElement("img");
      img_node"""+str(i)+'.src = "../scripts/output/'+str(i)+""".jpg";
      img_node"""+str(i)+""".width = "300";

      var marker"""+str(i)+""" = new google.maps.Marker({
      position: new google.maps.LatLng("""+str(dic[str(i)]["lat"])+","+str(dic[str(i)]["lon"])+"""),
      map: map
      });
      var infowindow"""+str(i)+""" = new google.maps.InfoWindow({
      content:img_node"""+str(i)+"""
      });
      marker"""+str(i)+""".addListener( "click", function ( argument ) {
        console.log( argument ) ;
        infowindow"""+str(i)+""".open(map, marker"""+str(i)+""");
        } ) ;""")
        copy_f.write("var img_node"+str(i)+""" = document.createElement("img");
      img_node"""+str(i)+'.src = "'+str(i)+""".jpg";
      img_node"""+str(i)+""".width = "300";

      var marker"""+str(i)+""" = new google.maps.Marker({
      position: new google.maps.LatLng("""+str(dic[str(i)]["lat"])+","+str(dic[str(i)]["lon"])+"""),
      map: map
      });
      var infowindow"""+str(i)+""" = new google.maps.InfoWindow({
      content:img_node"""+str(i)+"""
      });
      marker"""+str(i)+""".addListener( "click", function ( argument ) {
        console.log( argument ) ;
        infowindow"""+str(i)+""".open(map, marker"""+str(i)+""");
        } ) ;""")

    f.write("""var flightPath = new google.maps.Polyline({
    path: flightPlanCoordinates,
    strokeColor: "#FF0000",
    strokeOpacity: 1.0,
    strokeWeight: 2
    });
    flightPath.setMap(map);
    //ウィンドウを開く
    }""")

    copy_f.write("""var flightPath = new google.maps.Polyline({
    path: flightPlanCoordinates,
    strokeColor: "#FF0000",
    strokeOpacity: 1.0,
    strokeWeight: 2
    });
    flightPath.setMap(map);
    //ウィンドウを開く
    }""")

    f.close() # ファイルを閉じる
    copy_f.close() # ファイルを閉じる
