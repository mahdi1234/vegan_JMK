# diet:vegan=yes IN 'Jihomoravský kraj'
curl 'https://overpass-api.de/api/interpreter?data=%5Bout%3Ajson%5D%5Btimeout%3A100%5D%3Barea(3600442311)-%3E.searchArea%3B(node%5B%22diet%3Avegan%22%3D%22yes%22%5D(area.searchArea)%3Bway%5B%22diet%3Avegan%22%3D%22yes%22%5D(area.searchArea)%3Brelation%5B%22diet%3Avegan%22%3D%22yes%22%5D(area.searchArea)%3B)%3Bout%20body%3B%3E%3Bout%20skel%20qt%3B' | grep -v timestamp_ > vegan_yes.json
sleep 300
# diet:vegan=only IN 'Jihomoravský kraj'
curl 'https://overpass-api.de/api/interpreter?data=%5Bout%3Ajson%5D%5Btimeout%3A100%5D%3Barea(3600442311)-%3E.searchArea%3B(node%5B%22diet%3Avegan%22%3D%22only%22%5D(area.searchArea)%3Bway%5B%22diet%3Avegan%22%3D%22only%22%5D(area.searchArea)%3Brelation%5B%22diet%3Avegan%22%3D%22only%22%5D(area.searchArea)%3B)%3Bout%20body%3B%3E%3Bout%20skel%20qt%3B' | grep -v timestamp_ > vegan_only.json
sleep 300
# diet:vegan=limited IN 'Jihomoravský kraj'
curl 'https://overpass-api.de/api/interpreter?data=%5Bout%3Ajson%5D%5Btimeout%3A100%5D%3Barea(3600442311)-%3E.searchArea%3B(node%5B%22diet%3Avegan%22%3D%22limited%22%5D(area.searchArea)%3Bway%5B%22diet%3Avegan%22%3D%22limited%22%5D(area.searchArea)%3Brelation%5B%22diet%3Avegan%22%3D%22limited%22%5D(area.searchArea)%3B)%3Bout%20body%3B%3E%3Bout%20skel%20qt%3B' | grep -v timestamp_ > vegan_limited.json
sleep 300
# diet:vegetarian=yes IN 'Jihomoravský kraj'
curl 'https://overpass-api.de/api/interpreter?data=%5Bout%3Ajson%5D%5Btimeout%3A100%5D%3Barea(3600442311)-%3E.searchArea%3B(node%5B%22diet%3Avegetarian%22%3D%22yes%22%5D(area.searchArea)%3Bway%5B%22diet%3Avegetarian%22%3D%22yes%22%5D(area.searchArea)%3Brelation%5B%22diet%3Avegetarian%22%3D%22yes%22%5D(area.searchArea)%3B)%3Bout%20body%3B%3E%3Bout%20skel%20qt%3B' | grep -v timestamp_ > vegetarian_yes.json
sleep 300
# diet:vegetarian=only IN 'Jihomoravský kraj'
curl 'https://overpass-api.de/api/interpreter?data=%5Bout%3Ajson%5D%5Btimeout%3A100%5D%3Barea(3600442311)-%3E.searchArea%3B(node%5B%22diet%3Avegetarian%22%3D%22only%22%5D(area.searchArea)%3Bway%5B%22diet%3Avegetarian%22%3D%22only%22%5D(area.searchArea)%3Brelation%5B%22diet%3Avegetarian%22%3D%22only%22%5D(area.searchArea)%3B)%3Bout%20body%3B%3E%3Bout%20skel%20qt%3B' | grep -v timestamp_ > vegetarian_only.json
