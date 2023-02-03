docker build -t texts_api .
docker kill texts_api
docker run -d --rm -v C:\Users\Administrator\Desktop\texts_api:/myapp --env-file .env --name texts_api -p 8183:8183 texts_api