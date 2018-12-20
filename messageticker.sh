# stop script on error
set -e

# Check to see if root CA file exists, download if not
if [ ! -f ./root-CA.crt ]; then
  printf "\nDownloading AWS IoT Root CA certificate from AWS...\n"
  curl https://www.amazontrust.com/repository/AmazonRootCA1.pem > root-CA.crt
fi

# run message ticker application to receive message from iot service and display on led matrix
python3 /home/pi/risrim/awsiot/messageticker_iot.py -e a3q6yyaptqkmga-ats.iot.us-east-1.amazonaws.com -r root-CA.crt -c newsTicker.cert.pem -k newsTicker.private.key -t newstickerTopic