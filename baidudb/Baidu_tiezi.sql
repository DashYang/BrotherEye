DROP TABLE IF EXISTS `tiezi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tiezi` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) DEFAULT NULL,
  `reply` varchar(600) DEFAULT NULL,
  `url` varchar(200) DEFAULT NULL,
  `comment` varchar(65) DEFAULT NULL,
  `tieba` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3221 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

