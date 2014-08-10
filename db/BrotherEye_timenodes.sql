CREATE DATABASE  IF NOT EXISTS `BrotherEye` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `BrotherEye`;
-- MySQL dump 10.13  Distrib 5.5.37, for debian-linux-gnu (x86_64)
--
-- Host: 127.0.0.1    Database: BrotherEye
-- ------------------------------------------------------
-- Server version	5.5.37-0ubuntu0.12.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `timenodes`
--

DROP TABLE IF EXISTS `timenodes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `timenodes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nextnode` int(11) NOT NULL,
  `time_description` varchar(120) NOT NULL,
  `time_owner` int(11) NOT NULL,
  `display` varchar(5) NOT NULL DEFAULT 'true',
  `event_headnode` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `timenodes`
--

LOCK TABLES `timenodes` WRITE;
/*!40000 ALTER TABLE `timenodes` DISABLE KEYS */;
INSERT INTO `timenodes` VALUES (40,41,'世界诞生',6,'true',0),(41,58,'天启入侵（正义联盟诞生）',6,'true',0),(42,0,'???',6,'false',0),(43,0,'???????',6,'false',0),(44,0,'不测',6,'false',0),(45,59,'恶人之旅（0）',6,'true',0),(46,47,'正义联盟的日常（1）',6,'true',0),(47,56,'恶人之旅（1）',6,'true',0),(48,53,'豹女之秘',6,'true',0),(49,54,'亚特兰帝斯王座',6,'true',0),(50,51,'正义联盟的日常（2）',6,'true',0),(51,63,'沙赞！',6,'true',0),(52,46,'猫头鹰之夜',6,'true',0),(53,49,'第三军团崛起',6,'true',0),(54,55,'初灯之怒',6,'true',0),(55,61,'世上最凶（美国正义联盟出击）',6,'true',0),(56,48,'国际正义联盟解散',6,'true',0),(57,45,'信号大师（国际正义联盟成立）',6,'true',0),(58,57,'黑暗之中（黑暗正义联盟起源）',6,'true',0),(59,60,'月之暗面（风暴守卫登场）',6,'true',0),(60,52,'超临界',6,'true',0),(61,62,'觉醒的恶魔',6,'true',0),(62,50,'背叛（抹杀风暴守卫）',6,'true',0),(63,64,' 三体之战（1）',6,'true',0),(64,0,'三体之战（2）',6,'true',0);
/*!40000 ALTER TABLE `timenodes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-08-10 18:48:58
