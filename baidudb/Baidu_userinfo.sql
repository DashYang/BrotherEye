DROP TABLE IF EXISTS `userinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userinfo` (
  `username` varchar(30) NOT NULL,
  `sex` varchar(5) DEFAULT NULL,
  `location` varchar(30) DEFAULT NULL,
  `birthplace` varchar(30) DEFAULT NULL,
  `fans` varchar(11) DEFAULT NULL,
  `follows` varchar(11) DEFAULT NULL,
  `portrait` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
