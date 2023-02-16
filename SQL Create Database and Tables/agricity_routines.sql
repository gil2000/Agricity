-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
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
-- Temporary view structure for view `msgid2`
--

DROP TABLE IF EXISTS `msgid2`;
/*!50001 DROP VIEW IF EXISTS `msgid2`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `msgid2` AS SELECT 
 1 AS `barometricpressure`,
 1 AS `soilhumidity`,
 1 AS `soiltemperature`,
 1 AS `winddirection`,
 1 AS `windspeed`,
 1 AS `created_at`,
 1 AS `idEstacao`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `msgid1`
--

DROP TABLE IF EXISTS `msgid1`;
/*!50001 DROP VIEW IF EXISTS `msgid1`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `msgid1` AS SELECT 
 1 AS `outdoorhumidity`,
 1 AS `outdoortemperature`,
 1 AS `rain24hours`,
 1 AS `rain60minutes`,
 1 AS `sunlightuvindex`,
 1 AS `sunlightvisible`,
 1 AS `created_at`,
 1 AS `idEstacao`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `msgid2`
--

/*!50001 DROP VIEW IF EXISTS `msgid2`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`equipa`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `msgid2` AS select `bar`.`valor` AS `barometricpressure`,`shum`.`valor` AS `soilhumidity`,`stemp`.`valor` AS `soiltemperature`,`windir`.`valor` AS `winddirection`,`wspeed`.`valor` AS `windspeed`,`bar`.`created_at` AS `created_at`,`bar`.`idEstacao` AS `idEstacao` from ((((`barometricpressure` `bar` join `soilhumidity` `shum`) join `soiltemperature` `stemp`) join `winddirection` `windir`) join `windspeed` `wspeed`) where ((`bar`.`created_at` = `shum`.`created_at`) and (`shum`.`created_at` = `stemp`.`created_at`) and (`stemp`.`created_at` = `windir`.`created_at`) and (`windir`.`created_at` = `wspeed`.`created_at`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `msgid1`
--

/*!50001 DROP VIEW IF EXISTS `msgid1`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`equipa`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `msgid1` AS select `outdoorhumidity`.`valor` AS `outdoorhumidity`,`outdoortemperature`.`valor` AS `outdoortemperature`,`rain24hours`.`valor` AS `rain24hours`,`rain60minutes`.`valor` AS `rain60minutes`,`sunlightuvindex`.`valor` AS `sunlightuvindex`,`sunlightvisible`.`valor` AS `sunlightvisible`,`outdoorhumidity`.`created_at` AS `created_at`,`outdoorhumidity`.`idEstacao` AS `idEstacao` from (((((`outdoorhumidity` join `outdoortemperature`) join `rain24hours`) join `rain60minutes`) join `sunlightuvindex`) join `sunlightvisible`) where ((`outdoorhumidity`.`created_at` = `outdoortemperature`.`created_at`) and (`outdoortemperature`.`created_at` = `rain24hours`.`created_at`) and (`rain24hours`.`created_at` = `rain60minutes`.`created_at`) and (`rain60minutes`.`created_at` = `sunlightuvindex`.`created_at`) and (`sunlightuvindex`.`created_at` = `sunlightvisible`.`created_at`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-16 11:53:37
