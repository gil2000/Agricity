#!/usr/bin/env bash

#apenas teste

PASSWORD="NNSXS.6ZOQRGSQDUE3GK4LO6OK2T2ZYMPZCVCS7PSRGRI.373EW3C54Z5QGNEL5LSD35VKS5NMDSXWDXI7S7I2F5U4E2D56PCQ"
USER="teste-agricity@ttn"
HOST="eu1.cloud.thethings.network"

# TOPIC="#"
TOPIC="v3/teste-agricity@ttn/devices/eui-a8610a3330187402/up"

mosquitto_sub -h $HOST -t $TOPIC -u $USER -P $PASSWORD -d
