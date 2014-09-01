DROP TABLE IF EXISTS `comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comment` (
  `post_id` varchar(12) NOT NULL,
  `belongto` varchar(12) NOT NULL,
  `user_id` varchar(12) DEFAULT NULL,
  `user_name` varchar(30) DEFAULT NULL,
  `user_sex` int(11) DEFAULT NULL,
  `level_id` int(11) DEFAULT NULL,
  `level_name` varchar(20) DEFAULT NULL,
  `bawu` int(11) DEFAULT NULL,
  `open_type` varchar(20) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL,
  `content` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`post_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;


