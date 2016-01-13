tree_test_set = [
  ({"bath":2,"beds":2,"elevation":0,"index":1,"price":2750000,"price_per_sqft":1939,"sqft":1418,"year_built":2006,"zip":"10003"},'New York'),
  ({"bath":1,"beds":0,"elevation":10,"index":4,"price":439000,"price_per_sqft":878,"sqft":500,"year_built":1930,"zip":"10003"},'New York'),
  ({"bath":1,"beds":1,"elevation":12,"index":8,"price":975000,"price_per_sqft":1083,"sqft":900,"year_built":1930,"zip":"10003"},'New York'),
  ({"bath":3,"beds":3,"elevation":4,"index":10,"price":2095000,"price_per_sqft":952,"sqft":2200,"year_built":1926,"zip":"10004"},'New York'),
  ({"bath":1,"beds":1,"elevation":5,"index":11,"price":999000,"price_per_sqft":1274,"sqft":784,"year_built":1982,"zip":"10004"},'New York'),
  ({"bath":1,"beds":0,"elevation":5,"index":14,"price":1110000,"price_per_sqft":1590,"sqft":698,"year_built":2008,"zip":"10005"},'New York'),
  ({"bath":1,"beds":1,"elevation":3,"index":17,"price":715000,"price_per_sqft":1284,"sqft":557,"year_built":1903,"zip":"10006"},'New York'),
  ({"bath":1.5,"beds":2,"elevation":5,"index":19,"price":2650000,"price_per_sqft":1060,"sqft":2500,"year_built":1915,"zip":"10007"},'New York'),
  ({"bath":2,"beds":2,"elevation":9,"index":20,"price":3450000,"price_per_sqft":1865,"sqft":1850,"year_built":1900,"zip":"10007"},'New York'),
  ({"bath":2,"beds":2,"elevation":4,"index":23,"price":1185000,"price_per_sqft":1185,"sqft":1000,"year_built":1900,"zip":"10009"},'New York'),
  ({"bath":1,"beds":0,"elevation":8,"index":29,"price":625000,"price_per_sqft":781,"sqft":800,"year_built":1964,"zip":"10010"},'New York'),
  ({"bath":2,"beds":2,"elevation":11,"index":35,"price":6525000,"price_per_sqft":3233,"sqft":2018,"year_built":2016,"zip":"10010"},'New York'),
  ({"bath":2,"beds":2,"elevation":12,"index":37,"price":1675000,"price_per_sqft":1367,"sqft":1225,"year_built":2006,"zip":"10010"},'New York'),
  ({"bath":1,"beds":2,"elevation":5,"index":38,"price":999000,"price_per_sqft":1250,"sqft":799,"year_built":1985,"zip":"10011"},'New York'),
  ({"bath":1,"beds":1,"elevation":6,"index":39,"price":1550000,"price_per_sqft":1550,"sqft":1000,"year_built":1926,"zip":"10011"},'New York'),
  ({"bath":1,"beds":1,"elevation":10,"index":43,"price":1595000,"price_per_sqft":2234,"sqft":714,"year_built":2015,"zip":"10011"},'New York'),
  ({"bath":2,"beds":2,"elevation":8,"index":45,"price":4995000,"price_per_sqft":2468,"sqft":2024,"year_built":1900,"zip":"10012"},'New York'),
  ({"bath":3,"beds":3,"elevation":3,"index":49,"price":5985000,"price_per_sqft":1814,"sqft":3300,"year_built":1909,"zip":"10013"},'New York'),
  ({"bath":3,"beds":3,"elevation":4,"index":50,"price":9900000,"price_per_sqft":3356,"sqft":2950,"year_built":2015,"zip":"10013"},'New York'),
  ({"bath":2,"beds":2,"elevation":5,"index":52,"price":3500000,"price_per_sqft":1750,"sqft":2000,"year_built":1915,"zip":"10013"},'New York'),
  ({"bath":1,"beds":2,"elevation":7,"index":55,"price":899000,"price_per_sqft":1096,"sqft":820,"year_built":1990,"zip":"10013"},'New York'),
  ({"bath":1,"beds":0,"elevation":6,"index":59,"price":390000,"price_per_sqft":709,"sqft":550,"year_built":1955,"zip":"10016"},'New York'),
  ({"bath":2,"beds":2,"elevation":10,"index":62,"price":1200000,"price_per_sqft":1000,"sqft":1200,"year_built":1964,"zip":"10016"},'New York'),
  ({"bath":1,"beds":0,"elevation":10,"index":63,"price":319000,"price_per_sqft":638,"sqft":500,"year_built":1941,"zip":"10016"},'New York'),
  ({"bath":1,"beds":0,"elevation":10,"index":64,"price":699999,"price_per_sqft":1400,"sqft":500,"year_built":1988,"zip":"10016"},'New York'),
  ({"bath":1,"beds":0,"elevation":10,"index":65,"price":775000,"price_per_sqft":1419,"sqft":546,"year_built":2009,"zip":"10016"},'New York'),
  ({"bath":1,"beds":1,"elevation":10,"index":66,"price":649000,"price_per_sqft":865,"sqft":750,"year_built":1965,"zip":"10016"},'New York'),
  ({"bath":1,"beds":1,"elevation":12,"index":69,"price":1590000,"price_per_sqft":2025,"sqft":785,"year_built":2008,"zip":"10016"},'New York'),
  ({"bath":1,"beds":1,"elevation":18,"index":70,"price":1150000,"price_per_sqft":1783,"sqft":645,"year_built":2014,"zip":"10016"},'New York'),
  ({"bath":1,"beds":0,"elevation":8,"index":73,"price":569000,"price_per_sqft":1048,"sqft":543,"year_built":1962,"zip":"10017"},'New York'),
  ({"bath":1,"beds":1,"elevation":10,"index":74,"price":549000,"price_per_sqft":732,"sqft":750,"year_built":1924,"zip":"10017"},'New York'),
  ({"bath":2,"beds":2,"elevation":22,"index":76,"price":879000,"price_per_sqft":1099,"sqft":800,"year_built":1928,"zip":"10017"},'New York'),
  ({"bath":3,"beds":2,"elevation":10,"index":77,"price":2999000,"price_per_sqft":937,"sqft":3200,"year_built":1925,"zip":"10018"},'New York'),
  ({"bath":3,"beds":2,"elevation":10,"index":78,"price":2999000,"price_per_sqft":937,"sqft":3200,"year_built":1925,"zip":"10018"},'New York'),
  ({"bath":3,"beds":2,"elevation":12,"index":79,"price":2999000,"price_per_sqft":937,"sqft":3200,"year_built":1925,"zip":"10018"},'New York'),
  ({"bath":1,"beds":1,"elevation":10,"index":81,"price":399000,"price_per_sqft":840,"sqft":475,"year_built":1910,"zip":"10019"},'New York'),
  ({"bath":1,"beds":1,"elevation":10,"index":82,"price":1135000,"price_per_sqft":1587,"sqft":715,"year_built":2005,"zip":"10019"},'New York'),
  ({"bath":1,"beds":1,"elevation":10,"index":83,"price":1145000,"price_per_sqft":1636,"sqft":700,"year_built":2005,"zip":"10019"},'New York'),
  ({"bath":2,"beds":2,"elevation":10,"index":85,"price":1725000,"price_per_sqft":1767,"sqft":976,"year_built":2005,"zip":"10019"},'New York'),
  ({"bath":2,"beds":2,"elevation":10,"index":86,"price":2750000,"price_per_sqft":1987,"sqft":1384,"year_built":2007,"zip":"10019"},'New York'),
  ({"bath":3,"beds":3,"elevation":18,"index":92,"price":1249000,"price_per_sqft":833,"sqft":1500,"year_built":1962,"zip":"10019"},'New York'),
  ({"bath":3,"beds":3,"elevation":18,"index":93,"price":1500000,"price_per_sqft":938,"sqft":1600,"year_built":1962,"zip":"10019"},'New York'),
  ({"bath":1,"beds":1,"elevation":19,"index":95,"price":1145000,"price_per_sqft":1636,"sqft":700,"year_built":2005,"zip":"10019"},'New York'),
  ({"bath":2,"beds":2,"elevation":19,"index":96,"price":1725000,"price_per_sqft":1767,"sqft":976,"year_built":2005,"zip":"10019"},'New York'),
  ({"bath":2,"beds":2,"elevation":20,"index":97,"price":3500000,"price_per_sqft":2258,"sqft":1550,"year_built":1925,"zip":"10019"},'New York'),
  ({"bath":1,"beds":0,"elevation":21,"index":98,"price":525000,"price_per_sqft":1000,"sqft":525,"year_built":1940,"zip":"10019"},'New York'),
  ({"bath":2,"beds":2,"elevation":21,"index":99,"price":2025000,"price_per_sqft":1413,"sqft":1433,"year_built":1940,"zip":"10019"},'New York'),
  ({"bath":1,"beds":0,"elevation":24,"index":101,"price":925000,"price_per_sqft":1581,"sqft":585,"year_built":1978,"zip":"10019"},'New York'),
  ({"bath":2,"beds":2,"elevation":25,"index":102,"price":1700000,"price_per_sqft":1688,"sqft":1007,"year_built":1982,"zip":"10019"},'New York'),
  ({"bath":2,"beds":2,"elevation":25,"index":103,"price":1700000,"price_per_sqft":1688,"sqft":1007,"year_built":1982,"zip":"10019"},'New York'),
  ({"bath":1,"beds":0,"elevation":10,"index":104,"price":449000,"price_per_sqft":816,"sqft":550,"year_built":1962,"zip":"10021"},'New York'),
  ({"bath":1,"beds":0,"elevation":12,"index":105,"price":299000,"price_per_sqft":748,"sqft":400,"year_built":1930,"zip":"10021"},'New York'),
  ({"bath":1,"beds":1,"elevation":16,"index":107,"price":695000,"price_per_sqft":965,"sqft":720,"year_built":1961,"zip":"10021"},'New York'),
  ({"bath":5,"beds":5,"elevation":21,"index":109,"price":27500000,"price_per_sqft":3667,"sqft":7500,"year_built":1930,"zip":"10021"},'New York'),
  ({"bath":1,"beds":0,"elevation":10,"index":110,"price":539000,"price_per_sqft":1111,"sqft":485,"year_built":1957,"zip":"10022"},'New York'),
  ({"bath":1,"beds":0,"elevation":10,"index":111,"price":779000,"price_per_sqft":1521,"sqft":512,"year_built":1975,"zip":"10022"},'New York'),
  ({"bath":1,"beds":1,"elevation":10,"index":112,"price":925000,"price_per_sqft":1242,"sqft":745,"year_built":1985,"zip":"10022"},'New York'),
  ({"bath":2,"beds":2,"elevation":10,"index":115,"price":4285000,"price_per_sqft":2453,"sqft":1747,"year_built":2016,"zip":"10022"},'New York'),
  ({"bath":4,"beds":4,"elevation":10,"index":119,"price":13400000,"price_per_sqft":4023,"sqft":3331,"year_built":2016,"zip":"10022"},'New York'),
  ({"bath":5,"beds":5,"elevation":10,"index":120,"price":19000000,"price_per_sqft":3821,"sqft":4972,"year_built":2016,"zip":"10022"},'New York'),
  ({"bath":10,"beds":10,"elevation":12,"index":123,"price":7995000,"price_per_sqft":1249,"sqft":6400,"year_built":1910,"zip":"10022"},'New York'),
  ({"bath":1,"beds":1,"elevation":14,"index":125,"price":588000,"price_per_sqft":980,"sqft":600,"year_built":1970,"zip":"10022"},'New York'),
  ({"bath":2,"beds":2,"elevation":15,"index":127,"price":4195000,"price_per_sqft":2397,"sqft":1750,"year_built":2016,"zip":"10022"},'New York'),
  ({"bath":2,"beds":2,"elevation":15,"index":128,"price":4195000,"price_per_sqft":2408,"sqft":1742,"year_built":2016,"zip":"10022"},'New York'),
  ({"bath":2,"beds":2,"elevation":15,"index":130,"price":4285000,"price_per_sqft":2453,"sqft":1747,"year_built":2016,"zip":"10022"},'New York'),
  ({"bath":3,"beds":3,"elevation":15,"index":133,"price":9350000,"price_per_sqft":3062,"sqft":3054,"year_built":2016,"zip":"10022"},'New York'),
  ({"bath":3,"beds":3,"elevation":15,"index":134,"price":10225000,"price_per_sqft":3400,"sqft":3007,"year_built":2016,"zip":"10022"},'New York'),
  ({"bath":4,"beds":4,"elevation":15,"index":135,"price":13150000,"price_per_sqft":3939,"sqft":3338,"year_built":2016,"zip":"10022"},'New York'),
  ({"bath":4,"beds":4,"elevation":15,"index":136,"price":13400000,"price_per_sqft":4023,"sqft":3331,"year_built":2016,"zip":"10022"},'New York'),
  ({"bath":1,"beds":1,"elevation":18,"index":140,"price":1000000,"price_per_sqft":1634,"sqft":612,"year_built":1912,"zip":"10023"},'New York'),
  ({"bath":2,"beds":2,"elevation":24,"index":145,"price":3600000,"price_per_sqft":2687,"sqft":1340,"year_built":1960,"zip":"10023"},'New York'),
  ({"bath":2,"beds":2,"elevation":24,"index":146,"price":3600000,"price_per_sqft":2687,"sqft":1340,"year_built":1960,"zip":"10023"},'New York'),
  ({"bath":1,"beds":1,"elevation":24,"index":147,"price":525000,"price_per_sqft":750,"sqft":700,"year_built":1924,"zip":"10023"},'New York'),
  ({"bath":1,"beds":1,"elevation":10,"index":155,"price":779000,"price_per_sqft":1113,"sqft":700,"year_built":1902,"zip":"10025"},'New York'),
  ({"bath":1,"beds":2,"elevation":10,"index":156,"price":1475000,"price_per_sqft":1519,"sqft":971,"year_built":1973,"zip":"10025"},'New York'),
  ({"bath":2,"beds":2,"elevation":10,"index":157,"price":1385000,"price_per_sqft":1440,"sqft":962,"year_built":1971,"zip":"10025"},'New York'),
  ({"bath":1,"beds":1,"elevation":13,"index":158,"price":779000,"price_per_sqft":1113,"sqft":700,"year_built":1902,"zip":"10025"},'New York'),
  ({"bath":1,"beds":0,"elevation":26,"index":160,"price":725000,"price_per_sqft":1208,"sqft":600,"year_built":1960,"zip":"10025"},'New York'),
  ({"bath":1,"beds":2,"elevation":27,"index":161,"price":925000,"price_per_sqft":1171,"sqft":790,"year_built":1941,"zip":"10025"},'New York'),
  ({"bath":1,"beds":1,"elevation":27,"index":162,"price":965000,"price_per_sqft":1226,"sqft":787,"year_built":1961,"zip":"10025"},'New York'),
  ({"bath":1,"beds":2,"elevation":30,"index":163,"price":1250000,"price_per_sqft":1092,"sqft":1145,"year_built":1922,"zip":"10025"},'New York'),
  ({"bath":1,"beds":2,"elevation":8,"index":165,"price":385000,"price_per_sqft":470,"sqft":820,"year_built":1999,"zip":"10026"},'New York'),
  ({"bath":2,"beds":2,"elevation":16,"index":166,"price":1695000,"price_per_sqft":1613,"sqft":1051,"year_built":2012,"zip":"10026"},'New York'),
  ({"bath":1,"beds":1,"elevation":8,"index":167,"price":600000,"price_per_sqft":566,"sqft":1060,"year_built":1899,"zip":"10027"},'New York'),
  ({"bath":1,"beds":2,"elevation":8,"index":168,"price":910000,"price_per_sqft":858,"sqft":1060,"year_built":1899,"zip":"10027"},'New York'),
  ({"bath":1,"beds":1,"elevation":10,"index":170,"price":600000,"price_per_sqft":566,"sqft":1060,"year_built":1899,"zip":"10027"},'New York'),
  ({"bath":1,"beds":2,"elevation":10,"index":171,"price":910000,"price_per_sqft":858,"sqft":1060,"year_built":1899,"zip":"10027"},'New York'),
  ({"bath":1,"beds":1,"elevation":22,"index":177,"price":735000,"price_per_sqft":919,"sqft":800,"year_built":1928,"zip":"10028"},'New York'),
  ({"bath":2,"beds":2,"elevation":29,"index":178,"price":4625000,"price_per_sqft":2729,"sqft":1695,"year_built":1987,"zip":"10028"},'New York'),
  ({"bath":1,"beds":1,"elevation":10,"index":179,"price":749000,"price_per_sqft":983,"sqft":762,"year_built":2011,"zip":"10031"},'New York'),
  ({"bath":1,"beds":1,"elevation":35,"index":181,"price":749000,"price_per_sqft":983,"sqft":762,"year_built":2011,"zip":"10031"},'New York'),
  ({"bath":1,"beds":2,"elevation":51,"index":184,"price":559900,"price_per_sqft":467,"sqft":1200,"year_built":1925,"zip":"10032"},'New York'),
  ({"bath":1,"beds":0,"elevation":8,"index":189,"price":820000,"price_per_sqft":1538,"sqft":533,"year_built":2013,"zip":"10036"},'New York'),
  ({"bath":1,"beds":1,"elevation":10,"index":193,"price":1550000,"price_per_sqft":1952,"sqft":794,"year_built":2004,"zip":"10036"},'New York'),
  ({"bath":1,"beds":1,"elevation":14,"index":196,"price":1780000,"price_per_sqft":1802,"sqft":988,"year_built":2007,"zip":"10036"},'New York'),
  ({"bath":2,"beds":2,"elevation":14,"index":197,"price":2800000,"price_per_sqft":2141,"sqft":1308,"year_built":2007,"zip":"10036"},'New York'),
  ({"bath":1,"beds":1,"elevation":6,"index":198,"price":411500,"price_per_sqft":702,"sqft":586,"year_built":1921,"zip":"10039"},'New York'),
  ({"bath":2,"beds":2,"elevation":10,"index":200,"price":1995000,"price_per_sqft":1911,"sqft":1044,"year_built":1996,"zip":"10065"},'New York'),
  ({"bath":2,"beds":2,"elevation":14,"index":201,"price":2235000,"price_per_sqft":1444,"sqft":1548,"year_built":1999,"zip":"10065"},'New York'),
  ({"bath":4,"beds":4,"elevation":15,"index":202,"price":8800000,"price_per_sqft":2602,"sqft":3382,"year_built":1941,"zip":"10065"},'New York'),
  ({"bath":2,"beds":2,"elevation":17,"index":203,"price":1850000,"price_per_sqft":1772,"sqft":1044,"year_built":1996,"zip":"10065"},'New York'),
  ({"bath":1,"beds":1,"elevation":17,"index":205,"price":1695000,"price_per_sqft":2493,"sqft":680,"year_built":1927,"zip":"10065"},'New York'),
  ({"bath":1,"beds":1,"elevation":19,"index":206,"price":1495000,"price_per_sqft":1329,"sqft":1125,"year_built":1962,"zip":"10065"},'New York'),
  ({"bath":2,"beds":2,"elevation":2,"index":207,"price":2200000,"price_per_sqft":2107,"sqft":1044,"year_built":2000,"zip":"10069"},'New York'),
  ({"bath":2,"beds":3,"elevation":10,"index":210,"price":1950000,"price_per_sqft":1219,"sqft":1600,"year_built":1956,"zip":"10075"},'New York'),
  ({"bath":2,"beds":2,"elevation":18,"index":212,"price":1735000,"price_per_sqft":1095,"sqft":1585,"year_built":1980,"zip":"10075"},'New York'),
  ({"bath":3,"beds":3,"elevation":10,"index":214,"price":1850000,"price_per_sqft":1367,"sqft":1353,"year_built":2005,"zip":"10128"},'New York'),
  ({"bath":2,"beds":2,"elevation":14,"index":215,"price":1995000,"price_per_sqft":1419,"sqft":1406,"year_built":1986,"zip":"10128"},'New York'),
  ({"bath":2,"beds":2,"elevation":24,"index":217,"price":2499000,"price_per_sqft":1507,"sqft":1658,"year_built":2004,"zip":"10128"},'New York'),
  ({"bath":2,"beds":2,"elevation":33,"index":218,"price":1575000,"price_per_sqft":1190,"sqft":1324,"year_built":1930,"zip":"10128"},'New York'),
  ({"bath":3,"beds":3,"elevation":0,"index":219,"price":1495000,"price_per_sqft":1099,"sqft":1360,"year_built":1990,"zip":"10280"},'New York'),
  ({"bath":1,"beds":1,"elevation":0,"index":220,"price":529000,"price_per_sqft":814,"sqft":650,"year_built":1986,"zip":"10280"},'New York'),
  ({"bath":3,"beds":3,"elevation":1,"index":221,"price":2695000,"price_per_sqft":1354,"sqft":1991,"year_built":2006,"zip":"10280"},'New York'),
  ({"bath":1,"beds":1,"elevation":24,"index":224,"price":550000,"price_per_sqft":760,"sqft":724,"year_built":1982,"zip":"94102"},'San Francisco'),
  ({"bath":1,"beds":1,"elevation":5,"index":229,"price":598000,"price_per_sqft":1120,"sqft":534,"year_built":2005,"zip":"94103"},'San Francisco'),
  ({"bath":1,"beds":1,"elevation":10,"index":232,"price":798000,"price_per_sqft":1038,"sqft":769,"year_built":1926,"zip":"94103"},'San Francisco'),
  ({"bath":2,"beds":2,"elevation":12,"index":236,"price":334905,"price_per_sqft":320,"sqft":1047,"year_built":2000,"zip":"94103"},'San Francisco'),
  ({"bath":1.5,"beds":1,"elevation":13,"index":238,"price":1365000,"price_per_sqft":849,"sqft":1607,"year_built":1996,"zip":"94103"},'San Francisco'),
  ({"bath":1,"beds":1,"elevation":163,"index":241,"price":649000,"price_per_sqft":764,"sqft":850,"year_built":1983,"zip":"94103"},'San Francisco'),
  ({"bath":2,"beds":2,"elevation":0,"index":243,"price":1980000,"price_per_sqft":1348,"sqft":1469,"year_built":2009,"zip":"94105"},'San Francisco'),
  ({"bath":2,"beds":2,"elevation":0,"index":244,"price":3600000,"price_per_sqft":2179,"sqft":1652,"year_built":2009,"zip":"94105"},'San Francisco'),
  ({"bath":3,"beds":2,"elevation":0,"index":245,"price":4995000,"price_per_sqft":2240,"sqft":2230,"year_built":2009,"zip":"94105"},'San Francisco'),
  ({"bath":2,"beds":2,"elevation":0,"index":247,"price":2149000,"price_per_sqft":1632,"sqft":1317,"year_built":2008,"zip":"94105"},'San Francisco'),
  ({"bath":1,"beds":1,"elevation":12,"index":251,"price":187518,"price_per_sqft":280,"sqft":670,"year_built":2000,"zip":"94105"},'San Francisco'),
  ({"bath":2,"beds":2,"elevation":35,"index":254,"price":2799000,"price_per_sqft":2108,"sqft":1328,"year_built":2008,"zip":"94105"},'San Francisco'),
  ({"bath":2.5,"beds":2,"elevation":2,"index":255,"price":1050000,"price_per_sqft":640,"sqft":1640,"year_built":2000,"zip":"94107"},'San Francisco'),
  ({"bath":1,"beds":1,"elevation":3,"index":257,"price":998000,"price_per_sqft":1144,"sqft":872,"year_built":2006,"zip":"94107"},'San Francisco'),
  ({"bath":2,"beds":2,"elevation":4,"index":258,"price":1659000,"price_per_sqft":1424,"sqft":1165,"year_built":2000,"zip":"94107"},'San Francisco'),
  ({"bath":1,"beds":1,"elevation":4,"index":259,"price":788000,"price_per_sqft":873,"sqft":903,"year_built":2004,"zip":"94107"},'San Francisco'),
  ({"bath":2,"beds":2,"elevation":4,"index":260,"price":1395000,"price_per_sqft":1046,"sqft":1334,"year_built":2001,"zip":"94107"},'San Francisco'),
  ({"bath":2,"beds":3,"elevation":13,"index":266,"price":1275000,"price_per_sqft":849,"sqft":1502,"year_built":2001,"zip":"94107"},'San Francisco'),
  ({"bath":1.5,"beds":1,"elevation":14,"index":267,"price":775000,"price_per_sqft":928,"sqft":835,"year_built":2009,"zip":"94107"},'San Francisco'),
  ({"bath":1,"beds":1,"elevation":59,"index":270,"price":699000,"price_per_sqft":750,"sqft":932,"year_built":1907,"zip":"94107"},'San Francisco'),
  ({"bath":1,"beds":1,"elevation":11,"index":271,"price":985000,"price_per_sqft":1114,"sqft":884,"year_built":1978,"zip":"94108"},'San Francisco'),
  ({"bath":1,"beds":1,"elevation":60,"index":272,"price":725000,"price_per_sqft":682,"sqft":1063,"year_built":1978,"zip":"94108"},'San Francisco'),
  ({"bath":2,"beds":2,"elevation":66,"index":273,"price":849000,"price_per_sqft":772,"sqft":1100,"year_built":1911,"zip":"94108"},'San Francisco'),
  ({"bath":1,"beds":1,"elevation":72,"index":274,"price":618000,"price_per_sqft":877,"sqft":705,"year_built":1973,"zip":"94108"},'San Francisco'),
  ({"bath":2,"beds":2,"elevation":83,"index":275,"price":5950000,"price_per_sqft":1608,"sqft":3700,"year_built":1989,"zip":"94108"},'San Francisco'),
  ({"bath":4,"beds":4,"elevation":10,"index":276,"price":1800000,"price_per_sqft":727,"sqft":2475,"year_built":1948,"zip":"94109"},'San Francisco'),
  ({"bath":2.5,"beds":2,"elevation":19,"index":277,"price":2350000,"price_per_sqft":1788,"sqft":1314,"year_built":2008,"zip":"94109"},'San Francisco'),
  ({"bath":1,"beds":1,"elevation":51,"index":279,"price":699000,"price_per_sqft":896,"sqft":780,"year_built":1982,"zip":"94109"},'San Francisco'),
  ({"bath":1,"beds":1,"elevation":73,"index":285,"price":699000,"price_per_sqft":794,"sqft":880,"year_built":1984,"zip":"94109"},'San Francisco'),
  ({"bath":2,"beds":2,"elevation":20,"index":294,"price":1199000,"price_per_sqft":1271,"sqft":943,"year_built":2014,"zip":"94110"},'San Francisco'),
  ({"bath":2,"beds":2,"elevation":30,"index":295,"price":1095000,"price_per_sqft":965,"sqft":1135,"year_built":2010,"zip":"94110"},'San Francisco'),
  ({"bath":2,"beds":1,"elevation":31,"index":296,"price":795000,"price_per_sqft":1291,"sqft":616,"year_built":2014,"zip":"94110"},'San Francisco'),
  ({"bath":2,"beds":3,"elevation":33,"index":297,"price":979000,"price_per_sqft":680,"sqft":1440,"year_built":1900,"zip":"94110"},'San Francisco'),
  ({"bath":2,"beds":4,"elevation":69,"index":301,"price":1099000,"price_per_sqft":867,"sqft":1267,"year_built":1962,"zip":"94110"},'San Francisco'),
  ({"bath":2,"beds":3,"elevation":84,"index":304,"price":998000,"price_per_sqft":682,"sqft":1464,"year_built":1907,"zip":"94110"},'San Francisco'),
  ({"bath":2.5,"beds":3,"elevation":4,"index":305,"price":1300000,"price_per_sqft":792,"sqft":1642,"year_built":1975,"zip":"94111"},'San Francisco'),
  ({"bath":1,"beds":1,"elevation":5,"index":306,"price":539000,"price_per_sqft":760,"sqft":709,"year_built":2000,"zip":"94111"},'San Francisco'),
  ({"bath":1,"beds":1,"elevation":12,"index":307,"price":735000,"price_per_sqft":944,"sqft":779,"year_built":1983,"zip":"94111"},'San Francisco'),
  ({"bath":1,"beds":2,"elevation":44,"index":309,"price":859000,"price_per_sqft":781,"sqft":1100,"year_built":1890,"zip":"94112"},'San Francisco'),
  ({"bath":1,"beds":2,"elevation":48,"index":311,"price":750000,"price_per_sqft":765,"sqft":980,"year_built":1924,"zip":"94112"},'San Francisco'),
  ({"bath":2,"beds":3,"elevation":51,"index":312,"price":549000,"price_per_sqft":278,"sqft":1972,"year_built":1915,"zip":"94112"},'San Francisco'),
  ({"bath":3,"beds":4,"elevation":54,"index":315,"price":900000,"price_per_sqft":481,"sqft":1870,"year_built":2003,"zip":"94112"},'San Francisco'),
  ({"bath":2,"beds":3,"elevation":54,"index":316,"price":748000,"price_per_sqft":491,"sqft":1522,"year_built":1930,"zip":"94112"},'San Francisco'),
  ({"bath":1,"beds":2,"elevation":74,"index":321,"price":798888,"price_per_sqft":779,"sqft":1025,"year_built":1929,"zip":"94112"},'San Francisco'),
  ({"bath":2,"beds":5,"elevation":81,"index":322,"price":899000,"price_per_sqft":463,"sqft":1940,"year_built":1972,"zip":"94112"},'San Francisco'),
  ({"bath":1.5,"beds":3,"elevation":94,"index":323,"price":699000,"price_per_sqft":430,"sqft":1625,"year_built":1910,"zip":"94112"},'San Francisco'),
  ({"bath":2,"beds":3,"elevation":95,"index":324,"price":749000,"price_per_sqft":495,"sqft":1513,"year_built":1907,"zip":"94112"},'San Francisco'),
  ({"bath":1,"beds":2,"elevation":136,"index":328,"price":500000,"price_per_sqft":429,"sqft":1166,"year_built":1958,"zip":"94112"},'San Francisco'),
  ({"bath":2.5,"beds":4,"elevation":140,"index":331,"price":699900,"price_per_sqft":399,"sqft":1752,"year_built":1982,"zip":"94112"},'San Francisco'),
  ({"bath":1,"beds":2,"elevation":143,"index":332,"price":688000,"price_per_sqft":601,"sqft":1145,"year_built":1950,"zip":"94112"},'San Francisco'),
  ({"bath":2,"beds":3,"elevation":33,"index":334,"price":1195000,"price_per_sqft":856,"sqft":1396,"year_built":1907,"zip":"94114"},'San Francisco'),
  ({"bath":1,"beds":1,"elevation":50,"index":335,"price":697000,"price_per_sqft":1004,"sqft":694,"year_built":1922,"zip":"94114"},'San Francisco'),
  ({"bath":1,"beds":1,"elevation":74,"index":340,"price":825000,"price_per_sqft":1375,"sqft":600,"year_built":1955,"zip":"94114"},'San Francisco'),
  ({"bath":1,"beds":2,"elevation":89,"index":341,"price":699000,"price_per_sqft":764,"sqft":915,"year_built":1907,"zip":"94114"},'San Francisco'),
  ({"bath":2,"beds":3,"elevation":105,"index":342,"price":1495000,"price_per_sqft":984,"sqft":1520,"year_built":1927,"zip":"94114"},'San Francisco'),
  ({"bath":4.5,"beds":4,"elevation":238,"index":343,"price":5200000,"price_per_sqft":1080,"sqft":4813,"year_built":1952,"zip":"94114"},'San Francisco'),
  ({"bath":1,"beds":1,"elevation":91,"index":350,"price":1199000,"price_per_sqft":1053,"sqft":1139,"year_built":1906,"zip":"94115"},'San Francisco'),
  ({"bath":2,"beds":3,"elevation":36,"index":352,"price":795000,"price_per_sqft":589,"sqft":1350,"year_built":1954,"zip":"94116"},'San Francisco'),
  ({"bath":3.5,"beds":6,"elevation":97,"index":359,"price":949000,"price_per_sqft":384,"sqft":2473,"year_built":1918,"zip":"94116"},'San Francisco'),
  ({"bath":1,"beds":3,"elevation":65,"index":364,"price":1295000,"price_per_sqft":731,"sqft":1772,"year_built":1890,"zip":"94117"},'San Francisco'),
  ({"bath":6,"beds":6,"elevation":67,"index":365,"price":6895000,"price_per_sqft":884,"sqft":7800,"year_built":1902,"zip":"94117"},'San Francisco'),
  ({"bath":2,"beds":2,"elevation":86,"index":366,"price":1725000,"price_per_sqft":1219,"sqft":1415,"year_built":1922,"zip":"94117"},'San Francisco'),
  ({"bath":3,"beds":3,"elevation":88,"index":367,"price":1995000,"price_per_sqft":1042,"sqft":1915,"year_built":1922,"zip":"94117"},'San Francisco'),
  ({"bath":1,"beds":0,"elevation":91,"index":368,"price":499000,"price_per_sqft":978,"sqft":510,"year_built":1900,"zip":"94117"},'San Francisco'),
  ({"bath":1,"beds":0,"elevation":91,"index":369,"price":499000,"price_per_sqft":978,"sqft":510,"year_built":1900,"zip":"94117"},'San Francisco'),
  ({"bath":2,"beds":3,"elevation":121,"index":372,"price":1200000,"price_per_sqft":935,"sqft":1284,"year_built":1929,"zip":"94117"},'San Francisco'),
  ({"bath":3,"beds":3,"elevation":58,"index":374,"price":1785000,"price_per_sqft":906,"sqft":1970,"year_built":1925,"zip":"94118"},'San Francisco'),
  ({"bath":2,"beds":3,"elevation":75,"index":379,"price":995000,"price_per_sqft":714,"sqft":1393,"year_built":2000,"zip":"94118"},'San Francisco'),
  ({"bath":3.5,"beds":5,"elevation":89,"index":380,"price":6495000,"price_per_sqft":1409,"sqft":4609,"year_built":1906,"zip":"94118"},'San Francisco'),
  ({"bath":2,"beds":5,"elevation":26,"index":382,"price":6298000,"price_per_sqft":1757,"sqft":3585,"year_built":1914,"zip":"94121"},'San Francisco'),
  ({"bath":3,"beds":3,"elevation":44,"index":383,"price":1139000,"price_per_sqft":743,"sqft":1532,"year_built":2008,"zip":"94121"},'San Francisco'),
  ({"bath":1,"beds":4,"elevation":55,"index":385,"price":1050000,"price_per_sqft":594,"sqft":1767,"year_built":1932,"zip":"94121"},'San Francisco'),
  ({"bath":4,"beds":4,"elevation":81,"index":387,"price":1595000,"price_per_sqft":580,"sqft":2750,"year_built":1925,"zip":"94121"},'San Francisco'),
  ({"bath":1,"beds":2,"elevation":71,"index":391,"price":829000,"price_per_sqft":724,"sqft":1145,"year_built":1925,"zip":"94122"},'San Francisco'),
  ({"bath":1,"beds":2,"elevation":110,"index":394,"price":749000,"price_per_sqft":517,"sqft":1450,"year_built":1936,"zip":"94122"},'San Francisco'),
  ({"bath":1,"beds":2,"elevation":110,"index":395,"price":749000,"price_per_sqft":517,"sqft":1450,"year_built":1936,"zip":"94122"},'San Francisco'),
  ({"bath":3,"beds":4,"elevation":9,"index":397,"price":3595000,"price_per_sqft":1192,"sqft":3017,"year_built":1931,"zip":"94123"},'San Francisco'),
  ({"bath":1.5,"beds":2,"elevation":14,"index":398,"price":1425000,"price_per_sqft":1048,"sqft":1360,"year_built":1925,"zip":"94123"},'San Francisco'),
  ({"bath":1,"beds":1,"elevation":17,"index":399,"price":865000,"price_per_sqft":901,"sqft":960,"year_built":1993,"zip":"94123"},'San Francisco'),
  ({"bath":2,"beds":3,"elevation":5,"index":403,"price":358000,"price_per_sqft":270,"sqft":1325,"year_built":1989,"zip":"94124"},'San Francisco'),
  ({"bath":4,"beds":4,"elevation":8,"index":406,"price":850000,"price_per_sqft":344,"sqft":2470,"year_built":1928,"zip":"94124"},'San Francisco'),
  ({"bath":1,"beds":2,"elevation":11,"index":407,"price":648000,"price_per_sqft":576,"sqft":1125,"year_built":1921,"zip":"94124"},'San Francisco'),
  ({"bath":2,"beds":4,"elevation":21,"index":410,"price":689000,"price_per_sqft":468,"sqft":1473,"year_built":1951,"zip":"94124"},'San Francisco'),
  ({"bath":2,"beds":2,"elevation":23,"index":411,"price":669000,"price_per_sqft":508,"sqft":1317,"year_built":1986,"zip":"94124"},'San Francisco'),
  ({"bath":1.5,"beds":2,"elevation":27,"index":412,"price":729000,"price_per_sqft":720,"sqft":1012,"year_built":1942,"zip":"94124"},'San Francisco'),
  ({"bath":1,"beds":2,"elevation":36,"index":415,"price":995000,"price_per_sqft":1658,"sqft":600,"year_built":1908,"zip":"94124"},'San Francisco'),
  ({"bath":1,"beds":2,"elevation":43,"index":416,"price":759900,"price_per_sqft":647,"sqft":1175,"year_built":1941,"zip":"94124"},'San Francisco'),
  ({"bath":3.5,"beds":6,"elevation":55,"index":417,"price":995000,"price_per_sqft":323,"sqft":3080,"year_built":2001,"zip":"94124"},'San Francisco'),
  ({"bath":1,"beds":2,"elevation":60,"index":418,"price":725000,"price_per_sqft":697,"sqft":1040,"year_built":1945,"zip":"94124"},'San Francisco'),
  ({"bath":3,"beds":4,"elevation":98,"index":419,"price":3420000,"price_per_sqft":669,"sqft":5113,"year_built":1926,"zip":"94127"},'San Francisco'),
  ({"bath":2,"beds":3,"elevation":106,"index":420,"price":1650000,"price_per_sqft":815,"sqft":2025,"year_built":1922,"zip":"94127"},'San Francisco'),
  ({"bath":2,"beds":3,"elevation":179,"index":424,"price":1049000,"price_per_sqft":645,"sqft":1626,"year_built":1947,"zip":"94127"},'San Francisco'),
  ({"bath":2,"beds":2,"elevation":181,"index":425,"price":599000,"price_per_sqft":695,"sqft":862,"year_built":1990,"zip":"94127"},'San Francisco'),
  ({"bath":3.5,"beds":5,"elevation":181,"index":426,"price":2995000,"price_per_sqft":770,"sqft":3890,"year_built":1947,"zip":"94127"},'San Francisco'),
  ({"bath":1,"beds":1,"elevation":43,"index":428,"price":350000,"price_per_sqft":583,"sqft":600,"year_built":1908,"zip":"94131"},'San Francisco'),
  ({"bath":1,"beds":2,"elevation":43,"index":429,"price":550000,"price_per_sqft":688,"sqft":800,"year_built":1908,"zip":"94131"},'San Francisco'),
  ({"bath":4,"beds":4,"elevation":49,"index":430,"price":3760000,"price_per_sqft":1219,"sqft":3085,"year_built":1900,"zip":"94131"},'San Francisco'),
  ({"bath":2,"beds":3,"elevation":52,"index":431,"price":1050000,"price_per_sqft":829,"sqft":1266,"year_built":1922,"zip":"94131"},'San Francisco'),
  ({"bath":1,"beds":2,"elevation":92,"index":436,"price":600000,"price_per_sqft":444,"sqft":1350,"year_built":1908,"zip":"94131"},'San Francisco'),
  ({"bath":2,"beds":3,"elevation":103,"index":438,"price":1595000,"price_per_sqft":1053,"sqft":1515,"year_built":1961,"zip":"94131"},'San Francisco'),
  ({"bath":2,"beds":3,"elevation":106,"index":439,"price":849000,"price_per_sqft":523,"sqft":1622,"year_built":1947,"zip":"94131"},'San Francisco'),
  ({"bath":3.5,"beds":4,"elevation":108,"index":440,"price":1995000,"price_per_sqft":602,"sqft":3312,"year_built":1992,"zip":"94131"},'San Francisco'),
  ({"bath":3.5,"beds":3,"elevation":125,"index":442,"price":2195000,"price_per_sqft":1012,"sqft":2168,"year_built":1922,"zip":"94131"},'San Francisco'),
  ({"bath":2,"beds":3,"elevation":143,"index":445,"price":1159000,"price_per_sqft":670,"sqft":1731,"year_built":1977,"zip":"94131"},'San Francisco'),
  ({"bath":3.5,"beds":5,"elevation":174,"index":448,"price":2250000,"price_per_sqft":603,"sqft":3729,"year_built":1962,"zip":"94131"},'San Francisco'),
  ({"bath":2.5,"beds":3,"elevation":187,"index":450,"price":1095000,"price_per_sqft":586,"sqft":1868,"year_built":1968,"zip":"94131"},'San Francisco'),
  ({"bath":1,"beds":2,"elevation":189,"index":451,"price":599000,"price_per_sqft":605,"sqft":990,"year_built":1972,"zip":"94131"},'San Francisco'),
  ({"bath":1,"beds":2,"elevation":24,"index":453,"price":915000,"price_per_sqft":731,"sqft":1251,"year_built":1954,"zip":"94132"},'San Francisco'),
  ({"bath":2.5,"beds":3,"elevation":43,"index":455,"price":1588000,"price_per_sqft":794,"sqft":2001,"year_built":2015,"zip":"94132"},'San Francisco'),
  ({"bath":1,"beds":2,"elevation":63,"index":456,"price":795000,"price_per_sqft":633,"sqft":1256,"year_built":1941,"zip":"94132"},'San Francisco'),
  ({"bath":2,"beds":4,"elevation":69,"index":458,"price":848000,"price_per_sqft":515,"sqft":1646,"year_built":1949,"zip":"94132"},'San Francisco'),
  ({"bath":2,"beds":3,"elevation":118,"index":460,"price":849900,"price_per_sqft":649,"sqft":1310,"year_built":1958,"zip":"94132"},'San Francisco'),
  ({"bath":2.5,"beds":3,"elevation":136,"index":462,"price":1539514,"price_per_sqft":761,"sqft":2024,"year_built":2014,"zip":"94132"},'San Francisco'),
  ({"bath":2.5,"beds":3,"elevation":143,"index":463,"price":1339000,"price_per_sqft":628,"sqft":2133,"year_built":2015,"zip":"94132"},'San Francisco'),
  ({"bath":2.5,"beds":3,"elevation":153,"index":465,"price":1611000,"price_per_sqft":805,"sqft":2001,"year_built":2015,"zip":"94132"},'San Francisco'),
  ({"bath":1,"beds":1,"elevation":36,"index":467,"price":699000,"price_per_sqft":932,"sqft":750,"year_built":1908,"zip":"94133"},'San Francisco'),
  ({"bath":1,"beds":1,"elevation":84,"index":472,"price":599000,"price_per_sqft":949,"sqft":631,"year_built":1945,"zip":"94134"},'San Francisco'),
  ({"bath":2,"beds":2,"elevation":1,"index":475,"price":1698000,"price_per_sqft":1048,"sqft":1620,"year_built":2008,"zip":"94158"},'San Francisco'),
  ({"bath":1,"beds":1,"elevation":2,"index":476,"price":849000,"price_per_sqft":958,"sqft":886,"year_built":2012,"zip":"94158"},'San Francisco'),
  ({"bath":2,"beds":2,"elevation":2,"index":477,"price":1675000,"price_per_sqft":1072,"sqft":1562,"year_built":2012,"zip":"94158"},'San Francisco'),
  ({"bath":2,"beds":2,"elevation":2,"index":478,"price":1695000,"price_per_sqft":1053,"sqft":1610,"year_built":2007,"zip":"94158"},'San Francisco'),
  ({"bath":2,"beds":3,"elevation":13,"index":479,"price":2219000,"price_per_sqft":1155,"sqft":1921,"year_built":2012,"zip":"94158"},'San Francisco'),
  ({"bath":2,"beds":2,"elevation":4,"index":481,"price":1950000,"price_per_sqft":1010,"sqft":1930,"year_built":1995,"zip":"San Francisco, CA"},'San Francisco'),
  ({"bath":1,"beds":0,"elevation":5,"index":482,"price":539000,"price_per_sqft":760,"sqft":709,"year_built":2000,"zip":"San Francisco, CA"},'San Francisco'),
  ({"bath":2,"beds":2,"elevation":24,"index":483,"price":849000,"price_per_sqft":824,"sqft":1030,"year_built":1982,"zip":"San Francisco, CA"},'San Francisco'),
  ({"bath":2.5,"beds":2,"elevation":48,"index":484,"price":2495000,"price_per_sqft":1379,"sqft":1809,"year_built":1940,"zip":"San Francisco, CA"},'San Francisco'),
  ({"bath":4,"beds":4,"elevation":49,"index":485,"price":3760000,"price_per_sqft":1219,"sqft":3085,"year_built":1894,"zip":"San Francisco, CA"},'San Francisco'),
  ({"bath":2,"beds":3,"elevation":66,"index":486,"price":1799000,"price_per_sqft":999,"sqft":1800,"year_built":1926,"zip":"San Francisco, CA"},'San Francisco'),
  ({"bath":2.5,"beds":5,"elevation":76,"index":487,"price":1800000,"price_per_sqft":586,"sqft":3073,"year_built":1890,"zip":"San Francisco, CA"},'San Francisco')
]