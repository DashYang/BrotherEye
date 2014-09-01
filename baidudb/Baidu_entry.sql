DROP TABLE IF EXISTS `entry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `entry` (
  `id` varchar(12) NOT NULL,
  `belongto` varchar(200) DEFAULT NULL,
  `reply` varchar(12) DEFAULT NULL,
  `author` varchar(30) DEFAULT NULL,
  `title` varchar(65) DEFAULT NULL,
  `userid` varchar(12) DEFAULT NULL,
  `link` varchar(40) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `entry`
--


