# Handig om docker set-up te testen
docker stop pestileaks && docker rm -v pestileaks
docker build -t crop-r/pestileaks .
. create-container.sh
sleep 2
docker exec -ti -u pestileaks pestileaks sh -c  'sh ~/pestileaks/deploy.sh'
cat pestileaks.sql | docker exec -i -u pestileaks pestileaks psql
