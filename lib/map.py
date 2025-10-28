from staticmap import StaticMap, CircleMarker

class Map:
    def run(self,lon,lat):
        # Buat peta ukuran 400x400 piksel
        m = StaticMap(400, 400)

        # Tambahkan marker merah
        marker = CircleMarker((lon, lat), 'red', 6)
        m.add_marker(marker)

        # Render peta ke gambar
        image = m.render()

        # Simpan ke file
        image.save('picture/map_osm.png')
