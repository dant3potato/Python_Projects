import qrcode as qr
image = qr.make("https://www.meteomatics.com/en/weather-api/weather-api-key/")
image.save("whether")
