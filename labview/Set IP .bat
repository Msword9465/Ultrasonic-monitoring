set addr=10.0.0.100
set mask=255.255.255.0
set gateway=202.38.205.254
set dns=202.38.193.33
netsh interface ip set address name="ÒÔÌ«Íø" source=static addr=%addr% mask=%mask% gateway=%gateway%
netsh interface ip set dns "ÒÔÌ«Íø" source=static addr=%dns%