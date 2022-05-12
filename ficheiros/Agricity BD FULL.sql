-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: agricity
-- ------------------------------------------------------
-- Server version	5.7.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `barometricpressure`
--

DROP TABLE IF EXISTS `barometricpressure`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `barometricpressure` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` timestamp NOT NULL,
  `BarometricPressure` float unsigned NOT NULL,
  `idEstacao` varchar(50) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `idEstacaoBarPressure` (`idEstacao`) USING BTREE,
  CONSTRAINT `idEstacaoBarPressure` FOREIGN KEY (`idEstacao`) REFERENCES `estacao` (`idEstacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `barometricpressure`
--

LOCK TABLES `barometricpressure` WRITE;
/*!40000 ALTER TABLE `barometricpressure` DISABLE KEYS */;
/*!40000 ALTER TABLE `barometricpressure` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `batterypower`
--

DROP TABLE IF EXISTS `batterypower`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `batterypower` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` timestamp NOT NULL,
  `batteryPower` int(4) unsigned NOT NULL,
  `idEstacao` varchar(50) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `idEstacaoBatteryPower` (`idEstacao`) USING BTREE,
  CONSTRAINT `idEstacaoBatteryPower` FOREIGN KEY (`idEstacao`) REFERENCES `estacao` (`idEstacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `batterypower`
--

LOCK TABLES `batterypower` WRITE;
/*!40000 ALTER TABLE `batterypower` DISABLE KEYS */;
/*!40000 ALTER TABLE `batterypower` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estacao`
--

DROP TABLE IF EXISTS `estacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estacao` (
  `idEstacao` varchar(50) NOT NULL,
  `lat` float DEFAULT NULL,
  `lon` float DEFAULT NULL,
  `Altitude` int(10) DEFAULT NULL,
  `Vegetacao` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `ativo` tinyint(4) unsigned NOT NULL DEFAULT '1',
  `observacoes` text,
  PRIMARY KEY (`idEstacao`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estacao`
--

LOCK TABLES `estacao` WRITE;
/*!40000 ALTER TABLE `estacao` DISABLE KEYS */;
/*!40000 ALTER TABLE `estacao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `metal`
--

DROP TABLE IF EXISTS `metal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `metal` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` timestamp NOT NULL,
  `metal` int(10) NOT NULL,
  `idEstacao` varchar(50) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `idEstacaometal` (`idEstacao`) USING BTREE,
  CONSTRAINT `idEstacaometal` FOREIGN KEY (`idEstacao`) REFERENCES `estacao` (`idEstacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `metal`
--

LOCK TABLES `metal` WRITE;
/*!40000 ALTER TABLE `metal` DISABLE KEYS */;
/*!40000 ALTER TABLE `metal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `outdoorhumidity`
--

DROP TABLE IF EXISTS `outdoorhumidity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `outdoorhumidity` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` timestamp NOT NULL,
  `OutdoorHumidity` float NOT NULL,
  `IdEstacao` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idEstacaoOutdoorHum` (`IdEstacao`),
  CONSTRAINT `idEstacaoOutdoorHum` FOREIGN KEY (`IdEstacao`) REFERENCES `estacao` (`idEstacao`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `outdoorhumidity`
--

LOCK TABLES `outdoorhumidity` WRITE;
/*!40000 ALTER TABLE `outdoorhumidity` DISABLE KEYS */;
/*!40000 ALTER TABLE `outdoorhumidity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `outdoortemperature`
--

DROP TABLE IF EXISTS `outdoortemperature`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `outdoortemperature` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` timestamp NOT NULL,
  `OutdoorTemperature` float NOT NULL,
  `IdEstacao` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `IdEstacao` (`IdEstacao`),
  CONSTRAINT `idEstacaoOutdoorTemp` FOREIGN KEY (`IdEstacao`) REFERENCES `estacao` (`idEstacao`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `outdoortemperature`
--

LOCK TABLES `outdoortemperature` WRITE;
/*!40000 ALTER TABLE `outdoortemperature` DISABLE KEYS */;
/*!40000 ALTER TABLE `outdoortemperature` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rain24hours`
--

DROP TABLE IF EXISTS `rain24hours`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rain24hours` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` timestamp NOT NULL,
  `Rain24Hours` float unsigned NOT NULL,
  `idEstacao` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idEstacaorain24` (`idEstacao`),
  CONSTRAINT `idEstacaorain24` FOREIGN KEY (`idEstacao`) REFERENCES `estacao` (`idEstacao`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rain24hours`
--

LOCK TABLES `rain24hours` WRITE;
/*!40000 ALTER TABLE `rain24hours` DISABLE KEYS */;
/*!40000 ALTER TABLE `rain24hours` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rain60minutes`
--

DROP TABLE IF EXISTS `rain60minutes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rain60minutes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` timestamp NOT NULL,
  `Rain60Minutes` float unsigned NOT NULL,
  `idEstacao` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idEstacao` (`idEstacao`) USING BTREE,
  CONSTRAINT `idEstacaorain60` FOREIGN KEY (`idEstacao`) REFERENCES `estacao` (`idEstacao`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rain60minutes`
--

LOCK TABLES `rain60minutes` WRITE;
/*!40000 ALTER TABLE `rain60minutes` DISABLE KEYS */;
/*!40000 ALTER TABLE `rain60minutes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `soilhumidity`
--

DROP TABLE IF EXISTS `soilhumidity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `soilhumidity` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` timestamp NOT NULL,
  `soilHumidity` int(10) unsigned NOT NULL,
  `idEstacao` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `idEstacaoSoilHumidity` (`idEstacao`) USING BTREE,
  CONSTRAINT `idEstacaoSoilHumidity` FOREIGN KEY (`idEstacao`) REFERENCES `estacao` (`idEstacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `soilhumidity`
--

LOCK TABLES `soilhumidity` WRITE;
/*!40000 ALTER TABLE `soilhumidity` DISABLE KEYS */;
/*!40000 ALTER TABLE `soilhumidity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `soiltemperature`
--

DROP TABLE IF EXISTS `soiltemperature`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `soiltemperature` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` timestamp NOT NULL,
  `soilTemperature` float NOT NULL,
  `idEstacao` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `idEstacaoSoilTemperature` (`idEstacao`) USING BTREE,
  CONSTRAINT `idEstacaoSoilTemperature` FOREIGN KEY (`idEstacao`) REFERENCES `estacao` (`idEstacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `soiltemperature`
--

LOCK TABLES `soiltemperature` WRITE;
/*!40000 ALTER TABLE `soiltemperature` DISABLE KEYS */;
/*!40000 ALTER TABLE `soiltemperature` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `solarpower`
--

DROP TABLE IF EXISTS `solarpower`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `solarpower` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` timestamp NOT NULL,
  `solarPower` float NOT NULL DEFAULT '0',
  `idEstacao` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `idEstacaoSolarPower` (`idEstacao`) USING BTREE,
  CONSTRAINT `idEstacaoSolarPower` FOREIGN KEY (`idEstacao`) REFERENCES `estacao` (`idEstacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `solarpower`
--

LOCK TABLES `solarpower` WRITE;
/*!40000 ALTER TABLE `solarpower` DISABLE KEYS */;
/*!40000 ALTER TABLE `solarpower` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sunlightuvindex`
--

DROP TABLE IF EXISTS `sunlightuvindex`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sunlightuvindex` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` timestamp NOT NULL,
  `SunlightUVIndex` float NOT NULL,
  `idEstacao` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `idEstacaoSunUV` (`idEstacao`) USING BTREE,
  CONSTRAINT `idEstacaoSunUV` FOREIGN KEY (`idEstacao`) REFERENCES `estacao` (`idEstacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sunlightuvindex`
--

LOCK TABLES `sunlightuvindex` WRITE;
/*!40000 ALTER TABLE `sunlightuvindex` DISABLE KEYS */;
/*!40000 ALTER TABLE `sunlightuvindex` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sunlightvisible`
--

DROP TABLE IF EXISTS `sunlightvisible`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sunlightvisible` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` timestamp NULL DEFAULT NULL,
  `SunlightVisible` int(10) DEFAULT NULL,
  `idEstacao` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idEstacaoSunVisible` (`idEstacao`),
  CONSTRAINT `idEstacaoSunVisible` FOREIGN KEY (`idEstacao`) REFERENCES `estacao` (`idEstacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sunlightvisible`
--

LOCK TABLES `sunlightvisible` WRITE;
/*!40000 ALTER TABLE `sunlightvisible` DISABLE KEYS */;
/*!40000 ALTER TABLE `sunlightvisible` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `winddirection`
--

DROP TABLE IF EXISTS `winddirection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `winddirection` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` timestamp NOT NULL,
  `WindDirection` varchar(5) NOT NULL,
  `idEstacao` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `idEstacaoWindDirection` (`idEstacao`) USING BTREE,
  CONSTRAINT `idEstacaoWindDirection` FOREIGN KEY (`idEstacao`) REFERENCES `estacao` (`idEstacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `winddirection`
--

LOCK TABLES `winddirection` WRITE;
/*!40000 ALTER TABLE `winddirection` DISABLE KEYS */;
/*!40000 ALTER TABLE `winddirection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `windspeed`
--

DROP TABLE IF EXISTS `windspeed`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `windspeed` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` timestamp NULL DEFAULT NULL,
  `WindSpeed` float DEFAULT NULL,
  `idEstacao` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `idEstacaoWindSpeed` (`idEstacao`) USING BTREE,
  CONSTRAINT `idEstacaoWindSpeed` FOREIGN KEY (`idEstacao`) REFERENCES `estacao` (`idEstacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `windspeed`
--

LOCK TABLES `windspeed` WRITE;
/*!40000 ALTER TABLE `windspeed` DISABLE KEYS */;
/*!40000 ALTER TABLE `windspeed` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-12 15:32:03
